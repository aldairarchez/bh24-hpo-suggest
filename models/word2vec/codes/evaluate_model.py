#!/usr/bin/env python3
import logging
from collections import Counter, defaultdict
import sys
from gensim.models import Word2Vec
from hpo import HPO

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_test_data(file_path):
    """Load test data with comma-separated HPO terms"""
    with open(file_path, "r", encoding='utf-8') as f:
        return [line.strip().split(",") for line in f if line.strip()]

def predict_next_term(model, test_data, hpo, k_values):
    """Order-dependent evaluation: Predict only the next term"""
    print("\nPREDICT NEXT TERM\n")

    for k in k_values:
        print(f"k={k}")
        print("n\texact\tclose\twrong")

        for num_input_terms in range(1, 8):  # Evaluating from 0 to 7 input terms
            exact_matches = 0
            close_matches = 0
            incorrect = 0

            for line in test_data:
                if len(line) <= num_input_terms + 1:
                    continue  # Skip if not enough terms

                input_terms = line[:num_input_terms + 1]
                expected_term = line[num_input_terms + 1]

                try:
                    predicted_terms = [t for t, _ in model.wv.most_similar(input_terms, topn=k)]
                except KeyError:
                    incorrect += 1
                    continue

                # Get HPO nodes for evaluation
                predicted_hpos = [hpo.hps.get(t) for t in predicted_terms if hpo.hps.get(t)]
                expected_hpo = hpo.hps.get(expected_term)

                if not expected_hpo:
                    incorrect += 1
                    continue

                if expected_term in predicted_terms:
                    exact_matches += 1
                elif any(hpo_node in get_close_hps([expected_hpo]) for hpo_node in predicted_hpos if hpo_node):
                    close_matches += 1
                else:
                    incorrect += 1

            print(f"{num_input_terms}\t{exact_matches}\t{close_matches}\t{incorrect}")
        print()

def predict_future_terms(model, test_data, hpo, k_values):
    """Order-independent evaluation: Predict any of the remaining terms"""
    print("\nPREDICT FUTURE TERMS\n")

    for k in k_values:
        print(f"k={k}")
        print("n\texact\tclose\twrong")

        for num_input_terms in range(1, 8):  # Evaluating from 0 to 7 input terms
            exact_matches = 0
            close_matches = 0
            incorrect = 0

            for line in test_data:
                if len(line) <= num_input_terms + 1:
                    continue

                input_terms = line[:num_input_terms + 1]
                remaining_terms = line[num_input_terms + 1:]

                try:
                    predicted_terms = [t for t, _ in model.wv.most_similar(input_terms, topn=k)]
                except KeyError:
                    incorrect += 1
                    continue

                # Get HPO nodes for evaluation
                predicted_hpos = [hpo.hps.get(t) for t in predicted_terms if hpo.hps.get(t)]
                remaining_hpos = [hpo.hps.get(t) for t in remaining_terms if hpo.hps.get(t)]

                if not remaining_hpos:
                    incorrect += 1
                    continue

                # Check for exact matches
                if any(t in predicted_terms for t in remaining_terms):
                    exact_matches += 1
                # Check for close matches (parent/child relationships)
                elif any(hpo_node in get_close_hps(remaining_hpos) for hpo_node in predicted_hpos if hpo_node):
                    close_matches += 1
                else:
                    incorrect += 1

            print(f"{num_input_terms}\t{exact_matches}\t{close_matches}\t{incorrect}")
        print()

def get_close_hps(target_hps):
    """Get related HPO terms (parents and children)"""
    close_hps = set()
    for hp in target_hps:
        if hp:  # Skip None values
            close_hps.update(hp.parents)
            close_hps.update(hp.children)
    return close_hps

def main():
    if len(sys.argv) != 4:
        print("Usage: python evaluate_model_NEW.py <model_file> <test_file> <hpo.obo>")
        sys.exit(1)

    model_file = sys.argv[1]
    test_file = sys.argv[2]
    hpo_file = sys.argv[3]

    try:
        logger.info("Loading model...")
        model = Word2Vec.load(model_file)
        
        logger.info("Loading HPO ontology...")
        hpo = HPO(hpo_file)
        
        logger.info("Loading test data...")
        test_data = load_test_data(test_file)
        
        if not test_data:
            logger.error("No valid test data found")
            sys.exit(1)
            
        logger.info("Evaluating model...")
        k_values = [1, 3, 5, 10]  # Your original k values
        
        predict_next_term(model, test_data, hpo, k_values)
        predict_future_terms(model, test_data, hpo, k_values)
        
    except Exception as e:
        logger.error(f"Evaluation failed: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
