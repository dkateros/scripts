# Some quality of life scripts
## codegen
Because we hate boilerplate.
### java-ut (Java unit test generator)
Assumes a default maven layout. Uses Junit4 and Mockito. Tested with Python 2.7.12.
1. createTestFile.sh: takes a single argument, that is hopefully the name of the class you want to generate a unit test skeleton for. Finds the java file within the working directory. Feeds this file to ctf.py that does most of the heavy lifting.
1. ctf.py: Creates a test class skeleton in the same package. Start your unit test from this skeleton :)
