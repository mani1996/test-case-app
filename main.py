import os,sys,shutil

class NewTestCase(object):
	def __init__(self,folder_name):
		self.ip_count = 0 #Number of input files,output files present till now
		self.folder_name = folder_name
		if('/' not in folder_name and folder_name!=''):
			if(os.path.isdir(folder_name)):
				#raise Exception('Folder with same name already there')
				x = 0
				while(os.path.exists(folder_name+'/input'+str(x)+'.txt')):
					x+=1
					self.ip_count+=1
			else:
				os.mkdir(folder_name)
		else:
			raise Exception('Improper folder name!')

	def AddGenerator(self,path): #Path contains the absolute path to file
		if(os.path.isfile(path) and path.split('/')[-1]=='Generator.py'):
			shutil.copyfile(path,self.folder_name+'/Generator.py')
		else:
			raise Exception('Invalid File Path')

	def AddSolution(self,path): #Path contains the absolute path to file
		if(os.path.isfile(path) and path.split('/')[-1]=='Solution.py'):
			shutil.copyfile(path,self.folder_name+'/Solution.py')
		else:
			raise Exception('Invalid File Path')

