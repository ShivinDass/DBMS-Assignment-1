# DBMS-Assignment-1
Compares the performmance of databases that use metadata files against the ones that don't

In our submission we have submitted 3 program files and 2 text files.

program1_2016091_2016220.py : Implementation of the program that does not use metadata file as given in the assignment

program2_2016091_2016220.py : Implementation of the program that uses metadata to read the user file and execute operations on it.

fileGen.py : Used for generating the large valued database to measure the efficiency of the program.

data.txt : A sample database to demonstrate the implementation

metadata.txt : The metadata file of data.txt



EFFICIENCY

To compare the efficiency of the two programs we had to increase the number of attributes of the data base 
and hence the size of the metadata file as well.

**In order to do so we changed program1.py to adapt to such large values whereas changing the metadata file for
program2.py was enough.


We checked the two programs for a value of 100000 attributes:-

Time taken by program1.py : 4.81s
Time taken by program2.py : 5.49s

This shows how for a larger number of values program1 will be much more efficient.
