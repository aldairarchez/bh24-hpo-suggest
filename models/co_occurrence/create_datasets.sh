# Split data into training and test datasets
grep '202[1-3]] GET' log_pcf_ds_20210608_20240826.txt > raw_train.txt
grep '2024] GET' log_pcf_ds_20210608_20240826.txt > raw_test.txt

# Clean data
cat raw_train.txt | sed -e 's/&filter.*//' | sed -e 's/^.*phenotype=//' | sed -e 's/_ja//g' | egrep '^[,HP:0-9]*$' > hpo_train.txt
cat raw_test.txt | sed -e 's/&filter.*//' | sed -e 's/^.*phenotype=//' | sed -e 's/_ja//g' | egrep '^[,HP:0-9]*$' > hpo_test.txt

# Deduplicate data
python3 collapse_duplicates.py < hpo_train.txt > hpo_train_dedup.txt
python3 collapse_duplicates.py < hpo_test.txt > hpo_test_and_validation_dedup.txt

# Split non-training data into equal validation and test datasets
head -n 8957 hpo_test_and_validation_dedup.txt > hpo_validation_dedup.txt
tail -n 8957 hpo_test_and_validation_dedup.txt > hpo_test_dedup_new.txt

# Create alternative training file for co-occurrence model
python3 flatten_hpos.py < hpo_train.txt > hpo_train_flat.txt