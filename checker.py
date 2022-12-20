import subprocess
import time
import sys
import os

# Check Command Line Arguments
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('Usage: python checker.py suffix1 [suffix2]')
    quit()

if os.path.exists('testcase') == False:
    print("Folder 'testcase' does not exist!")
    quit()

if os.path.isdir('testcase') == False:
    print("'testcase' is not a folder!")
    quit()

# Get the length of the first argument: the suffix1
suffix1_len = len(sys.argv[1])

for filename in os.listdir('testcase'):
    # Only consider files with '.in' extension
    if len(filename) < 4+suffix1_len or filename[-4-suffix1_len:] != sys.argv[1]+'.sol':
        continue

    # Check if we want to compare the suffix file against 
    # 1) default suffix
    # 2) the specified suffix
    if len(sys.argv) == 2:
        # Compare with a default suffix
        against_name = filename[:-4-suffix1_len]+'.sol'
    else:
        # Compare with a default suffix
        against_name = filename[:-4-suffix1_len]+sys.argv[2]+'.sol'

    print(f'Comparing answer files between {filename} and {against_name}...')

    # Check if the other answer file exists
    if os.path.exists(os.path.join('.','testcase',against_name)) == False:
        print(f'{against_name} does not exist!')
        continue

    filepath1 = os.path.join('.','testcase',filename)
    filepath2 = os.path.join('.','testcase',against_name)
    f1 = open(filepath1)
    f2 = open(filepath2)
    x = f1.read().strip()
    y = f2.read().strip()
    if x == y:
        print('Testcase {} is ok'.format(filename))
    else:
        print('Testcase {} is not ok. {} vs {}'.format(filename,x,y))
    f1.close()
    f2.close()

print('The program runs and terminate successfully')