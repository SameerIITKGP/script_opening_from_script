import os
import sys
from subprocess import call
print "File file.py is running."
call([sys.executable, 'run_file.py'])
#os.system("/home/Documents/fuzzy_logic/testing/Script_opening_from_script/dist/run_file/run_file.exe")
print "File file.py is still running."
