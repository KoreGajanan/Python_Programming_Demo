
def Addition(value1,value2):
	ret=value1 + value2
	return ret
    
def main():	
 no1=int(input("Enter First no"))
 no2=int(input("Enter Sec no"))

 ans=Addition(no1,no2)    

 print("Addition is: ",ans)
 
if __name__ =="__main__":
	main()