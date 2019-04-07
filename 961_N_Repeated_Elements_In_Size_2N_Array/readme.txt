This problem is more simple than it initially looks. Because of what we are told about the array:
1. Size 2N
2. N+1 Unique elements
3. One element is repeated N times

This means that only the element that is repeated N times exists more than once in the array. This can be seen in the examples below

[1,2,3,3] -> 3

[2,1,2,5,3,2] -> 2

[5,1,5,2,5,3,5,4] -> 5

So to solve the problem I just created a new set named stack to hold values as I iterate through the list. During each iteration I check to see if the value 
already exists in the stack. If it does we have found our answer, return that value. If it does not append the value onto the stack

