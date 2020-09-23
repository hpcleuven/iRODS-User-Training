# iRules for VSC Users

## What are rules?
In iRODS rules are used to let organizations automate their data management tasks. At the community level policies are determined and rules are used to automate these determined policies. iRODS has its own rule language which is a domain specific language to define policies and actions in the system. However there is the iRODS rule engine plugin interface that allows iRODS administrators and users to write iRODS policy rules in other languages, e.g. Python. Rules are an important part of iRODS: automating data management policies reduces not only the workload but also human errors, making our data management more consistent.

Execution type of rules based on the accepted policies may change. Most of the rules with complex data issues are triggered Policy Enforcement Points (PEP) in terms of automation. We call this type of rules system level rules, and they are managed by the admins.

On the other side, we have user-defined rules. Users can trigger their rules they wrote themselves with the `irule`command. These can be written into a local file in our VSC system. You can think of these the same way as scripts in other languages, which are used to automate tasks. In this tutorial, we will dive deeper into these user-defined rules.

By the end you will be able to:
* Write your own user defined rules
* Execute your own rules through the `irule` command

## The basics of *irule*
Calling the irule command on example file, Rulename.r, goes as follows:

```sh
irule -F Rulename.r
```
The option -F means that we supply the rule in a file. There are other ways to call rules, but this is the way we will use.


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
Note that not all of these parts are mantadory. For example, if our rule uses no input, we can set input to NULL or just not mention it. Likewise, if there is no specific condition to be met, we can remove the 'on()' and the extra pair of curly brackets.

A rule that simply prints 'Hello World!' to the terminal would look like this:

```
helloworld{
    writeLine('stdout', 'Hello World!');
}

output ruleExecOut
```

As you can see, the command `writeLine('stdout', 'your message');` is the common way to print things.



**Exercise 1**

* Write a rule that prints "Hello" and your name
* Write a rule that prints the sum of 5 and 3

If you don't know how to do certain things, you can always look them up in the [documentation of the iRODS rule language](https://docs.irods.org/4.2.8/plugins/irods_rule_language/).

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
rule{
    
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
rule{
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

<!--- Of course, we can do more with rules than do calculations and print lines. We can also get information about our data, collections,... in iRods.-->

## Using microservices
<!---We have shown you how to query iRods for information, but how do we actually interact with iRODS? This is done by using microservices, which are small, preprogrammed functions. For example, there are microservices that create a collection, remove a data object or add metadata. By chaining these tiny tasks together, you can automate your workflow. -->

<!---

These are previous parts of the tutorial

**Exercise1**

Create firstrule.r file with the following command and execute it.

```sh
MyFirstRule {
    writeLine("stdout", "Hello world!");
 }

OUTPUT ruleExecOut
```

**Exercise2**

Create hello.r file with the following command and execute it.

```sh
HelloWorld{
        writeLine("stdout", "Hello *name!");
}

INPUT *name="iRODS project group"
OUTPUT ruleExecOut, *name
```

**Exercise3**

Create list.r file with the following command and execute it.

```sh
recursiveList{
    foreach(*i in SELECT COLL_NAME, DATA_NAME WHERE COLL_NAME like '%test%'){
        *coll = *i.COLL_NAME;
        *data = *i.DATA_NAME;
        writeLine("stdout", "*coll/*data");
    }
    writeLine("stdout", "listing done");
}

input null
output ruleExecOut
```

-->
