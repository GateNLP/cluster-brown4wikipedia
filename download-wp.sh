#!/bin/bash

## example downloads ...
## if there are many files to download, better to put the links into a file and use parallel
## download option of wget
pushd wpdumps
wget -c https://dumps.wikimedia.org/eswiki/latest/eswiki-latest-pages-articles.xml.bz2
wget -c https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
popd
