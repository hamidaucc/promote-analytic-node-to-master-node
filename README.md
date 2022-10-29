# In-vRealize-operation-manager-how-to-promote-analytic-node-to-master-node
One of the ideas I have is to create a Python script to update the primary node role to a different node. It's extremely time-consuming process to do and would be quite beneficial to have by selecting the node from a list, then update the selected node to become the primary node.
Completing this manually on a cluster with 2 nodes is usually 30-40 mins. Any larger clusters will take much longer and is susceptible to human errors as it's updating an extremely long JSON line in a script file and can be built-in to take a backup of the file as well

This is a collaboration space, while working on a project for the SRE 2.0 training (2022).
The resource list which we will automate, to reduce errors when manually follow different KBs and procedures:
https://ikb.vmware.com/s/article/2135749
https://ikb.vmware.com/s/article/82421
https://ikb.vmware.com/s/article/2114077
https://ikb.vmware.com/s/article/2150176
