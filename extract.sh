#/bin/bash

infile="$1"
if [ "x$infile" == "x" ]
then
  echo need one or two parameters the path to the wiki dump file and the output file
  exit 1
fi
name=`basename $infile .xml.bz2`
outfile="$2"
if [ "x$outfile" == "x" ]
then
  outfile=${name}.txt
fi

echo saving output to file $outfile
## TODO: add a script to clean other HTML we do not want
python3 ./wikiextractor/WikiExtractor.py --no-templates -o - --min_text_length 100 --filter_disambig_pages $infile | \
  grep -v  -E '<doc' | grep -v -E '</doc' | \
  sed -e "s/<br>/\n/g" | 
  cat > ${name}.txt
echo file $outfile created
