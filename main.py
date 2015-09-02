import os,sys,shutil

class NewTestCase(object):
	def __init__(self,folder_name):
		self.ip_count = self.op_count = 0 #Number of input files,output files present till now
		if('/' not in folder_name and folder_name!=''):
			if(os.path.exists(folder_name)):
				raise Exception('Folder with same name already there')
			else:
				os.mkdir(folder_name)
		else:
			raise Exception('Improper file name!')