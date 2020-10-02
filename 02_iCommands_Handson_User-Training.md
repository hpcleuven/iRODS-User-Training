# iCommands for VSC Users

*Prerequisites:*  
*-A VSC account (or your own iRODS environment)*  
*-Basic knowledge of command line (Bash)*  

This training introduces you to the basics of what iCommands are and how we do simple data management as a user with iCommands.
To this end we will make show of the icommands which is an Unix utilities that give users a command-line interface to iRODS.

## Categorizing iCommands
As a command line user interface to iRODS, more than 50 iCommands exist. However a regular user may use only a few of them for his/her daily needs. Therefore, if we categorize them in different groups, we can easily grab how they work.
- Informative iCommands
- Unix like iCommands
- Functional iCommands
- Metadata Related iCommands
- Rule Based iCommands
- Administrative iCommands

## Goal of the Training
The aim of the training is to explain the following topics by using the command line tool-iCommands:
- uploading/downloading data
- adding metadata to data objects/collections
- querying based on metadata
- deleting data objects/collections
- synchronization of data
- ACLs to data objects/collections

### Login in to VSC
In this course we will use the Tier-1 login node as our user interface. But you can also use Tier-2 login. Therefore you are supposed to reach to either Tier-1 or Tier-2 login node.
In the future we will also be able to use compute nodes.

### Connecting to iRODS
After you have reached the Tier-1 to work on, to be able to interact with iRODS, as a VSC user you will need to activate the service by executing the following commands:

```sh
ssh irods.hpc.kuleuven.be | bash
```

If you are connecting from Tier-2 login node, you should then execute:

```sh
ssh irods.tier1.leuven.vsc | bash
```

### Informative iCommands
These commands help us find and understand some useful information. We may not need these commands directly when we work with data, however we use them to discover what we need.

The command that will print out all commands with their explanation is:

```sh
ihelp
```

To get help on a specific commands:
`ihelp iuserinfo` or `iuserinfo -h`

If you would like to know the setting details you can execute the following command.

```sh
ienv
```

To know about the details of an user you can run the below command following with an user account.
This command will show for example to which groups a user belongs:

```sh
iuserinfo vscXXXXX
```

To be able to learn what an error code stands for, you can then use the command below with a code number:

```sh
ierror 826000
```

To connect to the server and retrieve some basic server information (use as a simple test for connecting to the server):

```sh
imiscsvrinfo
```

Typically we don’t use these commands very often.

### Unix like iCommands (Basics)
These commands exactly work as what Unix based commands do.

To identify the current working collection (directory) you can use the `ipwd` command. Basically this command tells you where you are in iRODS:

```sh
ipwd
/kuleuven_tier1_pilot/home/public
```

Let’s create a collection in iRODS and name it “test”.

```sh
imkdir test
```

To see the content of our current collection(directory), we can use `ils`. It lists Collections (directories) and Data Objects (files).
And we see that we have successfully created our “test” collection.

```sh
ils
/kuleuven_tier1_pilot/home/public:
  C- /kuleuven_tier1_pilot/home/public/test
```

To go to the collection that you want, you would use `icd` with an absolute path or a relative path.
In other saying, to navigate around folder(s) of iRODS, we use it. Let's go inside the 'test' collection:

```sh
icd test
```

To copy a data-object (file) or collection (directory) to another data-object or collection, we use `icp`.
For example, if we want to copy “test” collection that we created to the same directory with a different name “test1”:

```sh
icp –r test test1
```

To move/rename an irods data-object (file) or collection (directory) to another, data-object or collection, we use `imv`.
Let’s move collection “test1” inside the collection “test”.

```sh
imv test1 test/
```

To remove one or more data-object or collection from iRODS space, we use `irm`. By default, the data-objects are moved to the trash collection (/kuleuven_tier1_pilot/trash) unless the -f option is used.
The –r option is used for collections. Now we can remove test1 collection.

```sh
irm -r test1
```

**Note**: The irmtrash command should be used to delete data-objects in the trash collection.

**Exercise 1:**

- Create two different collections in iRODS and move around using basic unix like iCommands (ipwd, ils, icd, imkdir, imv and irm).
- At the end delete one of the collection permanently and remove the other one from your iRODS home.

### Functional iCommands
With the commands in this section, we will do functional data operations like data uploading/downloading, access control and verifying/synchronizing data.
This constitutes the basis of data management in iRODS.

#### Data Upload
We can store a file into iRODS.  If the destination data-object or collection are not provided, the current iRODS directory and the input file name are used.

To upload data into iRODS we should have a data object in our VSC system. Thus we should first create a data file in our Linux home-directory. 

```sh
nano example.txt
Hi, this is an example file!
```

With the linux command `ls` we can check that the file has been created.

We now upload the data to the iRODS.

```sh
iput –K example.txt
```

*The flag -K triggers iRODS to create a checksum and store this checksum in the iCAT metadata catalogue.*

Let’s remove the original file.

```sh
rm example.txt
ls
```

The file is now only available on the iRODS server not in our VSC home directory.

```sh
ils

/kuleuven_tier1_pilot/home/public:
  example.txt
  C- /kuleuven_tier1_pilot/home/public/test
```

**Exercise 2:**

- Upload the ThePlanetWeLiveOn.pdf book (you can get it from the following link with `wget http://www.learndev.org/dl/Science/EarthScience/ThePlanetWeLiveOn.pdf`) to your home directory in iRODS.
- Create a new collection science_book  within your home directory
- Move ThePlanetWeLiveOn.pdf into this new collection.

As we have seen before, data can be deleted by `irm (-f) example.txt`. But we will not do it now.

#### Connection between logical and physical namespace
iRODS provides an abstraction from the physical location of the files. ` /kuleuven_tier1_pilot/home/public/example.txt` is the logical path which only iRODS knows.
But where is the file actually located on the server?

```sh
ils -L

/kuleuven_tier1_pilot/home/public:
  vsc33586          0 default;tier1-p-irods-2020-pilot;tier1-p-irods-2020-pilot-replication;tier1-p-irods-posix;tier1-p-irods-posix-1-4;tier1-p-irods-posix-3-a-4-a;tier1-p-irods-posix-3-a-weight;tier1-p-irods-posix-3-a           24 2020-07-13.09:23 & example.txt
    sha2:cQWOwjd7n0JM25XzWdaZPh9RQUvpQWa81Slilj/R0YA=    generic    /irods/a/home/public/example.txt
  vsc33586          1 default;tier1-p-irods-2020-pilot;tier1-p-irods-2020-pilot-replication;tier1-p-irods-posix;tier1-p-irods-posix-1-4;tier1-p-irods-posix-3-a-4-a;tier1-p-irods-posix-4-a-weight;tier1-p-irods-posix-4-a           24 2020-07-13.09:23 & example.txt
    sha2:cQWOwjd7n0JM25XzWdaZPh9RQUvpQWa81Slilj/R0YA=    generic    /irods/a/home/public/example.txt
```

Let’s try to understand what does this mean. The example.txt that we uploaded to iRODS seems at the logical path `/kuleuven_tier1_pilot/home/public/example.txt`. vsc33586 is the owner of the file and the numbers after user name show the replica of files in the iRODS system.
“default” represent storage resource name. The size of the file is 24KB. The file is stored with a time stamp and a checksum. `/irods/a/home/public/example.txt` is the physical path of the file.

#### Data Download
We can get data-objects or collections from iRODS space, either to the specified local area or to the current working directory. Simply lets download data files from iRODS to our current VSC location.

To download or to restore the file (copy it from iRODS to your VSC home):

```sh
iget –K example.txt example-restore.txt
```

We download the iRODS file example.txt as a new file called example-restore.txt in our linux home directory. Here the flag -K triggers iRODS to verify the checksum. Checksums are used to verify data integrity upon data moving.

*To get the progress feedback, we can use –P flag.*

**Note**: The iput and iget commands also work for directories/collections, simply use the -r (for recursive) flag.

**Exercise 3:**

- download the data object ThePlanetWeLiveOn.pdf as downloaded_ThePlanetWeLiveOn.pdf
- download the collection science_book

#### Access control and data sharing
Collections in the iRODS logical name space have an attribute named Inheritance. `ichmod` can be used to manipulate this attribute on a per-Collection level.
ils -A displays ACLs and the inheritance status of the current working iRODS directory. iRODS has ACL with read, write and own rights.

You can check the current access of your data with:

```sh
ils –r –A

/kuleuven_tier1_pilot/home/public:
        ACL - g:public#kuleuven_tier1_pilot:own
        Inheritance - Disabled
  example.txt
        ACL - vsc33586#kuleuven_tier1_pilot:own
  C- /kuleuven_tier1_pilot/home/public/mymessage
/kuleuven_tier1_pilot/home/public/mymessage:
        ACL - vsc33586#kuleuven_tier1_pilot:own
        Inheritance - Disabled
  message.txt
        ACL - vsc33586#kuleuven_tier1_pilot:own
  C- /kuleuven_tier1_pilot/home/public/test
/kuleuven_tier1_pilot/home/public/test:
        ACL - vsc33586#kuleuven_tier1_pilot:own
        Inheritance - Disabled
```

After 'ACL' it shows which user has what rights, e.g. <vsc33586> owns all files listed. No one else has access rights.

Collections have a flag 'Inheritance'. If this flag is set to true, all content of the folder will inherit the accession rights from the folder.

Let us change the accession rights of 'mymessage'. You can choose another user who you want to give access:

```sh
ichmod read vsc30706 mymessage
```

The user vsc30706 now can list the collection and see the data to which he/she has the respective permission.

We can change the inheritance and place some new data in the collection:

```sh
ichmod inherit mymessage
iput -K example-restore.txt mymessage/example1.txt
```

Only the recently added file will inherit the ACLs from the folder. Old data will keep their ACLs.

```sh
ils -A -r mymessage
```

#### Checking data integrity
For confirming data integrity, the checksum of a data object or a collection can be checked both in our VSC systems (Tier-1 nodes) and iRODS.

We can confirm the checksum of one or more data-object or collection from iRODS. Let’s first check the checksum of mymessage collection in iRODS.

```sh
ichksum –r mymessage

C- /kuleuven_tier1_pilot/home/public/mymessage:
    example1.txt    sha2:cQWOwjd7n0JM25XzWdaZPh9RQUvpQWa81Slilj/R0YA=
    message.txt    sha2:I+hXKW8cY3IZ1KZUJlFE8yPRltdSstwnONohiUr3UTo=
```

As you remember we can check same by `ils -L` command. But this command list all other information.

We can reproduce the same digits with `sha256sum ${FILENAME} | awk '{print $1}' | xxd -r -p | base64`.

Now we check the checksum of the message.txt file in our local system.

```sh
sha256sum message.txt | awk '{print $1}' | xxd -r -p | base64

I+hXKW8cY3IZ1KZUJlFE8yPRltdSstwnONohiUr3UTo=
```

So we can confirm that this data object/file is the same and we don’t detect any error during its transmission or storage.

**Exercise 5:**

Confirm the data integrity of example1.txt data object.

#### Data Synchronization
To synchronize the data between a local copy (local file system) and the copy stored in iRODS or between two iRODS copies, we can use ` irsync`. The command and its mode can be determined by the way the sourceFile|sourceDirectory and targetFile|targetDirectory are specified.

Files and directories prepended with 'i:' are iRODS files and collections. Local files and directories are specified without any prefix.

For example, the command:

```sh
irsync -r foo1 i:foo2
```

synchronizes recursively the data from the local directory foo1 to the iRODS collection foo2 and the command:

```sh
 irsync -r i:foo1 foo2
 ```

synchronizes recursively the data from the iRODS collection foo1 to the local directory foo2.

```sh
 irsync -r i:foo1 i:foo2
 ```

synchronizes recursively the data from the iRODS collection foo1 to another iRODS collection foo2.

How does this command work? The command compares the checksum values and file sizes of the source and target files to determine whether synchronization is needed. 

**Exercise 6:**

- Download mymessage collection to your VSC system (`iget -r mymessage`).
- Add test1.txt file inside this directory.
- Synchronize this change with your iRODS destination.
- See the update in iRODS collection.

#### File Bundling
To upload and download structured files such as tar files to/from iRODS, we can use `ibun` command.

A tar file containing many small files can be created with normal unix tar command on our local machine . We can then upload the tar file to the iRODS server as a normal iRODS file. Furthermore, `ibun –x` command can be used to extract/untar the uploaded tar file. The extracted subfiles and subdirectories will then be appeared as normal iRODS files and sub-collections.

As a good practice we can tag the tar file using the -Dtar flag when uploading the file with iput. The dataType tag can be added later with the isysmeta command. For example:
isysmeta mod /kuleuven_tier1_pilot/home/vsc33586/mydir.tar datatype 'tar file'

```sh
  tar -chlf test.tar –C myCollection my file
  iput -Dtar test.tar
  ibun -x test.tar test_collection
```

We can also add/bundle an iRODS collection into a tar file by using `ibun -c` command.

```sh
  ibun -cDtar test.tar myCollection1
```

**Exercise 7:**

- Create a “test.tar” file composed of folder and files in your VSC. Or get a compressed file with corresponding extensions.
- Upload this file to iRODS with using tag (-Dtar flag) as a good practice.
- Extract this tar file in “test” collection that you don’t have before.
- Bundle an iRODS collection into a tar file.
- Upload another tar file to iRODS without using tag.
- Check its data type and if it doesn’t have a proper one, modify it with ‘tar file’.


### Metadata
Metadata is often called data about data and is used to facilitate data discovery to improve search and retrieval. iRODS provides the user with the possibility to create Attribute Value Unit triples and store them with the data. The triples are stored in the iCAT catalogue.

Metadata attribute-value-units triples (AVUs) consist of an Attribute-Name, Attribute-Value, and an optional Attribute-Units.  They can be added via the 'add' command (and in other ways), and then queried to find matching objects.

For each command, -d, -C, -R, or -u is used to specify which type of object to work with: dataobjs (iRODS files), collections, resources, or users.

These triples are added to a database and are searchable so that we will explore how to create these AVUs triples for which we can search later.

#### Create AVUs triples

-	Annotate a data file:

```sh
imeta add -d example.txt 'distance' '10' 'meter'
imeta add -d example.txt 'author' 'Tom'
```

We can leave ‘Unit' part is here empty because it is optional.

-	Annotate a collection:

```sh
imeta add -C mymessage 'training' 'irods' 'online'
```

#### List Metadata

To list metadata we do:

```sh
imeta ls -d example.txt
```

and for a collection:

```sh
imeta ls -C mymessage
```

With `imeta ls`, we can retrieve the AVUs when given a file or collection name. In the next part we will see how we can retrieve the file and folder names when given an attribute or value.

#### Queries for data
Previously we calculated a checksum. The checksum was stored in the iCAT metadata catalogue but we cannot fish it out with imeta. To query the iCAT metadata catalogue we need another command, the iquest command.

Whereas we can use `imeta qu` for a simple queries, we should use `iquest` command for sql-like sophisticated search. Previously calculated a checksum can be searched by `iquest` since the checksum was stored in the iCAT metadata catalogue.

For a simple query:

```sh
imeta qu -d distance = 10
```

For an extended queries:

Let’s fetch the data file, given e.g. the attribute 'author'.

```sh
iquest "select COLL_NAME, DATA_NAME, META_DATA_ATTR_VALUE where \
META_DATA_ATTR_NAME like 'author'"
```

We can filter for a specific attribute values:

```sh
iquest "select COLL_NAME, DATA_NAME where \
META_DATA_ATTR_NAME like 'author' and META_DATA_ATTR_VALUE like 'Tom'"
```

Or we can retrieve all data with a certain checksum:

```sh
iquest "select COLL_NAME, DATA_NAME, DATA_CHECKSUM where \
DATA_CHECKSUM like 'sha2:I+hXKW8cY3IZ1KZUJlFE8yPRltdSstwnONohiUr3UTo='"
```

To bring all files with substring 'test' in file name:

```sh
iquest "select COLL_NAME, DATA_NAME, DATA_CHECKSUM where DATA_NAME like '%test%'"
```

**Note**: the '%' and '_' are wildcards.

To see predefined attributes that we can use in our searches:

```sh
iquest attrs
```

**Exercise 7:**

- Create the author Jan for the file example.txt
- Inspect the list of AVUs
- Add a new triple 'weight' '40' 'kg'
- Add a new triple 'type' 'file' 'unix'
- Explore the options of imeta (imeta -h)
- Overwrite the author in (author, Jan) with a different name. Do not create a new triple and delete the old one. Find a way to update the existing triple.
- Remove the author Tom
- What does imeta addw do?

