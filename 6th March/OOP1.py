
class Marvellous:
	Value1=11						#class/static characteristics
	
	def __init__(self,no1,no2):		#constructor
		self.i=no1					#instance variable
		self.j=no2
		print("Inside constructor..")
	
	def __del__(self):			#destructor
		print("Inside destructor")

	def Fun(self):
		print("Inside fun method")
		print("value of j is",self.j)
def main():
	obj1=Marvellous(11,21)			#creating the object
	obj2=Marvellous(51,101)
	
	# print("Value of i from obj1",obj1.i)   #accessing instance members
	# print("Value of i from obj2",obj2.i)
	print("Value of class member",Marvellous.Value1)
	
	obj1.Fun()		
	obj2.Fun()
	
	# del obj1
	# del obj2
	
if __name__=="__main__":
	main()



	

