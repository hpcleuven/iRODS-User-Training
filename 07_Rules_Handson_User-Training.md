# iRules for VSC Users

## What are rules?
In iRODS rules are used to let organizations automate their data management tasks. At the community level policies are determined and rules are used to automate these determined policies. iRODS has its own rule language which is a domain specific language to define policies and actions in the system. However there is the iRODS rule engine plugin interface that allows iRODS administrators and users to write iRODS policy rules in other languages, e.g. Python. Rules are an important part of iRODS: automating data management policies reduces not only the workload but also human errors, making our data management more consistent.

Execution type of rules based on the accepted policies may change. Most of the rules with complex data issues are triggered Policy Enforcement Points (PEP) in terms of automation. We call this type of rules system level rules, and they are managed by the admins.

On the other side, we have user-defined rules. Users can trigger their rules they wrote themselves with the `irule`command. These can be written into a local file in our VSC system. You can think of these the same way as scripts in other languages, which are used to automate tasks. In this tutorial, we will dive deeper into these user-defined rules.

By the end you will be able to:
* Write your own user defined rules
* Execute your own rules through the `irule` command

## Working with *irule*
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


<details>
  <summary>Solutions</summary>

  Solutions to exercises will come here

</details>


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
