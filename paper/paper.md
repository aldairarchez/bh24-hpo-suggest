---
title: 'BioHackathon2024 report: HPO Suggest'
title_short: 'BH2024: HPO Suggest'
tags:
  - HPO term recommender
  - co-occurrence analysis
  - phenotype
  - rare disease
authors:
  - name: Marlon Aldair Arciniega Sanchez
    orcid: 0000-0001-5050-2509
    affiliation: 1
  - name: Atsuko Yamaguchi
    orcid: 0000-0001-5050-2509
    affiliation: 2
  - name: Orion Buske
    orcid: 0000-0001-5050-2509
    affiliation: 3
  - name: Toyofumi Fujiwara
    orcid: 0000-0001-5050-2509
    affiliation: 4
affiliations:
  - name: xxx
    index: 1
  - name: Tokyo City University, Tokyo, Japan
    index: 2
  - name: PhenoTips, Toronto, Canada
    index: 3
  - name: Database Center for Life Science, Joint Support-Center for Data Science Research, Research Organization of Information and Systems, Chiba, Japan
    index: 4
date: 31 August 2024
cito-bibliography: paper.bib
event: BH24
biohackathon_name: "BioHackathon 2024"
biohackathon_url:   "https://2024.biohackathon.org/"
biohackathon_location: "Fukushima, Japan, 2024"
group: HPO suggest group
# URL to project git repo --- should contain the actual paper.md:
git_url: https://github.com/biohackathon-japan/bh24-hpo-suggest
# This is the short authors description that is used at the
# bottom of the generated paper (typically the first two authors):
authors_short: First Author \emph{et al.}
---


# Introduction

The Human Phenotype Ontology (HPO) has become an indispensable resource for researchers and clinicians in the field of rare diseases. Since its introduction in 2008, HPO has grown to include a standardized vocabulary of phenotypic abnormalities associated with over 8,000 diseases [@citation:robinson2008human]. This comprehensive and well-defined set of terms has facilitated deep phenotyping, allowing for more accurate and detailed descriptions of clinical abnormalities [citation:kohler2014human]. As a result, HPO has become the de facto standard for patient phenotyping in rare diseases, widely adopted by researchers, clinicians, informaticians, and patient registry systems globally [citation:kohler2019expansion].

HPO's hierarchical organization and interoperability with other ontologies have significantly enhanced its utility in computational tools [citation:kohler2019encoding]. By using HPO for creating patient profiles, patient repositories such as PhenomeCentral [citation:buske2015phenomecentral] and IRUD [citation:adachi2017japan], both participants in the Matchmaker Exchange project, facilitate the precise description and comparison of clinical features across patients [citation:boycott2022seven]. PubCaseFinder, a phenotype-driven differential diagnosis tool, leverages HPO to generate ranked lists of rare diseases by comparing patient phenotypes with known disease profiles [citation:fujiwara2018pubcasefinder]. Similarly, LIRICAL utilizes HPO terms to identify potential disease-causing variants from whole-exome or whole-genome sequencing data [citation:robinson2020interpretable]. These systems underscore the critical role of HPO in modern medical research and diagnostics.

Despite the HPO’s success, one of the ongoing challenges in its application is the effective identification of co-occurring phenotypic ter [citation:shen2017phenotypic]. The ability to identify and suggest related phenotypic terms not only helps in creating a more complete patient profile but also enhances the accuracy of computational diagnostic tools that rely on phenotype-based comparisons [citation:yuan2022evaluation].

To address this challenge, we developed a new tool designed to suggest related HPO terms by conducting statistical analysis of previously entered data in PubCaseFinder and Human Phenotype Ontology annotations [citation:kohler2019expansion]. This tool leverages the vast amount of phenotypic data already available, providing users with informed suggestions when entering new HPO terms. By offering statistically informed suggestions for related HPO terms, our tool facilitates more accurate and comprehensive deep phenotyping. This, in turn, can lead to more precise creating patient profiles and diagnoses, ultimately contributing to better patient outcomes.


# Method

This document use Markdown and you can look at [this tutorial](https://www.markdowntutorial.com/).

## Data Preprocessing

Please keep sections to a maximum of only two levels.

## Co-occurrence Analysis

Please keep sections to a maximum of only two levels.

## Evaluation

Please keep sections to a maximum of only two levels.


# Result

This document use Markdown and you can look at [this tutorial](https://www.markdowntutorial.com/).

## Data Preprocessing

Please keep sections to a maximum of only two levels.

## Co-occurrence Analysis

Please keep sections to a maximum of only two levels.

## Evaluation

Please keep sections to a maximum of only two levels.


# Discussion

This document use Markdown and you can look at [this tutorial](https://www.markdowntutorial.com/).

## Machine Learning Model

Please keep sections to a maximum of only two levels.

## Data Redundancy

Please keep sections to a maximum of only two levels.

## Evaluation Metrics

Please keep sections to a maximum of only two levels.

## Next Steps

Please keep sections to a maximum of only two levels.



## Tables and figures

Tables can be added in the following way, though alternatives are possible:

Table: Note that table caption is automatically numbered and should be
given before the table itself.

| Header 1 | Header 2 |
| -------- | -------- |
| item 1 | item 2 |
| item 3 | item 4 |

A figure is added with:

![Caption for BioHackrXiv logo figure](./biohackrxiv.png)

# Other main section on your manuscript level 1

Lists can be added with:

1. Item 1
2. Item 2



...

## Acknowledgements

...

## References
