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
```
# Output example

|[('HP:0001363', 0.87), ('HP:0000194', 0.84), ('HP:0002650', 0.82)]|
|-|

# 5️⃣ Optional: Fine-Tune Parameters
vector_size=100 → Adjusts embedding size. Higher values capture more info but require more data.
window=5 → Context window. Larger values capture long-range dependencies.
min_count=1 → Minimum occurrences for a term to be included.
sg=1 → Skip-gram (for rare words). Use sg=0 for CBOW (faster but less accurate for rare terms).
