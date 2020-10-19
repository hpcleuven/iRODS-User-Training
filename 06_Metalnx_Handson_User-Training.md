# Metalnx Portal Client for VSC Users
*This version of the tutorial is meant for the iRODS training for humanities researchers at KU Leuven*

*Prerequisites:*  
*-A VSC-account coupled to an iRODS account*  
*-The dataset provided for the exercises*

Metalnx is a graphical user interface and serves as a client to iRODS. It help simplify most administration, collection management, and metadata management tasks removing the need to memorize the long list of iCommands. It allows users to manage content and metadata associated with content.

Via the following link [Metalnx](https://icts-p-hpc-metalnx.cloud.icts.kuleuven.be/metalnx/login/), we can reach the Metalnx portal. 

To be able to login the system, we should fill in the username and password fields of “sign in to Metalnx” form.

<img align="center" src="img/metalnx_login.png" width="400px">

The username should be your iRODS user name. The temporary password (valid only for one day) should be acquired from the account page at [password](https://vsc-passwd.icts.kuleuven.be) address. To get the password you can simply log in the mentioned address using your institution account, authorize the application, and copy the obtained password.

<img align="center" src="img/metalnx_password.png" width="400px">

Metalnx portal is mainly composed of two panes. The left pane keeps the relevant tabs of our deployment instance and the right pane provides us with the selected tabs’ functionalities.

<img align="center" src="img/metalnx_general.png" width="400px">

**Collections**: Under this tab, we can perform all data object (= a file) and collection related activities
 
- Uploading files  
- Moving files/collections  
- Copying files/collections  
- Renaming files/collections  
- Applying metadata templates (see later)  
- Downloading files  

Behind any collection or file, you can press 'View info' for the following options:

- Adding metadata to files/collections  
- Adding files/collections to favorites  
- Setting permissions  
- Getting previews of files  

This tab and its functionalities are mostly used in Metalnx.

**Search**: This tab gives search options based on the metadata and properties parameters (currently not available).

**Templates**: We can here create our own metadata templates or import a template from outside in a json format. These can then be applied to files or collections.

**Shared Links**: Here you can see the links shared by other users.

**Favorites**: Here you can see your bookmarked collections and files.

**Public**: here you can reach the public area collections.

**Trash**: Here you can see the files and collections moved to trash bin.

Now let’s do some hands-on exercises:

**Exercise 1: data objects, folders and metadata**:

- Create a collection named 'Medieval corpus' under your home directory (the directory with your VSC-account name).
- Upload the files from the dataset to the collection. You can upload multiple datasets at a time.
- Click on 'view info' to see some basic information about each of the files.
- Go to file 002_f01_m01_c11.txt. Click on 'view info' and then on preview.

  Something is clearly wrong  with this file. Go ahead and edit the file in preview mode, then save it.
  
- Edit the metadata of this same file and give it the attribute 'Century' and value '11'.
- One of the files in the collection 'Medieval corpus' clearly has the wrong name. Please rename it to '001_f01_m01_c11.txt'.
- Download one of the files to your local machine.

 **Exercise 2: metadata templates**:

- Create one private metadata template with the name of “Historical datasets” and it has to include at least two AVUs.
- Create one public metadata template with the name of your choice.
- Apply the public template one of your files.
- Apply the template 'Historical datasets' to the collection 'Medieval corpus'.

Take a look at the metadata of that file and collection. As you can see, we can easily manage metadata on both collections and the files in them, even if they have different metadata.

**Exercise 3: favorites and sharing**:

- Add the 'Medieval corpus' collection to your favorites.
- Give “own” access permission for one of your files to a friend and share the file link.
- Check your shared tab if there are any files shared with you. (If not, ask me to share with you one.)

**Exercise 4: deleting**:
- Go back to the collections tab, then to the collection 'Medieval corpus'
- One of the files clearly doesn't belong in this collection here! Please search which one, and delete it. 
- Delete the entire collection 'Medieval corpus'.

  ...okay, perhaps we should not have done that. Let's try to get it back!
  
- Go to the trash tab and look at your deleted items.
- Permanently delete the deleted file.
- Move the deleted collection metalnx_test to your home directory again.

As you have seen we can do lots of data management operations easily with the Metalnx portal.

