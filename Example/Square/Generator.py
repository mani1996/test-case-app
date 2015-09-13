#The file which generates inputs based on parameters from tcmanager.NewTestSuite.NewInput method
import sys,random
params = sys.argv[1:] # First argument of sys.argv contains the filename('Generator.py')
t,l,u = map(lambda x:int(x),params)
print t
for i in range(t):
	print random.randint(l,u)

