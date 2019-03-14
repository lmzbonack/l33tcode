Iterative Solution:

Grab first node - if that nodes value is less than the value we need to insert make node.right the next node value to evaluate
if that nodes values is greater than the value we need to insert make node.left the next node value to evaluate

Do this until there is no node to change the current node value to. When that happens create a new node with that value
break the loop as well.