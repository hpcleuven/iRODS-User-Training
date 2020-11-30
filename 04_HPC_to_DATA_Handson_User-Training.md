# DATA to HPC: integrate iRODS in batch job scripts

*Prerequisites:*  
*-A vsc-account and acces to the Tier-1 of Tier-2 infrastructure of KU Leuven*  
*-Permission to submit jobs on the Tier-1 or Tier-2 system*  
*-Knowledge on how to use the HPC infrastructure*  
*-Basic knowledge of command line (Bash) and shell scripting*  


This training explain how to integrate the VSC-PRC command line tools with 
job batch scripts to be able to stagein/stageout data from/to iRODS to the HPC scratch directory. 

# Upload the data to irods 

Create a training collection and upload all the molecules directory

```sh 
vsc-prc-imkdir('training')
vsc-prc-put "molecules" --destination="~/training"
```


# Create a job script that does the following:

- Download the the xyz files on the training/molecules irods collection to a directory in $VSC_SCRATCH
- Does some calculation using the xyz files 
- Create a results directory in the training iRODS collection
- Upload the result file to iRODS
- add job metadata to the results file
- Add some additional user metadata to the results file. 


In the directory jobsscripts you can find a template file (exercise1.pbs) 
that you can use as reference to create your script


