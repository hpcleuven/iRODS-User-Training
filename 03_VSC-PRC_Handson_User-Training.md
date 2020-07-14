# VSC-PRC
VSC-PRC is a complementary module created for supporting the Python iRODS Client (PRC) operations on VSC.

## Installation
VSC-PRC and its dependencies are available as a module.

```sh
iinmodule use /apps/leuven/common/modules/all
module load vsc-python-irodsclient/developmentit
``` 

## General Overview

VSC-PRC's main goal is to make it easier for researchers to manage their data using iRODS, in particular on VSC's high performance computing infrastructure.

To this end, VSC-PRC offers a Python module and associated command line scripts:

The vsc_irods Python module contains a VSCiRODSSession class which represents an extension of the corresponding iRODSSession class in PRC.

A main feature is the possibility of using wildcards ("*") and tildes ("~") for specifying iRODS data objects and collections. For example, the following code will copy all files ending on '.txt' inside a 'my_irods_collection' collection in your irods_home to the local working directory:

