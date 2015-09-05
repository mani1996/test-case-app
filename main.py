import os,sys,shutil

class NewTestSuite(object):
	def __init__(self,folder_name):
		self.ip_count = 0 #Number of input files,output files present till now
		self.folder_name = folder_name
		if('/' not in folder_name and folder_name!=''):
			if(not os.path.isdir(folder_name)):
				os.mkdir(folder_name)
			self.__maintain_folders()
		else:
			raise Exception('Improper folder name!')

	#Creates folders for I/P and O/P if needed and removes junk files/folders 
	def __maintain_folders(self):
		#Input folder processing
		if(os.path.isdir(self.folder_name+'/input')):
			os.chdir(self.folder_name+'/input')
			self.ip_count = 0
			while(os.path.isfile('input'+str(self.ip_count)+'.txt')):
				self.ip_count+=1
			files = os.listdir(os.getcwd())
			allowed = ['input'+str(x)+'.txt' for x in range(self.ip_count)]
			for f in files:
				if(f not in allowed):
					if(os.path.isfile(f)):
						os.remove(f)
					else:
						shutil.rmtree(f,ignore_errors=True)

			os.chdir('../..')
		else:
			os.mkdir(self.folder_name+'/input')

		#Output folder processing
		if(not os.path.isdir(self.folder_name+'/output')):
			os.mkdir(self.folder_name+'/output')
		else:
			os.chdir(self.folder_name+'/output')
			files = os.listdir(os.getcwd())
			allowed = ['output'+str(x)+'.txt' for x in range(self.ip_count)]
			for f in files:
				if(f not in allowed):
					if(os.path.isfile(f)):
						os.remove(f)
					else:
						shutil.rmtree(f,ignore_errors=True)
			os.chdir('../..')



	def AddGenerator(self,path): #Path contains the path to source file
		self.__maintain_folders()
		if(os.path.isfile(path) and path.split('/')[-1]=='Generator.py'):
			shutil.copyfile(path,self.folder_name+'/Generator.py')
		else:
			raise Exception('Invalid File Path')

	def AddSolution(self,path): #Path contains the absolute path to source file
		self.__maintain_folders()
		if(os.path.isfile(path) and path.split('/')[-1]=='Solution.py'):
			shutil.copyfile(path,self.folder_name+'/Solution.py')
		else:
			raise Exception('Invalid File Path')

	def NewInput(self,arg): #arg contains the list of arguments to be passed to generator file
		self.__maintain_folders()
		os.chdir(self.folder_name)
		call = 'python Generator.py '
		s = ' '.join(map(lambda x:str(x),arg))
		call+=(' '+s+' > input/input'+str(self.ip_count)+'.txt')
		x = os.system(call)
		if(x==0):
			self.ip_count+=1
		else:
			os.remove('input/input'+str(self.ip_count)+'.txt')
		os.chdir('..')
		self.__maintain_folders()

	def GetOutput(self):
		self.__maintain_folders()
		os.chdir(self.folder_name)
		call = 'python Solution.py < {} > {}'
		for i in range(self.ip_count):
			x = os.system(call.format('input/input'+str(i)+'.txt','output/output'+str(i)+'.txt'))
			if(x!=0):
				os.remove('output/output'+str(i)+'.txt')
		os.chdir('..')
		self.__maintain_folders()


	def DeleteTest(self,index):
		self.__maintain_folders()
		os.chdir(self.folder_name)
		os.chdir('input')
		if(os.path.isfile('input'+str(index)+'.txt')):
			os.remove('input'+str(index)+'.txt')
			for i in range(index+1,self.ip_count):
				os.rename('input'+str(i)+'.txt','input'+str(i-1)+'.txt')
		os.chdir('..')
		os.chdir('output')
		if(os.path.isfile('output'+str(index)+'.txt')):
			os.remove('output'+str(index)+'.txt')
			i = index+1
			while(os.path.isfile('output'+str(i)+'.txt')):
				os.rename('output'+str(i)+'.txt','output'+str(i-1)+'.txt')
				i+=1
		os.chdir('../..')