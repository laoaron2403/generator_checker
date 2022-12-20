import subprocess
import time
import sys
import os

# Check Command Line Arguments
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('Usage: python run.py solution_executable [suffix_for_solution_file]')
    quit()

if os.path.exists('testcase') == False:
    print("Folder 'testcase' does not exist!")
    quit()

if os.path.isdir('testcase') == False:
    print("'testcase' is not a folder!")
    quit()

for filename in os.listdir('testcase'):
    # Only consider files with '.in' extension
    if len(filename) < 3 or filename[-3:] != '.in':
        continue

    print(f'Generate answer file for {filename}...')
    # Let the input file have the ".in" extension
    input_path = os.path.join(".","testcase",filename)

    # Custom File Suffix: check if the user wants to have different suffix for the answer files
    if len(sys.argv) == 3: 
        # Use the thrid argument as the suffix to the file
        # Then change the extension to ".sol"
        output_path = os.path.join(".","testcase",filename[:-3]+sys.argv[2]+".sol")
    else:
        # Default option:
        # Let the output file have the same name but with ".sol" extension
        output_path = os.path.join(".","testcase",filename[:-3]+".sol")

    # run the command line "./solution <input_file >output_file"
    subprocess.run([sys.argv[1], '<'+input_path, '>'+output_path], shell=True)

print('The program runs and terminate successfully')