#import Arithmatic

#import Arithmatic as AR

from Arithmatic import Addition,Substraction

# from Arithmatic import*

#Entry point function
def main():
	print("__name__from main is:",__name__)
	print("Enter first number")
	value1=int(input())
	
	print("Enter Second number")
	value2=int(input())
	
	ret1=Addition(value1,value2)
	ret2=Substraction(value1,value2)
	
	print("Addition is: ",ret1)
	print("Substraction is: ",ret2)
	
#code starter
if __name__=="__main__":
	main()



