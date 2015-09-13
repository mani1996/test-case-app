# Script to generate test cases for a problem
# Purpose of problem : Finding square of each input number

from tcmanager import NewTestSuite
import random
test_object = NewTestSuite('Square')

# I am manually adding the Generator.py and Solution.py to the folder.
# Use the in-built methods if the files are in different folder and need to be moved.

no_of_tests = 10
for new_test in range(no_of_tests):
	l = random.randint(0,1000000000)
	u = random.randint(l,1000000000)
	t = 10**(new_test/2)
	test_object.NewInput([t,l,u])#Sending params to generate inputs(t-number of tests,[l,u]-Range of IP

test_object.GetOutput() #This creates output files for each input
test_object.ZipTests() #This creates the .zip file