#  Webpage of the theoretical and computational chemistry (TACC) group, University of Helsinki.

The webpage is hosted on github pages, built on top of [Jekyll Now](https://github.com/barryclark/jekyll-now).


# TODO

## General

* This is a very rough version!
* Are more pages required? Eg for conferences, courses
* We should use a domain name from the university

## People
* How should the people be partitioned?
* Some sort of model for people object with following fields:
  * Name
  * Picture
  * Status (pi, researcher, postdoc, phd student, student, visitor, alumni)
  * Personal webpage
  * Email
  * Description

* Personal webpage could easily be rendered from a such model, /people/firstname_lastname/

## Publications
* TUHAT webpage has a RSS-feed containing DOI identifiers. These can be transformed to a bibliography by:
  1) Parsing the DOIs
  2) DOI -> .bib, using eg. [doi2bib](https://github.com/bibcure/doi2bib) or [autobib.py](https://gist.github.com/dhimmel/719fc5e3a21dd2779d9fe69bf41e6ba6/34cb3b10ebe25cb424c1506172857c6f2c307d26) by dhimmel.
  3) bib -> rendered reference, with eg. bibtex?
  3) Rendered to a list, sorted by date
* A model could be generated that contains a rendered references, url to arxiv, graphical abstract
## Software
* Links to repositories, articles, etc...
## Research
* Descriptions of research
