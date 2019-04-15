I am sure there is a better way to solve this. My approach was to create a helper function that iterated through the pattern 2 times.

The first time it creates a map that stores the values of the pattern and what their values should be

The second time it checks to make sure that the values are correct in the word

I then use this helper to evaluate every item in the original words array and return the subset of words that "pass"