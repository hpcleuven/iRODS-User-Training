# DATA to HPC: integrate iRODS in batch job scripts

*Prerequisites:*  
*-A vsc-account and acces to the Tier-1 of Tier-2 infrastructure of KU Leuven*  
*-Permission to submit jobs on the Tier-1 or Tier-2 system*  
*-Knowledge on how to use the HPC infrastructure*  
*-Basic knowledge of command line (Bash) and shell scripting*  


This training explains how to integrate the VSC-PRC and its command line tools with 
job batch scripts to be able to stagein/stageout data from/to iRODS to the HPC scratch directory.

The first exercise will be about how you can use the VSC-PRC command line tools in a batch script. The second exercise is how to use the Python iRODS client with a batch file.

In the directory jobsscripts, you can find template files which you can use as reference to create your script.

# Upload the data to irods 

Create a training collection and upload all the molecules directory

```sh 
vsc-prc-imkdir training
vsc-prc-iput molecules --destination="~/training"
```


## Exercise-1: Create a job script that does the following:

- Download the the xyz files on the training/molecules irods collection to a directory in $VSC_SCRATCH
- Do some calculation using the xyz files 
- Create a results directory in the training iRODS collection
- Upload the result file to iRODS
- Add job metadata to the results file
- Add some additional user metadata to the results file.
- You can use exercise_template.pbs as reference


## Exercise-2: Create a job script running python code that will do the following:

- Download all the files from irods collection molecules to the your script directory(workingdir)
- Do some calculation using the xyz files (look at the templates in jobscripts)
- Create a result directory in the irods training collection
- Upload the output file to iRODS
- Add some metadata to the output file
- You can use exercise2_example_py.pbs and calculate_template.py as reference