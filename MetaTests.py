#To run, enter "python3 MetaTests.py" on Shell
'''
import os
import subprocess

os.system('clear')

def empty_students():
  student = open("students.json", "w")
  student.write("{\n}")
def empty_jobs():
  jobs = open("job_postings.json", "w")
  jobs.write("{\n}")
  
empty_students()
#Run tests, print to results files.
print("Running testrunner.py")
os.system('python3 -m pytest Tests/testrunner.py > Tests/Results/Runner1.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Runner1.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]
print(tempstr)

empty_students()
print("Finished testrunner.py\n\nRunning testrunner2.py")
os.system('python3 -m pytest Tests/testrunner2.py > Tests/Results/Runner2.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Runner2.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]
print(tempstr)


empty_students()
empty_jobs()
print("Finished testrunner2.py\n\nRunning testrunner_jobs.py")
os.system('python3 -m pytest Tests/testrunner_jobs.py > Tests/Results/Jobs.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Jobs.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]

empty_jobs()
print("Finished testrunner_jobs.py\n\nRunning testrunner_jobs_max.py")
os.system('python3 -m pytest Tests/testrunner_jobs_max.py > Tests/Results/Jobs_max.txt')
#Get result from file, print to Shell
temp = subprocess.check_output(['tail', '-1', 'Tests/Results/Jobs_max.txt'])
tempstr = str(temp)
#MUST ESCAPE ' CHARACTER FIRST
tempstr = tempstr.translate(str.maketrans('', '', '\'=b\\'))
tempstr = tempstr[1:len(tempstr)-1]
print(tempstr)

empty_jobs()
empty_students()
print("echo Finished testrunner_jobs.py\n")
'''