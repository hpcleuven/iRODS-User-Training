# Metalnx Portal Client for VSC Users
Metalnx is a graphical user interface and serves as a client to iRODS. It help simplify most administration, collection management, and metadata management tasks removing the need to memorize the long list of iCommands. It allows users to manage content and metadata associated with content.

Via the following link [Metalnx](https://icts-p-hpc-metalnx.cloud.icts.kuleuven.be/metalnx/login/), we can reach the Metalnx portal. 

To be able to login the system, we should fill in the username and password fields of “sign in to Metalnx” form.

<img align="center" src="img/metalnx_login.png" width="400px">

The username should be your iRODS user name. The temporary password (valid only for one day) should be acquired from the account page at [password](https://vsc-passwd.icts.kuleuven.be) address. To get the password you can simply log in the mentioned address using your institution account, authorize the application, and copy the obtained password.

<img align="center" src="img/metalnx_password.png" width="400px">

Metalnx portal is mainly composed of two panes. The left pane keeps the relevant tabs of our deployment instance and the right pane provides us with the selected tabs’ functionalities.

<img align="center" src="img/metalnx_general.png" width="400px">

**Collections**: Under this tab, we can perform all data object and collection related activities. This includes adding new collections, uploading data objects, downloading collection/data objects, editing/deleting and giving user/group access permissions. This tab and its functionalities are mostly used in Metalnx.

**Search**: This tab gives search options based on the metadata and properties parameters. (there is an open issue now)

**Templates**: We can here add (create) our own metadata templates or import a template from outside in a json format.

**Shared Links**: It is possible to reach the links shared by other users.

**Favorites**: We can easily see our bookmarked collections and files.

**Public**: We can reach the public area collections.

**Favorites**: We can see the files and collections moved to trash bin.

Now let’s do some hands-on exercises:

**Exercise1**:

- Create a metalnx_test collection under your home directory.
- Give read access to your friend recursively.
- Upload a data object inside the collection.
- Add one metadata AVU to the this uploaded file. (Attribute: Author, Value: your name, Unit: Your organization).

 **Exercise2**:

- Create one public metadata template with the name of “test_training” and it has to include at least two AVUs.
- Create one private metadata template with the name of your choose.
- Add the private one on the metalnx_test collection.
- Add one of the public metadata templates on the metalnx_test collection.

Investigate the metadata of your collection and data object. We can easily come to a conclusion that managing metadata with different combinations (even multiple files may take different metadata than a collection) is quite manageable and easy.

**Exercise3**:

- Make this metalnx_test collection your favorite.
- Add a new file to this collection using the favorite tab.
- Give “own” access permission to your friend and share this file link.
- Download the first file you created to your local machine.
- Check your shared tab to see if you have any file for you. (If not, ask me to share one with you.)

**Exercise4**:
- Change the name of the second uploaded file.
- Delete this renamed file.
- Delete metalnx_test collection.
- Go to the trash tab and see your deleted items.
- Permanently delete the renamed file (deleted).
- Move deleted collection metalnx_test to public collection.

As you have seen we can do lots of data management operations easily with the Metalnx portal.

