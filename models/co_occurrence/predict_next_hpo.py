
import os
import sys
import logging

from collections import Counter, defaultdict

import numpy as np

from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt

from hpo import HPO

logger = logging.getLogger(__name__)


class HPOTermRecommender:
    def __init__(self, normalization_method='cosine'):
        self.tag_to_index = {}
        self.index_to_tag = {}
        self.tag_matrix = None
        self.normalization_method = normalization_method

    def _normalize(self, matrix):
        if self.normalization_method == 'cosine':
            return cosine_similarity(matrix)
        elif self.normalization_method == 'l1':
            return normalize(matrix, norm='l1', axis=1)
        elif self.normalization_method == 'softmax':
            exp_matrix = np.exp(matrix)
            return exp_matrix / exp_matrix.sum(axis=1, keepdims=True)
        elif self.normalization_method == 'min_max':
            min_val = matrix.min()
            max_val = matrix.max()
            return (matrix - min_val) / (max_val - min_val)
        else:
            raise ValueError(f"Unknown normalization method: {self.normalization_method}")


    def fit(self, logs):
        # Create term-to-index and index-to-term mappings
        unique_terms = set(term for log in logs for term in log)
        self.term_to_index = {term: i for i, term in enumerate(unique_terms)}
        self.index_to_term = {i: term for term, i in self.term_to_index.items()}

        # Create co-occurrence matrix
        n_terms = len(unique_terms)
        logger.info('Found {} unique terms'.format(n_terms))

        co_occurrence = np.zeros((n_terms, n_terms))
        for log in logs:
            for i in range(len(log)):
                for j in range(i+1, len(log)):
                    term1, term2 = sorted([log[i], log[j]])
                    co_occurrence[(self.term_to_index[term1], self.term_to_index[term2])] += 1

        # Make matrix symmetric
        co_occurrence = co_occurrence + co_occurrence.T

        # Normalize
        self.term_matrix = self._normalize(co_occurrence)

    def predict(self, terms, n=5):
        # for term in terms:
        #     if not term in self.term_to_index:
        #         logger.warning('Ignoring unknown term: {}'.format(term))

        # Get indices for input terms (dropping those that aren't known)
        term_indices = [self.term_to_index[term] for term in terms if term in self.term_to_index]

        # Sum the term vectors for all input terms
        combined_vector = np.sum(self.term_matrix[term_indices], axis=0)

        # Sort terms by combined similarity score
        similar_indices = combined_vector.argsort()[::-1]

        # Get top N recommendations (filtering out input terms)
        recommendations = []
        for idx in similar_indices:
            if self.index_to_term[idx] not in terms:
                recommendations.append(self.index_to_term[idx])
                if len(recommendations) == n:
                    break

        return recommendations

def any_overlap(set1, set2):
    return bool(set(set1).intersection(set2))

def get_close_hps(target_hps):
    close_hps = set()
    for hp in target_hps:
        close_hps.update(hp.parents)
        close_hps.update(hp.children)

    close_hps.difference_update(target_hps)
    return close_hps

def evaluate_accuracy_predicting_next_position(model, test_data, hpo, k=5, max_sequence_length=5):
    results = defaultdict(Counter)

    for log in test_data:
        for i in range(0, min(len(log), max_sequence_length)):
            previous_terms = log[:i]
            actual_next_term = log[i]

            predicted_terms = model.predict(previous_terms, n=k)

            predicted_hps = []
            for t in predicted_terms:
                predicted_hps.append(hpo[t])

            target_hp = hpo[actual_next_term]
            close_hps = get_close_hps([target_hp])

            if target_hp in predicted_hps[:k]:
                results[i]['exact'] += 1
            elif close_hps and any_overlap(close_hps, predicted_hps[:k]):
                results[i]['close'] += 1
            else:
                results[i]['wrong'] += 1

    return results

def evaluate_accuracy_predicting_remainder(model, test_data, hpo, k=5, max_sequence_length=5):
    results = defaultdict(Counter)

    for log in test_data:
        for i in range(0, min(len(log), max_sequence_length)):
            previous_terms = log[:i]
            future_terms = log[i:len(log)]

            predicted_terms = model.predict(previous_terms, n=k)

            predicted_hps = [hpo[t] for t in predicted_terms]
            target_hps = [hpo[t] for t in future_terms]
            close_hps = get_close_hps(target_hps)

            if any_overlap(target_hps, predicted_hps[:k]):
                results[i]['exact'] += 1
            elif close_hps and any_overlap(close_hps, predicted_hps[:k]):
                results[i]['close'] += 1
            else:
                results[i]['wrong'] += 1

    return results

def clean_term(term):
    if term.startswith('HP:'):
        term_id = int(term.split(':', 1)[1])
    else:
        term_id = int(term)

    return 'HP:{:07}'.format(term_id)

def parse_hpo_line_to_terms(line):
    line = line.strip()
    if not line:
        return []

    terms = line.strip().split(',')

    cleaned_terms = []
    for term in terms:
        try:
            cleaned_terms.append(clean_term(term))
        except:
            logging.warning('Skipping un-parseable HPO term: {}'.format(term))

    return cleaned_terms

def read_logs(filename):
    data = []
    with open(filename) as ifp:
        for line in ifp:
            hpos = parse_hpo_line_to_terms(line)
            data.append(hpos)

    return data

def read_hpo_adjacencies(filename):
    data = {}
    with open(filename) as ifp:
        for line in ifp:
            term, rest_of_line = line.strip().split('\t', 1)
            other_terms = parse_hpo_line_to_terms(rest_of_line)
            assert term not in data
            data[term] = set(other_terms)

    return data

def print_results(results):
    for i in sorted(results):
        row = [results[i][res] for res in ['exact', 'close', 'wrong']]
        print('\t'.join(map(str, [i, *row])))

def script(train_file, test_file, hpo_file):
    hpo = HPO(hpo_file)

    data = read_logs(train_file)

    recommender = HPOTermRecommender(normalization_method='l1')
    recommender.fit(data)


    test_data = read_logs(test_file)

    max_sequence_length = 8
    print('PREDICT NEXT TERM')
    print('\t'.join(['n', 'exact', 'close', 'wrong']))
    for k in [1, 3, 5, 10]:
        print('k={}'.format(k))
        results = evaluate_accuracy_predicting_next_position(recommender, test_data, hpo, k, max_sequence_length)
        print_results(results)

    print('PREDICT FUTURE TERMS')
    print('\t'.join(['n', 'exact', 'close', 'wrong']))
    for k in [1, 3, 5, 10]:
        print('k={}'.format(k))
        results = evaluate_accuracy_predicting_remainder(recommender, test_data, hpo, k, max_sequence_length)
        print_results(results)


def parse_args(args):
    from argparse import ArgumentParser
    description = __doc__.strip()
    
    parser = ArgumentParser(description=description)
    parser.add_argument("train_file")
    parser.add_argument("test_file")
    parser.add_argument('hpo_file', metavar="hp.obo")

    return parser.parse_args(args)

def main(args=sys.argv[1:]):
    args = parse_args(args)

    logging.basicConfig(level='DEBUG')

    script(**vars(args))

if __name__ == '__main__':
    sys.exit(main())
