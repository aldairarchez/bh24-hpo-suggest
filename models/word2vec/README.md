# Step 1: 1️⃣ Prepare Your Data
```
python3 -m venv hpo_eval_env
. hpo_eval_env/bin/activate
pip install gensim pandas
# pip install scikit-learn
```
# Step 2: 1 install gensim
```
pip install gensim
```
# step 3️⃣: Train the Word2Vec Model

Running the training script [train_model.py](https://github.com/aldairarchez/bh24-hpo-suggest/blob/main/models/word2vec/codes/train_model.py)
```
python ./scripts/train_model.py ./Data/training_data1.txt hpo_word2vec.model
# python ./scripts/train_model.py ./Data/training_data2.txt hpo_word2vec.model
# python ./scripts/train_model.py ./Data/training_data3.txt hpo_word2vec.model

python ./scripts/train_combined.py ./Data/training_data1.txt hpo_word2vec.model

```
# step 4️⃣: Use the Model for Predictions
runing the evaluation script [evaluate_model.py](https://github.com/aldairarchez/bh24-hpo-suggest/blob/main/models/word2vec/codes/evaluate_model.py)
```
python ./scripts/evaluate_model.py hpo_word2vec.model ./Data/test_data.txt
python ./scripts/evaluate_hybrid.py hpo_word2vec.model ./Data/test_data.txt
```
# Output example

|[('HP:0001363', 0.87), ('HP:0000194', 0.84), ('HP:0002650', 0.82)]|
|-|

# 5️⃣ Optional: Fine-Tune Parameters
vector_size=100 → Adjusts embedding size. Higher values capture more info but require more data.
window=5 → Context window. Larger values capture long-range dependencies.
min_count=1 → Minimum occurrences for a term to be included.
sg=1 → Skip-gram (for rare words). Use sg=0 for CBOW (faster but less accurate for rare terms).


# Optimized Word2Vec for HPO Term Prediction - Technical Report

## Best Performing Configuration

The final optimized parameters that yielded the best results:

```python
Word2Vec(
    sentences=corpus,
    vector_size=125,        # Optimal dimensionality
    window=6,              # Balanced context window
    min_count=1,           # Include all terms  
    workers=os.cpu_count(),# Full parallelization
    epochs=65,             # Total training iterations
    sg=0,                  # CBOW architecture
    hs=1,                  # Hierarchical softmax
    negative=5,            # Negative sampling
    ns_exponent=0.7,       # Frequency weighting
    alpha=0.03,            # Initial learning rate
    min_alpha=0.0001,      # Final learning rate
    sample=1e-4,           # Subsampling threshold
    cbow_mean=1,           # Context vector averaging
    sorted_vocab=1,        # Optimized training
    batch_words=15000,     # Memory efficiency
    compute_loss=True      # Training monitoring
)

## Parameter Tuning History

| Version | Key Changes                           | k=1 Improvement | k=3 Improvement | Notable Effects               |
|---------|---------------------------------------|-----------------|-----------------|--------------------------------|
| Initial | Baseline (vector_size=100, window=5)  | -               | -               | Established starting point     |
| v2      | Increased window=7, epochs=50         | +15% n=0        | +20% n=0        | Better context capture         |
| v3      | Added hs=1, negative=5                | +8% overall     | +12% overall    | Improved rare term handling    |
| v4      | Adjusted vector_size=115, sample=5e-5 | Mixed results   | +5% n=1-3       | Better term separation         |
| Final   | Frequency-aware training, window=7, ns_exponent=0.65 | +22% n=0 | +18% n=1 | Best overall performance |


