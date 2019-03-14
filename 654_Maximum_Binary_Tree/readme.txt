This problem is solved with recursion. The first step is finding the largest value in the list along with the index of that value.
Next, create the root note with the largest value.
Then, create the left and right nodes with recursion by making use of the index that we grabbed earlier.

Do this until nums is empty then return the root node as the instructions indicate