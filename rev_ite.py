#!/usr/bin/python3

##########################################################################################################
#Program that takes a number and then iterates ovet it in reverse direction using Python Iterator Protocol
##########################################################################################################

class mclass:
	def __init__(self,n):
		self.i = 0
		self.n = n
	
	def __iter__(self):
		return mclass_rev_iter(self.n)
	

class mclass_rev_iter:
	def __init__(self,n):
		self.i = n-1
		
	def __next__(self):
		if(self.i >= 0):
			ret = self.i
			self.i-=1
			return ret
		else:
			raise StopIteration()

			
			
if __name__ == '__main__':
	mobj = mclass(5)

	for i in mobj:
		print(i)
