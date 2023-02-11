#To run, enter "python3 MetaTests.py" on Shell
import os
import subprocess

#Open Results files
file1 = open("Tests/Results/Runner1.txt", "w+")
file2 = open("Tests/Results/Runner2.txt", "w+")
file3 = open("Tests/Results/Runner3.txt", "w+")
os.system('clear');

#Run tests, print to results files.
os.system('echo "Running testrunner.py"')
os.system('pytest ./Tests/testrunner.py > Tests/Results/Runner1.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Runner1.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]
print(tempstr)
file1.close()

os.system('echo "Finished testrunner.py\n\nRunning testrunner2.py"')
os.system('pytest ./Tests/testrunner2.py > Tests/Results/Runner2.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Runner2.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]
print(tempstr)
file2.close()

os.system('echo "Finished testrunner2.py\n\nRunning testrunner3.py"')
os.system('pytest ./Tests/testrunner3.py > Tests/Results/Runner3.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Runner3.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]
print(tempstr)
os.system('echo "Finished testrunner.py\n"')
file3.close()