import pronto
import csv
from collections import Counter

# Load HPO ontology
ontology = pronto.Ontology("hp.obo")  # Ensure you have an updated HPO file

def suggest_hpo_terms(hpo_list):
    suggested_terms = []
    for hpo_id in hpo_list:
        if hpo_id in ontology:
            term = ontology[hpo_id]
            # Get related terms (parents, children, or siblings)
            related_terms = term.parents | term.children | term.siblings
            suggested_terms.extend([t.id for t in related_terms])

    # Get the most common suggested term
    if suggested_terms:
        most_common_term = Counter(suggested_terms).most_common(1)[0][0]
        return most_common_term
    return None

# Read the input file and process each row
input_file = "hpo_combinations.txt"
output_file = "hpo_predictions.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        predicted_term = suggest_hpo_terms(row)
        writer.writerow(row + [predicted_term] if predicted_term else row + ["No prediction"])
