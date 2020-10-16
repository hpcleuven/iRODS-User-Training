# Yoda Portal Client for VSC Users

*Prerequisites:*  
*-A VSC-account coupled to an iRODS account*    
*-You should be added to some test groups by the HPC staff before starting this tutorial.*
*-Some of these exercises are made for groups, but you can do most of them alone*

[Yoda](https://yoda.uu.nl/yoda-uu-nl/what-is-yoda/index.html) is a research data management solution on top of iRODS developed by Utrecht University. Yoda portal is a web application for performing data management activities, such as managing access to your data and changing metadata. It allows users to deploy and manage their research data.

You can reach the Yoda portal by clicking [VSC-Yoda]( https://icts-p-hpc-yoda-portal.cloud.icts.kuleuven.be/user/login) login page.

To be able to login the Yoda, we should fill in the username and password fields of “sign in to Yoda” form.

<img align="center" src="img/yoda_login.png" width="400px">

You should enter your iRODS user name in the username field. For password field, you should first obtain a temporary password (valid only for one day) from the account page at [password](https://vsc-passwd.icts.kuleuven.be) address. 

To get the password you can simply log in the mentioned address using your institution account, authorize the application, and copy the obtained password.

<img align="center" src="img/yoda_password.png" width="400px">

In VSC-Yoda portal, there are two main workspaces, “research” and “vault”.

**Research**: Collaboration workspace for a research group. No restrictions on the organization of data in folders. Metadata can be added to a folder. When all required metadata has been added a folder can be archived. You can view/edit/add metadata for a dataset that will be placed in the vault.

VSC users are expected to use mostly this space.

**Vault**: This area has a 'deposit' functionality which VSC users will not use. Tier-1 Data service users will use this area as an output of research area and an input to compute system. 

**Group Manager**: To keep data in a secure way Yoda allows you to put the data in data compartments, which can only be accessed by members. The Group Manager can create category/subcategory/group as data compartments and their members. People with a “group manager” role can add members to a data compartment, remove them, and change their roles.

<img align="center" src="img/yoda_general.png" width="400px">

Use the Research menu item to manage your data. Each data compartment has two main folders:

The main folder (“research-…”) contains current research data that researchers collaborate on. Data is kept in subfolders. The subfolders can be organized according to the needs of the researcher.

Use the “Submit” button to deposit the subfolder. This will copy the contents of the subfolder to the Vault folder as a new data package (see below). Before doing so, the subfolder must be described with metadata, which can be entered by clicking on the Metadata button. The folder named “vault-…” contains deposited data packages. Once deposited, data cannot be removed. Therefore the vault can be used to account for data in a research project to comply with FAIR principles.

**Note**: If a collection is created in iRODS, we can see it with its content in Yoda but we cannot edit anything. A collection created first in Yoda can be seen/edited both in Yoda and iRODS.

To allow different communities to share the same Yoda implementation the concept of categories and subcategories were introduced. Every group has a category and subcategory. Within the group-manager groups are grouped into a tree of categories and subcategories. See [category/permission](https://github.com/UtrechtUniversity/yoda/blob/development/docs/design/group-manager.md)

We can do now some hands-on exercises:

**Exercise1**:  
- Go to the 'group manager' tab. 

Under 'Yoda groups', there are categories, which may contain subcollections, which contain research groups.
You should be part of at least one research groups. If not, you will be added soon.

- If you have been made group manager, invite your teammates to the group. 
- Click on your group to see some information about it on the right-hand side.

Congratulations! You and your teammates have now a shared research-folder where you can put data and work together.

**Exercise2**:
- Go to the tab 'research', and go to your research folder.
- Add a collection with 'test' + your name as title.  
- Upload a file from your pc to the collection you just created.  
- Try to download this file again. You can also try to download the files of your teammates.

**Exercise3**:

- Fill in default metadata form for your collection.

**Exercise4**:

- Use the search field options to find your previously uploaded file. Feel free tot play around and search other things to increase your understanding of the search function.

**Exercise5**:

- Lock one of the collections.


