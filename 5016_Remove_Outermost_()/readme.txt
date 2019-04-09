In this problem the most important realization that you have to come to is that a primitive decomposition 
can be identified by looking for an equal number of '(' and ')'

Once you realize this you set up counter variables for each character type, a stack to hold data, and a blank solution
string to append your answer onto.

Loop through the string incrementing the counters as appropriate and once they are equal pull all the characters
in the stack out and place them in their own string. Slice the first and last character off that string. Then append
it to the solution you return.

After this is done you reset the stack and also the counter variables