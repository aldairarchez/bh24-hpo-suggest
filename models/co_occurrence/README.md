# Co-occurrence model for HPO suggestion

## Overview

This is a co-occurrence model for predicting the next HPO term in a sequence given similarly-formatted training data.

Files:

* predict_next_hpo.py: HPO suggestion model
* create_datasets.sh: The commands that were used to generate the train, validation, and test files
* collapse_duplicates.py: Remove duplicates, while preserving order
* flatten_hpos.py: Remove duplicates more aggressively, ignoring order
* hpo.py: HPO helper library (also used to create HPO term adjacency file for others on the team)


## Requirements

* Python 3

* Python packages

    Set up python virtualenv and install package dependencies

    ```
    $ python3 -m venv venv
    $ . venv/bin/activate
    (venv) pip install -r requirements.txt
    ```

* Download hpo.obo

    ```
    wget https://github.com/obophenotype/human-phenotype-ontology/releases/latest/download/hp.obo
    ```


## Running the model

The following command will fit the model to the training data and print out the results

```
(venv) python predict_next_hpo.py hpo_train_flat.txt hpo_test_dedup.txt hp.obo
```

This should result in expected output such as:
```
INFO:hpo:Parsing graph...
INFO:hpo:HPO version: 1.2
INFO:hpo:Found 18988 HP nodes (22814 terms) in graph
DEBUG:hpo:Here are 5:
DEBUG:hpo:  0: HP:0011791
DEBUG:hpo:  1: HP:0045028
DEBUG:hpo:  2: HP:0011788
DEBUG:hpo:  3: HP:0045026
DEBUG:hpo:  4: HP:0100576
INFO:__main__:Found 6644 unique terms
PREDICT NEXT TERM
n   exact   close   wrong
k=1
0   0   0   6911
1   221 26  5983
2   133 24  4562
3   116 17  3010
4   82  7   1992
5   39  6   1342
6   25  4   946
7   12  3   688
k=3
0   3   0   6908
1   445 60  5725
2   322 55  4342
3   263 46  2834
4   163 22  1896
5   84  18  1285
6   44  14  917
7   32  13  658
[...]
```

