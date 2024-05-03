# LaTeX Source Files

This repository contains several document formats that may be of use for using LaTeX. Contact jhabel01 at gmail dot com for further information.
The .gitignore file here may also be useful in conjunction with any of these repositories for tracking TeX projects on git.

## manuscript_draft
This repostory contains materials for drafting and submitting LaTeX manuscipts. It is set up to be ready to do for 

##### Paper sections

###### Figures
Any `.pdf` or `.png` figures in `/figures` is accessible to the compiler. An example figure is there if needed.

###### Compiling
This directory uses pdflatex and bibtex to compile. To compile in a terminal, do:
```
pdflatex main.tex
bibtex main.aux
pdflatex main.tex
pdflatex main.tex
```
or compile using your favorite IDE.

###### Using bibtex and bibliography files
If you are using this repository, you need to add a bibtex file called library.bib that has your bibtex entries. 
This can be autogenerated by Mendeley or Zotero, please consult these software references for how to do so.
The current draft file is set up to pull from condensed_library.bib.

The python file condense_bibliography.py can be used to strip bibtex entries from a master .bib file. To do so, do:
`python condense_bibliography.py`.

The references are currently formatted according to IEEE standards. Other `.bst` files may be used as needed.

##### Correspondence
There are also form letters in here for cover letters and response letters. There are examples written in each which should help with use.

## poster
Beamer poster format with MGH-appropriate coloring. Follow the readme in there for use. Uses pdflatex to compile. This heavily draws upon the beamerposter LaTeX package (https://ctan.org/pkg/beamerposter) for the heavy lifting, with a MGH style and some added utils.

## slides
This contains a beamer slides format that heavily draws upon the metropolis slide theme (https://www.ctan.org/pkg/beamertheme-metropolis). It has been edited to follow most of the style from the 1976 NASA style guide (https://www.nasa.gov/sites/default/files/atoms/files/nasa_graphics_manual_nhb_1430-2_jan_1976.pdf). Use xelatex to compile.

## CV
This contains a CV format in LaTeX. All sections are obviously optional. This exact version requires the font Avenir (exists on Mac). Other fonts may be specified within. To compile, do `xelatex my-cv.tex`. This is using a remarkably neat format borrowed from Liana Lareau at UC Berkeley.
