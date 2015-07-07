# sparsModGECCO2015
Materials for reproducing results from the paper "Exploiting the relationship between structural modularity and sparsity for faster network evolution" by Anton Bernatskiy and Josh Bongard.

1. This code was developed and tested for GNU/Linux and is unlikely to work anywhere else without modification.
2. Current version assumes that all folders of the repository are located at $HOME.
3. Python2 is the main language of the codebase. The interpreter binary is expected at ${HOME}/anaconda/bin/python2.7. To install the Anaconda Python environment, visit http://continuum.io/download. If you wish to use the code without installing Anaconda, run the following commands:

 ```  
 $ cd ~  
 $ mkdir -p anaconda/bin  
 $ ln -s /usr/bin/python2 ${HOME}/anaconda/bin/python2.7  
 ```  

4. Whichever Python2 is used, it must have NumPy installed.
5. The code depends on the binaries of the [findcommunities](https://sites.google.com/site/findcommunities/) modularity optimizer. Download the "updated" version of the source code and compile it:

```
$ cd ~/findcommunities/
$ wget https://sites.google.com/site/findcommunities/newversion/community.tgz
$ tar -xf community.tgz
$ cd Community_latest
$ make
```

On some systems compilation fails with a "‘getpid’ was not declared in this scope" error. It can be fixed by adding the "#include <unistd.h>" line to the include section of main_community.cpp.

When done with the compilation, create named pipes for the wrapper:

```
$ cd ~/findcommunities/
$ ./makePipes.sh
```

6. Root executables of the project are at ~/evscripts/experiment*.py. They accept two arguments: run ID as the first and config file name as a second. Run ID is an integer from 0..199 which determines the random seed is to be used in the current run (random seed values are stored at ~/evscripts/randints1421128240.dat). All provided configs are named config.ini.

7. To run an experiment, go to the corresonding directory at ~/experimentalData and run the corresponding binary, e.g.

```
$ cd ~/experimentalData/experiment1taskA
$ ~/anaconda/bin/python2.7 ~/evscripts/experiment1taskA.py 10 config.ini
```

The script outputs the number of the current generation and a newline at each generation change. It should begin printing these number shortly after the execution.

Note that, unlike the other folders, the directory experimentalData doesn't have to be located at $HOME. The amount of the generated data is substantial (several gigabytes for all experiments), so feel free to move the folder to any location where the storage space is not an issue.

8. The scripts operate by exploring each subfolder of ~/experimentalData/experiment* folders, locating config.ini files in them and executing the corresponding simulations. For each simulation, the output is stored at bestIndividual*.log and bestIndividual*.log.q files at the corresponding subfolder. The suffix in the name of the file shows the random seed value which was used in the simulation.

In other words, each execution of the root script runs as many evolutionary simulations as there are subfolders at ~/experimentalData/experiment*, each with the same random seed (determined by run ID).

bestIndividual*.log files contain raw data from the evolutionary simulation: genomes of champions of each generation and their fitness. bestIndividual*.log.q contain the modularity (Q) values for the champions of each generation. The data is stored in text format.

9. The raw data files can be processed by going to an ~/experimentalData/experiment* folder and executing ~/evscripts/processDir.sh, e.g.

```
$ cd ~/experimentalData/experiment1taskA
$ ~/evscripts/processDir.sh
```

For each subfolder of ~/experimentalData/experiment1taskA this will create three files: <subfolderName>.fitness, <subfolderName>.qvalue and <subfolderName>.density. In these files, each line corresponds to a generation and contains all values of the corresponding parameters of the champions across the runs (random seed values).

10. The plots can be produced with Python scripts located at ~/figures/*/*.py. The scripts require Matplotlib to be installed. To use them, go the the script's folder, copy the processed data files there and run the script (may require tweaking of the plotting scripts to work).

11. Cluster scripts for batch-running the simulations using [PBS](https://en.wikipedia.org/wiki/Portable_Batch_System) are provided at ~/evscripts/experiment*.sh. Be sure to adjust the walltime parameter appropriately.

All questions should be directed to abernats@uvm.edu.
