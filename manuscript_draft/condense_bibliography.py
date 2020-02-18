#!/usr/bin/env python

from bibtexparser.bparser import BibTexParser
import sys
import string
import glob
import re
import numpy as np
 
bblfiles = glob.glob('*.bbl')
bibfiles = glob.glob('*.bib')
 
if len(bblfiles) > 1:
    for i, bbl in enumerate(bblfiles):
        print "[" + str(i) + "]: " + bbl
    bblindex = int(raw_input('Desired bbl file: '))
    bblfile = bblfiles[bblindex]
else: bblfile = bblfiles[0]
 
if len(bibfiles) > 1:
    for i, bbl in enumerate(bibfiles):
        print "[" + str(i) + "]: " + bbl
    bibindex = int(raw_input('Desired bib file: '))
    bibfile = bibfiles[bibindex]
else: bibfile = bibfiles[0]
 
with open(bblfile, 'r') as f:
    lines = f.readlines()
    lines = map(string.strip, lines)
 
# Combine bibitem lines together
# tlines = lines
# bibitems = []
# while True:
#     start = tlines.index('')
#     tlines = tlines[start+1:]
#     try: bibitems += [''.join(tlines[0:tlines.index('')])]
#     except ValueError: break
 
# Splits bibitem into short-author, key, and bibdata
pat1 = re.compile(r'\\bibitem{(.*?)}')
pat2 = re.compile(r'\\bibitem\[(.*?)\]{(.*?)}')
 
keys = pat1.findall(''.join(lines))
if not keys:
    keys = np.array(pat2.findall(''.join(lines)))[:,1].tolist()
 
# Parse bibtex library
with open('library.bib', 'r') as bibf:
    bp = BibTexParser(bibf.read())
 
def to_bibtex(data):
    bibtex = ''
    for entry in sorted(data.keys()):
        bibtex += ('@' + data[entry]['ENTRYTYPE'] + '{' + data[entry]['ID'] +
                   ",\n")
 
        for field in [i for i in sorted(data[entry]) if i not in
                      ['ENTRYTYPE', 'ID']]:
            bibtex += " " + field + " = {" + data[entry][field] + "},\n"
        bibtex += "}\n\n"
    return bibtex
 
bp_dict = bp.get_entry_dict()
 
cond_dict = {}
 
entries = ['chapter', 'publisher', 'author', 'year', 'booktitle',
           'title', 'volume', 'ENTRYTYPE', 'number', 'month', 'volume',
           'pages', 'year', 'journal', 'ID']
for key in keys:
    inentry = bp_dict[key]
    outentry = {}
 
    # Process bibtex entry:
    for inkey in inentry.keys():
        if inkey in entries:
            outentry[inkey] = inentry[inkey]
 
    # Correct Mendeley's dumb naming error
    try:
        t_author = str(outentry['author'])
    except:
        print 'ERROR: Unrecognized character in author name.\n'
        print outentry['author']

    t_author = t_author.replace(' a ', ' A ')
 
    if outentry['author'][-2:] == ' a':
        t_author = t_author[:-2] + ' A'
 
    # Fix Frank's name
    t_author = t_author.replace('Doyle, F', r'{Doyle~III}, F')

    outentry['author'] = t_author
    
    try:
        # Remove abbreviated page numbers
        pages = outentry['pages']
        page1 = pages[:pages.index('--')]
        page2 = pages[pages.index('--')+2:]
        if len(page2) < len(page1):
            diff = len(page1) - len(page2)
            page2 = page1[:diff] + page2
 
        outentry['pages'] = page1 + '--' + page2
    except (KeyError, ValueError): pass
 	
    #fix the periods remaining in the titles:
    if outentry['title'][-1]=='.':
        outentry['title']=outentry['title'][:-1]

    #fix dumb month abbreviations
    try:
        outentry['month'] = outentry['month'].capitalize()
        if outentry['month'][-1] is not '.':
            outentry['month'] = outentry['month']+'.'
        # just get rid of them entirely
        outentry['month'] = ''
    except (KeyError, ValueError): pass
    # if outentry['ID'] == 'Chirikjian2009':
    #     outentry['booktitle'] = 'Stochastic Models, Information Theory, and Lie Groups'
    # 
 
    # print outentry['author']
    cond_dict[key] = outentry
 
 
 
with open('condensed_library.bib', 'w') as outbib:
    bibtex = to_bibtex(cond_dict).encode('utf-8')
    outbib.write(bibtex)
