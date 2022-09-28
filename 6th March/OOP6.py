class Base1:
	def __init__(self):
		print("Inside Base1 constructor")
	def fun(self):
		print("Base1 fun")

class Base2:
	def __init__(self):
		print("Inside Base2 constructor")
	
	def fun(self):
		print("Base2 fun")	
		
class Derived(Base2,Base1):
	def __init__(self):
		Base1.__init__(self)#call base1 constructor fisrt   if we write Base2.__init__(self) then it display Base2constructor
		Base2.__init__(self)
		self.a=50
		self.b=60	
		print("Inside derived1 constructor")
		
def main():
	dobj=Derived()
	dobj.fun()
	
if __name__=="__main__":
	main()