import gensim
from gensim.models import Word2Vec
import argparse

# Load test data with comma-separated HPO terms
def load_test_data(file_path):
    with open(file_path, "r") as f:
        return [line.strip().split(",") for line in f]  # Comma-separated HPOs

# Order-dependent evaluation: Predict only the next term
def predict_next_term(model, test_data, k_values):
    print("\nPREDICT NEXT TERM\n")

    for k in k_values:
        print(f"k={k}")
        print("n\texact\twrong")

        for num_input_terms in range(8):  # Evaluating from 0 to 7 input terms
            exact_matches = 0
            incorrect = 0

            for line in test_data:
                if len(line) <= num_input_terms + 1:
                    continue  # Skip if not enough terms

                input_terms = line[: num_input_terms + 1]  # Growing input sequence
                expected_term = line[num_input_terms + 1]  # Next term to predict

                try:
                    predicted_terms = [t for t, _ in model.wv.most_similar(input_terms, topn=k)]
                except KeyError:
                    incorrect += 1  # Input terms not in vocabulary
                    continue  

                if expected_term in predicted_terms:
                    exact_matches += 1
                else:
                    incorrect += 1

            print(f"{num_input_terms}\t{exact_matches}\t{incorrect}")
        print()  # Blank line for readability

# Order-independent evaluation: Predict any of the remaining terms
def predict_future_terms(model, test_data, k_values):
    print("\nPREDICT FUTURE TERMS\n")

    for k in k_values:
        print(f"k={k}")
        print("n\texact\twrong")

        for num_input_terms in range(8):  # Evaluating from 0 to 7 input terms
            exact_matches = 0
            incorrect = 0

            for line in test_data:
                if len(line) <= num_input_terms + 1:
                    continue  # Skip if not enough terms

                input_terms = line[: num_input_terms + 1]  # Growing input sequence
                remaining_terms = set(line[num_input_terms + 1:])  # Remaining terms to predict

                try:
                    predicted_terms = [t for t, _ in model.wv.most_similar(input_terms, topn=k)]
                except KeyError:
                    incorrect += 1  # Input terms not in vocabulary
                    continue  

                if any(term in predicted_terms for term in remaining_terms):
                    exact_matches += 1
                else:
                    incorrect += 1

            print(f"{num_input_terms}\t{exact_matches}\t{incorrect}")
        print()  # Blank line for readability

# Command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a trained Word2Vec model on HPO term prediction.")
    parser.add_argument("model_file", type=str, help="Path to the trained model file")
    parser.add_argument("test_file", type=str, help="Path to the test data file")
    args = parser.parse_args()

    # Load model and test data
    model = Word2Vec.load(args.model_file)
    test_data = load_test_data(args.test_file)

    # Define k values
    k_values = [1, 3, 5, 10]

    # Run evaluations
    predict_next_term(model, test_data, k_values)
    predict_future_terms(model, test_data, k_values)
