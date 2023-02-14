#To run, enter "python3 MetaTests.py" on Shell
import os
import subprocess

#Open Results files
file1 = open("Tests/Results/Runner1.txt", "w+")
file2 = open("Tests/Results/Runner2.txt", "w+")
file3 = open("Tests/Results/Runner3.txt", "w+")
file3 = open("Tests/Results/Jobs.txt", "w+")
file3 = open("Tests/Results/Search_someone.txt", "w+")
os.system('clear');

def empty_students():
  student = open("students.json", "w")
  student.write("{\n}")
empty_students()
#Run tests, print to results files.
os.system('echo "Running testrunner.py"')
#os.system('pytest "./Tests/Sprint 1/testrunner.py" > Tests/Results/Runner1.txt')
os.system('pytest "./Tests/testrunner.py" > Tests/Results/Runner1.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Runner1.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]
print(tempstr)
file1.close()

empty_students()
os.system('echo "Finished testrunner.py\n\nRunning testrunner2.py"')
#os.system('pytest "./Tests/Sprint 1/testrunner2.py" > Tests/Results/Runner2.txt')
os.system('pytest "./Tests/testrunner2.py" > Tests/Results/Runner2.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Runner2.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]
print(tempstr)
file2.close()

empty_students()
os.system('echo "Finished testrunner2.py\n\nRunning testrunner3.py"')
#os.system('pytest "./Tests/Sprint 1/testrunner3.py" > Tests/Results/Runner3.txt')
os.system('pytest "./Tests/testrunner3.py" > Tests/Results/Runner3.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Runner3.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]
print(tempstr)
file3.close()

empty_students()
os.system('echo "Finished testrunner3.py\n\nRunning testrunner_jobs.py"')
#os.system('pytest "./Tests/Sprint 2/testrunner_jobs.py" > Tests/Results/Jobs.txt')
os.system('pytest "./Tests/testrunner_jobs.py" > Tests/Results/Jobs.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Jobs.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]
print(tempstr)
file3.close()

empty_students()
os.system('echo "Finished testrunner_jobs.py\n\nRunning testrunner_search_someone.py"')
#os.system('pytest "./Tests/Sprint 2/testrunner_search_someone.py" > Tests/Results/Search_someone.txt')
os.system('pytest "./Tests/testrunner_search_someone.py" > Tests/Results/Search_someone.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Search_someone.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]
print(tempstr)
os.system('echo "Finished testrunner_search_someone.py\n"')
file3.close()
empty_students()