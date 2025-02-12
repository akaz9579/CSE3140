import os

#going into LabGen to find the files 
os.chdir('/home/cse/Lab2/LabGen')

files = os.listdir('.') #list of all these files 

output = "Q1A.out" #creates the out file 

#changes back to Solutions for it to be stored here. 
os.chdir('/home/cse/Lab2/Solutions')

#opens output file to write all file names in  
    for f in files: 
        out.write(f + "\n")
    
