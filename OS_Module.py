import os
import time
'''cwd means current working directory'''
curDir = os.getcwd()

print(curDir)

os.mkdir('newDir')

time.sleep(2)

os.rename('newDir', 'newDir2')
time.sleep(2)

os.rmdir('newDir2')
