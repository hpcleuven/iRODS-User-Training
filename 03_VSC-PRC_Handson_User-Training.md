# Introduction to Python iRODS Client (PRC) and VSC-PRC tools

*Prerequisites:*  
*-A vsc-account and acces to the Tier-1 infrastructure of KU Leuven*  
*-Basic knowledge of command line (Bash)*   
*-Basic knowledge of Python is useful*    

This training introduces you to the basics of using the iRODS client API implemented in Python, as well as the additional functions and tools developed by VSC to extend the iRODS Python API functionalities. The main feature of the VSC extensions is the possibility of using wildcards ("\*") and tildes ("~") for specifying iRODS data objects and collections. 

## Goal of this training
You will learn how to use the Python iRODS API (PRC) to interact with the Tier-1 Data service iRODS infrastructure.
The following functionalities will be covered:

- Uploading and downloading data
- Uploading and downloading data collections
- Adding and editing metadata
- Setting access permissions for data objects and collections
- Querying for data using user defined metadata
- Using the VSC-PRC command line tools


## Using the VSC-PRC interactively 

This training is intended to be executed on the VSC Tier-1 (BrENIAC) system. We assume you already have a vsc-account and rights to connect to the Tier-1 Compute system and to use the Tier-1 Data service.

### Environment setup

- Connect to BrENIAC with your vsc-account using your favourite client. 
- Go to your data folder:
```sh
cd $VSC_DATA
```
  It is good practice to store files not in your home folder, but in your data folder, since a filled-up home folder can cause login issues.
  The home directory is mainly meant for configuration files.
  
- Copy the course material in your data directory


```sh
git clone https://github.com/hpcleuven/iRODS-User-Training.git
``` 
- The  Python iRODS API (PRC) and the VSC extensions are available as a module in the Tier-1 Compute system.
Before using it you will need to load the corresponding module:

```sh
module load Python/3.7.4-GCCcore-8.3.0
module load vsc-python-irodsclient/0.1-python-irodsclient-0.8.4
``` 

Note that vsc-python-irodsclient/0.1-python-irodsclient-0.8.4 will load a python module if there is none already loaded.
In order to have full control about which Python version is used it is recommended to prior to load the vsc-prc-python module 
to load the Python version you want to work with.

In addition before using the Python client it is needed to start an iRODS session by executing the command:

From Tier-1 login nodes or compute nodes:

```sh
ssh irods.hpc.kuleuven.be | bash
``` 

From Tier-2 login nodes: 

```sh
ssh irods.tier1.leuven.vsc | bash
``` 

These command will activate a temporary token for a period of 7 days. After the 7 days have passed you will need to reactivate 
your access by re-executing one of these commands again.

###  Working with collections and data objects

We will first start using iRODS interactively with ipython.  
That way, we can execute commands line by line, which is great for experimenting. 
So we will need to install locally ipython:

```sh
pip install --user ipython
``` 
and the corresponding directory to your path:


```sh
export PATH=$HOME/.local/bin/:$PATH
``` 


Start an ipython session:

```sh
ipython
``` 

The first thing we need to do is to import the VSCIRODSSession module and create an iRODS session.
This class is derived from PRC's irods.iRODSSession class, and as such you can still use it to do what PRC is capable of (see https://github.com/irods/python-irodsclient). Here, we will focus on the functionalities that are added by VSC-PRC.  

```py
from vsc_irods.session import VSCiRODSSession
session = VSCiRODSSession(txt='-')
```
In addition to the keyword arguments for irods.iRODSSession, it also accepts a txt argument. This specifies where the session's print output should be directed to, with the default '-' referring to stdout.

Note that when using the VSCiRODSSession class is best practice to initiate it using the with construct to 
ensure that the session is cleanly terminated, even if an error occurs:

```py
from vsc_irods.session import VSCiRODSSession
with VSCiRODSSession(txt="-") as session:
    
    [your code here]
```

The VSC-PRC library provides a number of functions grouped by functionality:

- path functions: functions related to navigation and path information 
  - get_irods_home
  - get_irods_cwd
  - get_absolute_irods_path
  - ichdir
  - imkdir 

- bulk functions: functions to perform actions on multiple collections or dataobjects in once by using wildcards ("\*") and tildes ("~") for specifying iRODS data objects and collections. 
  - get
  - put
  - remove
  - metadata
  - size 
  - add_job_metadata

- search functions: advance search capabilities either by filename or by metadata entries in the format Attribute, Value:
  - iglob
  - walk
  - find 

Let's try some of those functions:

Printing the iRODS home directory and the current working directory:

```py
session.path.get_irods_home()
session.path.get_irods_cwd()
```

Create a collection `training` on your iRODS home directory:

```py
session.path.imkdir('training')
```
We can verify that the collection has been created by requesting the absolute path (the full path from the root):

```py
session.path.get_absolute_irods_path('training')
```
Now we can change to the directory we just created:


```py
session.path.ichdir('training')
```

We can now check the current working directory, which is different from the home directory:

```py
session.path.get_irods_cwd()
session.path.get_irods_home()
```

Let's upload some data into our training iRODS collection!

First let's use the iRODS Python Client to upload a single dataobject from the molecules folder, alcl3.xyz, to iRODS.
You will need to fill in the correct path to the file you want to upload:

```py
session.data_objects.put( [location of the file]  , [target destination of the file])
```
For example, if user vsc33731 wants to upload this to his training folder, it might look like this:

```py
session.data_objects.put('/data/leuven/337/vsc33731/iRODS-User-Training/molecules/alcl3.xyz','/kuleuven_tier1_pilot/home/vsc33731/training/')
```

This demonstrates that even using the VSCIRODSSession class all the functionalities of the Python iRODS Client (PRC) are still available. 

Let's use the search.find() function to verify that the file has been uploaded to iRODS:

```py
irods_path = '/kuleuven_tier1_pilot/home/vsc33731/training/'
session.search.find(irods_path,types='f')
```
This command returns a list of iRODS data objects paths (types='f' means list files) which match a given pattern. As we have not defined a pattern then the default value ("\*") is used. So, the result will be a list containing the iRODS paths of all the files in the collection `irods_path`.  

We can loop over the list to print the search results:

```py
for item in session.search.find(irods_path, types='f'):
	print(item)
```

While this PRC function works well, it has the disadvantage that only works with single data object or collections.
Here the VSC-PRC bulk functionalities provide more flexibility, as they allow to select files using wildcards. 

So, let's now upload to the training iRODS collection all files with extension .xyz:

```py
session.bulk.put('./molecules/*.xyz', irods_path)
```
We can execute again the same find command we used before to verify that indeed all files with extension .xyz have been uploaded. 

```py
for item in session.search.find(irods_path, types='f'):
	print(item)
```
Let's now create a subdirectory `results` on our molecules collection and see how we can both list all 
subcollections and files of a given collection with the find function. As 'f' stands for files, 'd' stands for directories or collections.

```py
session.path.imkdir('results')
for item in session.search.find(irods_path, types='d,f'):
        print(item)
```


###  Adding metadata to files 

Until now we have seen how to use the search.find function to search for collections and data objects 
based on their paths and filenames. But iRODS also offers the possibility to add metadata to them 
in the form of tuples or triples (Attribute-Value-[Unit]), also called AVUs. 

Let's start adding metadata to our `training` collection to identify it with the associated research project.
We will add a tuple Attribute-Value (Project, Training) and we will apply this metadata to the training collection
and all its subcollections and data objects by using the recursive option. As we have also selected the verbose 
option, we will see to which collections and dataobjects the metadata is added: 

```py
avu1= ('Project', 'Training')
session.bulk.metadata(irods_path, collection_avu=avu1, action='add', recurse=True, verbose=True)
session.bulk.metadata(irods_path + '/*' , object_avu=avu1, action='add', recurse=True, verbose=True)
```

We will now create two other AVUs pairs to add to the xyz files the experiment information.
The molecules (c6h6.xyz, ch2och2.xyz and ch3cooh.xyz) where used in experiment1 while the file sih4.xyz in experiment2.
The rest of the molecules has not yet being used in any experiment. 

```py
avu2 = ('Experiment', 'Experiment1')
avu3 = ('Experiment', 'Experiment2')
session.bulk.metadata(irods_path + '/c*.xyz' , object_avu=avu2, action='add', recurse=True, verbose=True)
session.bulk.metadata(irods_path + '/sih4.xyz' , object_avu=avu3, action='add', recurse=True, verbose=True)
```

Now we can use this metadata information to perform searches on the iRODS collections and to download all the selected files to our local directory.
Let's download all the files that were used in Experiment1 using the bulk.get function: 


```py
iterator = session.search.find(irods_path, object_avu=avu2)
session.bulk.get(iterator, local_path='.', verbose=True)
```

To finish let's clean up by removing all the `training` collection. 
We will use the option recurse=True to remove the collection and all its subcollections 
and dataobjects and the option force=True to completely remove the files (iRODS by default move it to a Trash area). 

```py
session.bulk.remove(irods_path, recurse=True, force=True, verbose=True)
```

### Sharing data

You can give people access to your data as follows: 

```py
from irods.access import iRODSAccess
acl = iRODSAccess(<access_type>, <collection/dataobject_path>, <username>) 
session.permissions.set(acl)
```

- 'access_type' can be any of the following:
    - 'read'
    - 'write'
    - 'own'

- 'username' can either be the name of a user or the name of a group.

If you are applying the permissions to a collection, you can add the 'recursive' parameter to extend the access to any data objects and subcollections:  
`session.permissions.set(acl, recursive=True)`

You can remove permissions again with `session.permissions.remove(<acl>)`.  
Note that these methods were not added by the VSC-PRC extension, so they cannot handle wildcards and tildes.  
Instead, they need the full path of the collection or data object. 


##  Exercises 

Let's do the exercises below! 


Before starting the exercises, please clone the [git repository](https://github.com/hpcleuven/iRODS-User-Training) of this training if you haven't done so yet.  
You will find files for the exercises in the 'data' directory.

### Exercise 1: uploading data

Make a python script that does the following: 

- Make a directory called 'experiment1' in your home collection.  
- Go to the experiment1 collection.    
- Upload all files from the 'molecules' folder to the collection 'experiment1'
- Give your group 'read access to the collection 'experiment1'
- Add the AVU 'kind: organic' to any molecule starting with a 'c'.
- Make a local directory called 'organic_molecules' (you can use a bash command here)
- Download all data objects starting with 'c' to this new directory.



<details>   
  <summary>Solution</summary>

```
import os
from vsc_irods.session import VSCiRODSSession
from irods.access import iRODSAccess

with VSCiRODSSession(txt='-') as session:

    session.path.imkdir('experiment1')

    session.path.ichdir('experiment1')

    session.bulk.put('data/molecules/*')

    irods_path = session.path.get_irods_cwd()
    acl = iRODSAccess('read', irods_path, 'datateam')
    session.permissions.set(acl, recursive = True)

    avu = ('kind', 'organic')
    session.bulk.metadata(irods_path + '/c*.xyz' , object_avu=avu, action='add')

    os.mkdir('organic_molecules')

    session.bulk.get('/c*.xyz', 'organic_molecules', recursive=True)
```

</details>



### Exercise 2: Using the command line tools

The VSC-PRC also comes with a set of scripts which make it easy to use the
Python module from a Unix shell:

- vsc-prc-find - Search data objects in iRODS  
- vsc-prc-iget - Download data objects  
- vsc-prc-iput - Upload data objects  
- vsc-prc-imkdir - Create collections  
- vsc-prc-irm - Remove data objects/collections
- vsc-prc-imeta - Manage metadata
- vsc-prc-add-job-metadata - Manage job metadata
- vsc-prc-size - Show the size of a data object/collection

Type any of these commands followed by '--help' to get more info (e.g. `vsc-prc-find --help`).   
Just like the module we discussed here, these tools make it easy to work with wildcards ("*") and tildes ("~").

Let's try roughly the same as above, but now using the VSC-PRC command line tools: 

- Make a directory called 'experiment2' in your home collection.  
- Upload all files from the 'molecules' folder to the collection 'experiment2'
- Add the AVU 'kind: organic' to any molecule starting with a 'c'.
- List all the files with the metadata 'kind: organic' to see if this worked.
- Make a local directory called 'organic_molecules' (you can use a bash command here)
- Download all data objects starting with 'c' to this new directory.

<details>   
  <summary>Solution</summary>

  - `vsc-prc-imkdir experiment1` or `vsc-prc-imkdir ~/experiment2`    
  - `vsc-prc-iput data/molecules/* --destination experiment2`  
  - `vsc-prc-imeta "~/experiment2/c*" --object_avu=kind,organic --action=add`  
  - `vsc-prc-find "~/experiment2" --object_avu='=,kind;=,organic'`  
  - `mkdir organic_molecules`  
  - `vsc-prc-iget experiment2/c*`
</details>
