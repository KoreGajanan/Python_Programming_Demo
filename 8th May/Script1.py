from sys import *

def main():
	print("------------Marvellous Infosystems---------");
	print("Script title: "+argv[0]);

	if(len(argv)!=2):
		print("Insufficient Arguments to the script");
		exit();
	if(argv[1]=="-u")or (argv[1]=="-U"):
		print("Use the script as Name.py Parameters");
	
	if(argv[1]=="-h") or (argv[1]=="-H"):
		print("This is demo automation script");
	
if __name__=="__main__":
	main();
