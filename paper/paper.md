---
title: 'BioHackEU23 report: Template for the very long title'
title_short: 'BioHackEU23 #26: unknown chemical substances'
tags:
  - HPO term recommender
  - co-occurrence analysis
  - phenotype
  - rare disease
authors:
  - name: Marlon Aldair Arciniega Sanchez
    orcid: 0000-0000-0000-0000
    affiliation: 1
  - name: Toyofumi Fujiwara
    orcid: 0000-0000-0000-0000
    affiliation: 2
  - name: Surasak Sangkhathat
    orcid: 0000-0000-0000-0000
    affiliation: 3
  - name: Maxat Kulmanov
    orcid: 0000-0000-0000-0000
    affiliation: 4
  - name: Orion Buske
    orcid: 0000-0000-0000-0000
    affiliation: 5
  - name: Atsuko Yamaguchi
    orcid: 0000-0000-0000-0000
    affiliation: 6
affiliations:
  - name: First Affiliation
    index: 1
  - name: Second Affiliation
    index: 2
  - name: Second Affiliation
    index: 3
  - name: Second Affiliation
    index: 4
  - name: Second Affiliation
    index: 5
date: 31 August 2023
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
authors_short: Marlon Aldair Arciniega Sanchez \emph{et al.}
---


# Introduction

The Human Phenotype Ontology (HPO) has become an indispensable resource for researchers and clinicians in the field of rare diseases. Since its introduction in 2008, HPO has grown to include a standardized vocabulary of phenotypic abnormalities associated with over 8,000 diseases [1]. This comprehensive and well-defined set of terms has facilitated deep phenotyping, allowing for more accurate and detailed descriptions of clinical abnormalities [2]. As a result, HPO has become the de facto standard for patient phenotyping in rare diseases, widely adopted by researchers, clinicians, informaticians, and patient registry systems globally [3].
HPO's hierarchical organization and interoperability with other ontologies have significantly enhanced its utility in computational tools [4]. By using HPO for creating patient profiles, patient repositories such as PhenomeCentral [5] and IRUD [6], both participants in the Matchmaker Exchange project, facilitate the precise description and comparison of clinical features across patients [7]. PubCaseFinder, a phenotype-driven differential diagnosis tool, leverages HPO to generate ranked lists of rare diseases by comparing patient phenotypes with known disease profiles [8]. Similarly, LIRICAL utilizes HPO terms to identify potential disease-causing variants from whole-exome or whole-genome sequencing data [9]. These systems underscore the critical role of HPO in modern medical research and diagnostics.
Despite the HPO’s success, one of the ongoing challenges in its application is the effective identification of co-occurring phenotypic terms [10]. The ability to identify and suggest related phenotypic terms not only helps in creating a more complete patient profile but also enhances the accuracy of computational diagnostic tools that rely on phenotype-based comparisons [11].
To address this challenge, we developed a new tool designed to suggest related HPO terms by conducting statistical analysis of previously entered data in PubCaseFinder and Human Phenotype Ontology annotations [3]. This tool leverages the vast amount of phenotypic data already available, providing users with informed suggestions when entering new HPO terms. By offering statistically informed suggestions for related HPO terms, our tool facilitates more accurate and comprehensive deep phenotyping. This, in turn, can lead to more precise creating patient profiles and diagnoses, ultimately contributing to better patient outcomes.


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

# Citation Typing Ontology annotation

You can use [CiTO](http://purl.org/spar/cito/2018-02-12) annotations, as explained in [this BioHackathon Europe 2021 write up](https://raw.githubusercontent.com/biohackrxiv/bhxiv-metadata/main/doc/elixir_biohackathon2021/paper.md) and [this CiTO Pilot](https://www.biomedcentral.com/collections/cito).
Using this template, you can cite an article and indicate _why_ you cite that article, for instance DisGeNET-RDF [@citesAsAuthority:Queralt2016].

The syntax in Markdown is as follows: a single intention annotation looks like
`[@usesMethodIn:Krewinkel2017]`; two or more intentions are separated
with colons, like `[@extends:discusses:Nielsen2017Scholia]`. When you cite two
different articles, you use this syntax: `[@citesAsDataSource:Ammar2022ETL; @citesAsDataSource:Arend2022BioHackEU22]`.

Possible CiTO typing annotation include:

* Robinson PN, Köhler S, Bauer S, Seelow D, Horn D, Mundlos S. The Human Phenotype Ontology: a tool for annotating and analyzing human hereditary disease. Am J Hum Genet. 2008;83(5):610-615. doi:10.1016/j.ajhg.2008.09.017
* Köhler S, Doelken SC, Mungall CJ, et al. The Human Phenotype Ontology project: linking molecular biology and disease through phenotype data. Nucleic Acids Res. 2014;42(Database issue):D966-D974. doi:10.1093/nar/gkt1026
* Köhler S, Carmody L, Vasilevsky N, et al. Expansion of the Human Phenotype Ontology (HPO) knowledge base and resources. Nucleic Acids Res. 2019;47(D1):D1018-D1027. doi:10.1093/nar/gky1105
* Köhler S, Øien NC, Buske OJ, et al. Encoding Clinical Data with the Human Phenotype Ontology for Computational Differential Diagnostics. Curr Protoc Hum Genet. 2019;103(1):e92. doi:10.1002/cphg.92
* Buske OJ, Girdea M, Dumitriu S, et al. PhenomeCentral: a portal for phenotypic and genotypic matchmaking of patients with rare genetic diseases. Hum Mutat. 2015;36(10):931-940. doi:10.1002/humu.22851
* Takahashi Y, Mizusawa H. Initiative on Rare and Undiagnosed Disease in Japan. JMA J. 2021;4(2):112-118. doi:10.31662/jmaj.2021-0003
* Boycott KM, Azzariti DR, Hamosh A, Rehm HL. Seven years since the launch of the Matchmaker Exchange: The evolution of genomic matchmaking. Hum Mutat. 2022;43(6):659-667. doi:10.1002/humu.24373
* Fujiwara T, Yamamoto Y, Kim JD, Buske O, Takagi T. PubCaseFinder: A Case-Report-Based, Phenotype-Driven Differential-Diagnosis System for Rare Diseases. Am J Hum Genet. 2018;103(3):389-399. doi:10.1016/j.ajhg.2018.08.003
* Robinson PN, Ravanmehr V, Jacobsen JOB, et al. Interpretable Clinical Genomics with a Likelihood Ratio Paradigm. Am J Hum Genet. 2020;107(3):403-417. doi:10.1016/j.ajhg.2020.06.021
* Shen F, Wang L, Liu H. Phenotypic Analysis of Clinical Narratives Using Human Phenotype Ontology. Stud Health Technol Inform. 2017;245:581-585.
* Yuan X, Wang J, Dai B, et al. Evaluation of phenotype-driven gene prioritization methods for Mendelian diseases. Brief Bioinform. 2022;23(2):bbac019. doi:10.1093/bib/bbac019


* citesAsDataSource: when you point the reader to a source of data which may explain a claim
* usesDataFrom: when you reuse somehow (and elaborate on) the data in the cited entity
* usesMethodIn
* citesAsAuthority
* citesAsEvidence
* citesAsPotentialSolution
* citesAsRecommendedReading
* citesAsRelated
* citesAsSourceDocument
* citesForInformation
* confirms
* documents
* providesDataFor
* obtainsSupportFrom
* discusses
* extends
* agreesWith
* disagreesWith
* updates
* citation: generic citation


# Results


# Discussion

...

## Acknowledgements

...

## References
