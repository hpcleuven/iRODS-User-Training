# iRules for VSC Users
In iRODS rules are used to let organizations automate their data management tasks. At the community level policies are determined and rules are used to automate these determined policies. iRODS has its own rule language which is a domain specific language to define policies and actions in the system. However there is the iRODS rule engine plugin interface that allows iRODS administrators and users to write iRODS policy rules in other languages, e.g. Python. 

Execution type of rules based on the accepted policies may change. Most of the rules with complex data issues are triggered Policy Enforcement Points (PEP) in terms of automation. But some rules can be triggered by the `irule` command.

Therefore we can categorize the rules as system level rules and user-defined rules. User-defined rules can be written into a local file in our VSC system and we control the execution of these rules.

