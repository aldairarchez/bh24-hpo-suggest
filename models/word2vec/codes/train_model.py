import gensim
from gensim.models import Word2Vec
import argparse

# Function to load and preprocess training data
def load_training_data(file_path):
    with open(file_path, "r") as f:
        return [line.strip().split(",") for line in f]  # HPO terms are comma-separated

# Train and save the Word2Vec model
def train_model(train_file, model_file, vector_size=100, window=5, min_count=1, workers=4):
    data = load_training_data(train_file)
    model = Word2Vec(sentences=data, vector_size=vector_size, window=window, min_count=min_count, workers=workers)
    model.save(model_file)
    print(f"Model saved as {model_file}")

# Command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a Word2Vec model with HPO term data.")
    parser.add_argument("train_file", type=str, help="Path to the training data file")
    parser.add_argument("model_file", type=str, help="Path to save the trained model")
    args = parser.parse_args()

    train_model(args.train_file, args.model_file)
