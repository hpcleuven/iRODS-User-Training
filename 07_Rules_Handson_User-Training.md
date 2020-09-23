# iRules for VSC Users

## What are rules?
With rules, organizations can automate their data management tasks in iRODS. At the community level policies are determined and rules are used to automate these determined policies. iRODS has its own rule language which is a domain specific language to define policies and actions in the system. However, there is the iRODS rule engine plugin interface that allows iRODS administrators and users to write iRODS policy rules in other languages, e.g. Python. Rules are an important part of iRODS: automating data management policies reduces not only the workload but also human errors, making our data management more consistent.

There are two types of rules. System level rules handle complex data issues. They are determined by administrators and triggered by Policy Enforcement Points (PEP). 

On the other side, we have user-defined rules. Users can trigger their rules they wrote themselves with the `irule`command. These can be written into a local file in our VSC system. You can think of these the same way as scripts in other languages like python or bash. In this tutorial, we will dive deeper into user-defined rules.

By the end you will be able to:
* Execute rules through the `irule` command    
* Write your own user-defined rules


## Executing rules with iRule
Calling the irule command on example file, rulename.r, goes as follows:

```sh
irule -F Rulename.r
```
The option -F means that we supply the rule in a file. There are other ways to call rules, but this is the way we will use.


## Writing rules: the basics
Inside the file, you will find one or multiple rules. These rules have a syntax like this:

```
*rulename*{
    on(*condition*){
    
    *actions*
    
   }

}

input *input*
output *output*
```
Note that not all of these parts are mandatory. For example, if our rule uses no input, we can set input to NULL or just not mention it. Likewise, if there is no specific condition to be met, we can remove the 'on()' and the extra pair of curly brackets.

A rule that simply prints 'Hello World!' to the terminal would look like this:

```
helloworld{
    writeLine('stdout', 'Hello World!');
}

output ruleExecOut
```

As you can see, the command `writeLine('stdout', 'your message');` is the common way to print things.

In a file, only the first rule gets triggered by iRule, even . However, you can call these other rules in your first rule, as illustrated by this example:

```
firstRule{
    writeLine('stdout', 'This is my first rule');
    secondRule()
}

secondRule{
    writeLine('stdout', 'This is my second rule');
}

output ruleExecOut
```

**Exercise 1**

* Write a rule that prints "Hello" and your name
* Write a rule that prints the sum of 5 and 3

If you don't know how to do certain things, like adding numbers, you can always look them up in the [documentation of the iRODS rule language](https://docs.irods.org/4.2.8/plugins/irods_rule_language/).

<details>
  <summary>Solution</summary>

  ```
  nameRule{
    writeLine('stdout', 'Hello Jan');
  }
  output ruleExecOut
  ```
  
  ```
  sumRule{
    writeLine('stdout', 3+5);
  }
  output ruleExecOut
  ```
</details>


## Input and variables

Variables in iRODS always start with an **\***.
They can either be specified as input or in the body of the rule

```
variableRule{
    
    #you can define a variable here
    *var1="Hello";
    writeLine('stdout', *var1 ++ var2);
}

#you can also define a variable here
input *var2="World"
output ruleExecOut
```

You can also ask the user for input by setting the value of the variable to $.
When running the rule, the user will be prompted to give a value.
After the dollar sign, you can also specify a default value, but this is not mantadory.

```
promptRule{
    writeLine('stdout', "I Like" ++ myFavoriteFruit);
}

input myFavoriteFruit=$"apples"
output ruleExecOut 
```

**Exercise 2**

* Write a rule that ask users their name and prints "Hello \[name\]"

<details>
  <summary>Solution</summary>
        
  ```
  helloNameRule{
    writeLine('stdout', 'Hello ' ++ *name);
  }
  
  input *name=$
  output ruleExecOut
  ```
</details>



## Queries

Of course, we can do more with rules than do calculations and print lines. We can also get information about our data, collections,... in iRODS.
One way to do this is by searching collections or data objects with SQL queries:

```
queryRule{
    foreach(*i in SELECT COLL_NAME, DATA_NAME WHERE COLL_NAME like '%test%'){
        *coll = *i.COLL_NAME;
        *data = *i.DATA_NAME;
        writeLine("stdout", "*coll/*data");
    }
    writeLine("stdout", "listing done");
}

output ruleExecOut
```

**Exercise3**

1.  In your linux environment, make the files cat.txt and dog.txt
2.  In iRODS, create a folder called 'animals' and change your working directory to this folder
3.  Upload cat.txt and dog.txt to the 'animals' folder
4.  Write a rule that lists all files in that folder

<details>
    <summary>Solution</summary>
    
   ```
   queryRule{
       foreach(*i in SELECT COLL_NAME, DATA_NAME WHERE COLL_NAME like '%animals%'){
           *coll = *i.COLL_NAME;
           *data = *i.DATA_NAME;
           writeLine("stdout", "*coll/*data");
       }
   }
    
   output ruleExecOut
   ```  
</details>


## Using microservices
We have shown you how to query iRODS for information, but how do we actually interact with iRODS? 
This is done by using microservices, which are small, preprogrammed functions. For example, there are microservices that create a collection, remove a data object or add metadata. 
By chaining these tiny tasks together, you can automate your workflow.

You can find an overview of all available microservices in the [iRODS documentation](https://docs.irods.org/4.2.8/) under the tab ['Doxygen'](https://docs.irods.org/4.2.8/doxygen/). These pages also contain the parameters needed to use a certain microservice.

Here is a simple example of a rule that uses a microservice to create a collection called 'myCollection' in your home folder.
To run it, replace the placeholder with your VSC account (e.g. vsc00001).


```
createCollRule {
        *path="/kuleuven_tier1_pilot/home/[your VSC account]/myCollection";
        writeLine("stdout", "Creating a collection");
        msiCollCreate(*path, 0, *Status);
        writeLine("stdout", "Collection created");
}
output ruleExecOut

```

**Exercise 4**
1. Adding metadata to an object
    * Create a file called sun.txt and upload it to iRODS
    * Look up the microservices msiAddKeyVal() and msiAssociateKeyValuePairsToObj()
    * Write a rule with those two microservices to give the file the attribute-value pair 'temperature': 'hot'
2. Write a rule that prompts the user to give a name, and create a collection with that name



<details>
    <summary>Solution</summary>
   
   ```
   addMetadataRule {
   
        #making a variable with the path of sun.txt in string format
        *dataObj="/kuleuven_tier1_pilot/home/[your VSC account]/sun.txt"
   
        #creating the key-value pair
        msiAddKeyVal(*Keyval,'temperature','hot');
        
        #assigning the pair to the data object
        msiAssociateKeyValuePairsToObj(*Keyval,*dataObj,"-d");
        WriteLine('stdout', 'Metadata assigned');
   }
   
   output ruleExecOut
        
   ```  
   
   You can check whether this worked with the command `imeta ls -d sun.txt`.
   
   ```
   createCollRule {

        *path="/kuleuven_tier1_pilot/home/vsc33731/" ++ *collectionName

        writeLine("stdout", "Creating a collection");
        msiCollCreate(*path, 0, *Status);
        writeLine("stdout", "Collection created");

    }

    input *collectionName=$"myCollection"
    output ruleExecOut
    
   ``` 
    
</details>
