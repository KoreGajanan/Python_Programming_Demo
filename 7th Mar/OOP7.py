class C:
	def LearnAndCode(self):
		print("Learning C Programming")
		
class Cpp:
	def LearnAndCode(self):
		print("Learning C++ Programming")

class Golang:
	def LearnAndCode(self):
		print("Learning Golang Programming")
		
class Programmer:
	def Coding(self,language):
		language.LearnAndCode()

cobj=C()
cpobj=Cpp()
gobj=Golang()

obj=Programmer()
obj.Coding(cobj)
obj.Coding(cpobj)
obj.Coding(gobj)


