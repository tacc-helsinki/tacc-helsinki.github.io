"""
A Python script for generating bibliographies from DOI-identifiers.

Usage:


BSD-3 license, Copyright (c) 2018, Markus Rauhalahti
"""

from autobib import get_bibtex_entry
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import feedparser


def tuhat2doilist(url_of_rss_base):
    """
    Takes in as an argument a RSS feed from a TUHAT page without the page identifier. Eg
    RSS feed: https://tuhat.helsinki.fi/portal/fi/persons/dage-sundholm(0d4f606d-d7cf-459d-89cb-3208e73f9a82)/publications.rss?pageSize=all&page=3
    Input: https://tuhat.helsinki.fi/portal/fi/persons/dage-sundholm(0d4f606d-d7cf-459d-89cb-3208e73f9a82)/publications.rss?pageSize=all&page=         <---- no 3 :)

    Returns all the DOI identifiers as a list.

    Quite ugly but works for now.

    """
    doilist = []
    def rss2doilist(rss):
        entries = rss.entries
        if len(entries) == 0:
            # If the RSS feed of a given page does not contain any entries, terminate
            return False
        doilist = []
        for entry in entries:
            # A very ugly way to get the doi from a html.
            html = entry['summary']
            parsed_html = BeautifulSoup(html)
            tds = [str(el) for el in parsed_html.find_all('td')]
            try:
                doi_td = [td.split() for td in tds if 'doi' in td][0]
            except:
                continue
            doi =  ['/'.join(i.replace('"', '').split("/")[-2:]) for i in doi_td if i.startswith('href')][0]
            doilist.append(doi)
        return doilist
    page = 0
    while True:
        rss = feedparser.parse(url_of_rss_base + str(page))
        result = rss2doilist(rss) # Either False if all pages have been crawled, otherwise a list of DOIs
        if result == False:
            break
        else:
            doilist += result
        page +=1
    return doilist

def doilist2biblist(doilist,to_string=True):
    """
    Converts a list of DOIs to either a list of dicts with the data, or to list of .bib's
    if to_string is set to True
    """
    bibs = [get_bibtex_entry(doi) for doi in doilist]
    if to_string:
        db = BibDatabase()
        db.entries(bibs)
        bibs = bibtexparser.dumps(db, BibTexWriter())
    return bibs
