
class Student:
	School="MR"										#class variable
	
	def __init__(self,no1,no2,no3):
		self.m1=no1								#instance variable
		self.m2=no2
		self.m3=no3
				
	def Instance_Total(self):					#instance method
		print("Inside instance method")
		return self.m1+self.m2+self.m3
		
	@classmethod							#decorator
	def Class_DisplaySchool(cls):			#class method  #cls is keyword
		print("School name is: ",cls.School)
	
	@staticmethod						#decorator
	def Static_Info():					#static method
		print("This class contains the information of school")
		
def main():
	Student.Class_DisplaySchool()			#calling class method
	obj1=Student(50,80,70)			#object creation
	obj2=Student(65,80,75)
	ret=obj1.Instance_Total()
	print("Total obt marks",ret)
	Student.Static_Info()					#calling static method
	
	
if __name__=="__main__":
	main()