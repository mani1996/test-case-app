import os,sys,shutil

class NewTestCase(object):
	def __init__(self,folder_name):
		self.ip_count = self.op_count = 0 #Number of input files,output files present till now
		if(os.path.exists(folder_name)):
			ch = raw_input('Folder already exists.\nEnter "y" to delete existing folder and proceed:')
			if(ch=='y'):
				shutil.rmtree(folder_name,ignore_errors=True)
				os.mkdir(folder_name)
			else:
				self.ip_count = self.op_count = -1 #Invalid, basically
		else:
			os.mkdir(folder_name)


			


