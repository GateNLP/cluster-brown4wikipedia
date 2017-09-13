# Scripts for creating brown clusters from Wikipedia dumps

## Run the following scripts and steps in sequence

* `setup.sh` - to initialize and compile the submodules
* download the dump files so that they are stored or linked in the 
  wpdumps directory. The `download-wp.sh` script can be used as an example.
* extract the wikipedia dump into a single text file using
  `./extract.sh wpdumps/DUMPFILE.xml.bz2`
  This creates a file in the root directory with the same basename as the DUMPFILE but 
  extension  ".txt", DUMPFILE.txt 
* Create Brown mergers from the file:
  `./generalised-brown/merge_generator/wcluster --a 1000 --comment "created from DUMPFILE" --text DUMPFILE.txt`
* Create the actual clusters (number of clusters is 100 in this example): 
  `python3 ./generalised-brown/cluster_generator/cluster.py -in DUMPFILE-c1000-p1.out/merges -c 100`

## Experiments with running on bg, cs, de, en

Downloaded latest dump files as of 2017-08-18

Statistics for dump files (nr.docs is the last count shown by the INFO line
of the extraction script, nr.tokens is the number of words on the output 
returned by `wc -w`), extract is the time needed to extract the dump on derwent:

| language | size(M) | nr.docs | extracted |  nr. tokens | extract |
-----------------------------------------------------------------
| bg     | 00278 | 00666258 | 0232582 | 0049010508 | 0:04:59 | 
| cs     | 00623 | 01314984 | 0386612 | 0094447512 | 0:10:07 |
| de     | 04300 | 09995327 | 2086671 | 0668221382 | 1:16:06 | 
| en     | 14000 | 54723812 | 5328951 | 1903609328 | 2:07:01 |


On a sharc worker node, with both source and target on /scratch, the
time to extract bg was 15:40 so almost 4 times as slow!


Elapsed time for creating the merges (24 threads on derwent)
(command `time ./generalised-brown/merge_generator/wcluster --threads 24 --a 1000 --text XXwiki-latest-pages-articles.txt`) 

| language | time | server | threads | notes | 
--------------------------------------------------
| bg | 14:31:43 | derwent | 24 |  | 
| cs | 29:37:18 | derwent | 24 |  | 
| de | | derwent | 24 | | 
| en | 143:41:33 | gateservice8 | 30 | niced | 

