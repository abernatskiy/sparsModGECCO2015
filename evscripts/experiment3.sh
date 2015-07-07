#PBS -l nodes=1:ppn=1
#PBS -l walltime=02:50:00
#PBS -N myjob
#PBS -j oe
#PBS -m bea

cd $PBS_O_WORKDIR
echo "This is myjob running on " `hostname`
${HOME}/anaconda/bin/python2.7 ${HOME}/evscripts/experiment3.py $PBS_ARRAYID config.ini
