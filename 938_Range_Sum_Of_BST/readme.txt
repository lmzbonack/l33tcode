This problem makes you traverse a binary search tree in an efficient way to find all values in the tree between two values.
To do this we make use of a stack and a while loop.

We initialize the stack with the root node inside it. Inside the while loop we pop the node off the stack check if the node
is not undefined. Then check if its value needs to counted towards sum. 

After that we decide if any of the nodes children left or right need to be added to the Stack. 

To do this we see if the lower value is less than the nodes val. If it is we append the node at node.left to the stack

We also check to see if the higher value is greater than the nodes val. If it is we append the node at node.right to the stack