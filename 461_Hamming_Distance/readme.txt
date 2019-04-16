This one was pretty simple. The hardest part was learning how to convert integers to binary in Python

Once this was done I checked to make sure that the two binary representations were the same length. If they
are not I added padding of zeroes to make them the same length.

After that I looped through the x binary representation and checked the corresponding positions for each 'bit'
in the y binary representation. Incrementing the ham_distance whenever the 'bits' were different