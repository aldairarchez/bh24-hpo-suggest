# Step 1: 1️⃣ Prepare Your Data

# Step 2: 1 install gensim
```
pip install gensim
```
# step 3️⃣: Train the Word2Vec Model
# step 4️⃣: Use the Model for Predictions

# Output example
[('HP:0001363', 0.87), ('HP:0000194', 0.84), ('HP:0002650', 0.82)]

# 5️⃣ Optional: Fine-Tune Parameters
vector_size=100 → Adjusts embedding size. Higher values capture more info but require more data.
window=5 → Context window. Larger values capture long-range dependencies.
min_count=1 → Minimum occurrences for a term to be included.
sg=1 → Skip-gram (for rare words). Use sg=0 for CBOW (faster but less accurate for rare terms).
