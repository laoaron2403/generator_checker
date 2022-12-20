# Test Case Answer Generation Helper & Checker

Python scripts for helping generating answer files for your testcases, and compare answers from two different programs.

## Requirements

- The solution program must be in the same folder as the script
- Have the folder "testcase" in the same directory as the script
- Inside the folder "testcase", contains all the testdata files
- The testdata files must have ".in" extension
- The answer files will have ".sol" extension

## Usage

### Answer Generation

Run `run.py` with the following command line arguments
```shell
python run.py {solution program} [suffix for answer files]
```
- **Solution Program** = the executable file of your solution program. This will be later used inside the script for running `./{solution program} <{input_file} >{output_file}`
- **suffix for answer files** (optional) = appending a specified suffix to the answer files. Useful for generating answers from different programs and comparing between them.

For example, if the testdata file is named "1.in", then the output file will be named "1.sol", or "1_bruteforce.sol" if the *suffix for answer files* is specified as "_bruteforce"

### Checking Answers between different programs

Run `checker.py` with the following command line arguments
```shell
python checker.py {the first suffix} [the second suffix]
```
- **The first suffix** = Specified the files with that suffix to be compared
- **The second suffix** (Optional) = Specified the files with that suffix to be compared with the files in previous option. If this is not specified, the files with the first-prefix erased from its name will be used.

## Example

In this demo, we have testdata files and solution source codes ready.
1. Compile the solution source codes
```shell
g++ solution.cpp -o solution
g++ wrong_solution.cpp -o wrong_solution
```
2. Run `run.py` the generate answer files for `solution`. After this, the files "1.sol", "a_big_testcase.sol", "my_second_test.sol" will be generated.
```shell
python run.py solution
```
2. Run `run.py` the generate answer files for `wrong_solution` **with suffix "_wrong"**. After this, the files "1_wrong.sol", "a_big_testcase_wrong.sol", "my_second_test_wrong.sol" will be generated.
```shell
python run.py wrong_solution _wrong
```
3. Run `checker.py` to check if the two programs produce the same result, by comparing testdata with suffix "_wrong" with the ones without suffix
```shell
python checker.py _wrong
```
