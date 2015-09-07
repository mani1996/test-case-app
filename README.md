##**Test case manager**
A Python module to maintain multiple test suites locally. 

###**Requirements**
1.	Linux OS
2.	Python 2 ( Tested with Python 2.7) - Available with most Linux OS

###**Documentation**
**Note:** 

**1.** The test suite folder will be created in the folder where test suite object is initialized. Make sure that the chosen folder has read-write access.

**2.** The test suite folder contains 2 folders - **input** and **output** and  should contain the 2 files **Generator.py** and **Solution.py** . Details regarding these 2 files are explained below.

**3.** Make sure the codes for generating inputs and outputs don't have infinite loops. This will be automated as well in the future.

**Methods:**

1. **Creating a new object:**

	    from tcmanager import NewTestSuite
	    test_object = NewTestSuite('folder_name')

   This creates a new folder if folder is not present. It selects the existing folder, otherwise. 
   
2. **Adding generator file:**
        
	    test_object.AddGenerator('type_path_here')
    
   Generator file is the file which contains code to generate input based on parameters. Path refers to the path of the generator file in system.
   
 **Note:** The source file must be named as **_Generator.py_**
 
3. **Adding solution file:**  
		
		test_object.AddSolution('type_path_here')
	
	Solution file is the file which contains code to generate outputs for the test cases. Path refers to the path of solution file in system.
	
	**Note:** The source file must be named as **_Solution.py_**

4.  **Adding a new input file:**
	
		test_object.NewInput(args)

   _args_  is a list/tuple containing the set of parameters to be passed to generator code for new input file. These parameters can be accessed from the **_sys.argv_** parameter of generator file.
   
   **Note:** 
   1. The parameters start from sys.argv[1]. sys.argv[0] contains 'Generator.py' . 
   2. Add the **_Generator.py_** file before calling this function.
 
5.  **Generating outputs:**
		 
		 test_object.GetOutput()
	     
	This will generate output files if the code works successfully. Otherwise, the output folder is left empty.
	**Note:** Add the **_Solution.py_** file before calling this function.
   
6.  **Delete Test:**

		test_object.DeleteTest(index)
	
   This will delete the test case with given index. To find out the corresponding test case, check **input** folder, mentioned above. Out of bounds indices are ignored.

  **Note:** Indexing starts from 0 (**not 1**)

7.  **Create archive:**
		
		test_object.ZipTests()
	This will create a **.zip** archive containing input and output folders. The archive will be present in the folder of the Test Suite.  
