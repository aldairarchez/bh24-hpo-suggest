import gensim
from gensim.models import Word2Vec

# Load and preprocess the data
def load_hpo_data(file_path):
    with open(file_path, "r") as f:
        sentences = [line.strip().split() for line in f]
    return sentences

# Path to your dataset
file_path = "hpo_data.txt"

# Load the HPO term combinations
hpo_sentences = load_hpo_data(file_path)

# Train the Word2Vec model
model = Word2Vec(
    sentences=hpo_sentences,  # Input data
    vector_size=100,          # Embedding size (adjustable)
    window=5,                 # Context window size
    min_count=1,              # Minimum term frequency to be included
    workers=4,                # Number of CPU threads
    sg=1                      # Skip-gram (1) or CBOW (0)
)

# Save the model
model.save("hpo_word2vec.model")
print("Model training complete!")
