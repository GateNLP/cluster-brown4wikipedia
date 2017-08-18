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
