#!/usr/bin/env python3
import argparse
from gensim.models import Word2Vec
import logging
from collections import defaultdict
import os
import numpy as np

# Configure logging
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO
)

class HPOCorpus:
    """Optimized corpus iterator with frequency-aware shuffling"""
    
    def __init__(self, file_path, delimiter=','):
        self.file_path = file_path
        self.delimiter = delimiter
        self.term_freq = defaultdict(int)
        
        # First pass to build frequency stats
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                terms = [term.strip() for term in line.strip().split(delimiter) if term.strip()]
                for term in terms:
                    self.term_freq[term] += 1

    def __iter__(self):
        """Yield term sequences with frequency-based shuffling"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            for line in f:
                terms = [term.strip() for term in line.strip().split(self.delimiter) if term.strip()]
                if len(terms) >= 2:  # Only meaningful sequences
                    # Frequency-weighted shuffling (rare terms appear earlier)
                    terms.sort(key=lambda x: self.term_freq[x])
                    yield terms

def train_optimized_model(train_file, model_file):
    """
    Train the ultimate optimized Word2Vec model with:
    - Two-phase training
    - Frequency-aware processing
    - Hybrid hs/negative sampling
    """
    corpus = HPOCorpus(train_file)
    
    # Phase 1: Initial training with higher learning rate
    model = Word2Vec(
        sentences=corpus,
        vector_size=128,        # Optimal for HPO relationships
        window=7,              # Best context window size
        min_count=1,
        workers=os.cpu_count(),
        epochs=50,             # Initial training
        sg=0,                  # CBOW performs better
        hs=1,                  # Hierarchical softmax
        negative=5,            # Negative sampling
        ns_exponent=0.7,       # Balanced frequency weighting
        alpha=0.035,           # Higher initial rate
        min_alpha=0.001,
        sample=1e-5,           # Aggressive subsampling
        cbow_mean=1,
        sorted_vocab=1,
        batch_words=20000,     # Optimized batch size
        compute_loss=True
    )
    
    # Phase 2: Refinement with decaying learning rate
    model.train(
        corpus,
        total_examples=model.corpus_count,
        epochs=20,
        start_alpha=0.001,
        end_alpha=0.0001
    )
    
    # Add frequency data to model for downstream use
    model.term_freq = dict(corpus.term_freq)
    
    # Enhanced model saving
    model.save(model_file)
    logging.info(f"Model saved to {model_file}")
    
    # Print training summary
    vocab_size = len(model.wv)
    median_freq = np.median(list(corpus.term_freq.values()))
    logging.info(f"Training complete. Vocab size: {vocab_size}, Median term frequency: {median_freq}")
    
    return model

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Train ultimate optimized Word2Vec model for HPO terms',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("train_file", help="Path to training data file")
    parser.add_argument("model_file", help="Path to save trained model")
    args = parser.parse_args()
    
    try:
        trained_model = train_optimized_model(args.train_file, args.model_file)
        
        # Quick validation
        if len(trained_model.wv) > 10:
            sample_term = next(iter(trained_model.wv.key_to_index))
            logging.info(f"Sample prediction for '{sample_term}': {trained_model.wv.most_similar(sample_term)[0]}")
    except Exception as e:
        logging.error(f"Training failed: {str(e)}")
        raise
