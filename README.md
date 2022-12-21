# Test Case Answer Generation Helper & Checker

Suppose you want to run an executable file "program.o" with its input being stored in a file "input1.in". Then, you want to store the output of the execution into the file "output1.out".

You would normally execute something like the following command
```shell
./program < input1.in > output1.out
```
Now, what if we want to do this on ten different input files? or maybe 100?

And what if you have "program2.o" that you want to compare its outputs with program1's outputs?

This is what happen in *testcase preparation* in Competitive Programming.
Competitive Programming applies the concept of [Zero Knowledge Proof](https://en.wikipedia.org/wiki/Zero-knowledge_proof) to judge correctness of a program.

The contest creator will prepares a lot of "inputs" and corresponding "correct output". These are known as "testcases". If our submitted program give correct output for each corresponding prepared input, then our program will be considered correct.
But, as we already see, it can be a very tedious task.

This repository provides you python scripts for helping generating answer files ("correct output") for your testcases, and compare answers from two different programs. You can see the example below.

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
- **Solution Program** = the name of executable file of your solution program. This will be later used inside the script for running `./{solution program} <{input_file} >{output_file}`
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

In this repository, we have testdata files (in the "testcase" folder) and solution source codes ("solution.cpp" and "wrong_solution.cpp") ready.
The problem whom the solutions try to solve is "Receive 2 32-bit integers and output the multiplication of them".
Each of the input file ("1.in", "a_big_testcase.in", "my_second_test.in") contains 2 two integers separated by a space
Both of the program receive 2 integers and then output the multiplication of them, except that "wrong_solution.cpp" uses "int" datatype to contain the result, which causes overflow.

1. Compile the solution source codes.
```shell
g++ solution.cpp -o solution
g++ wrong_solution.cpp -o wrong_solution
```
2. Run `run.py` the generate answer files for `solution`. After this, the files "1.sol", "a_big_testcase.sol", "my_second_test.sol" will be generated.
```shell
python run.py solution
```
3. Run `run.py` the generate answer files for `wrong_solution` **with suffix "_wrong"**. After this, the files "1_wrong.sol", "a_big_testcase_wrong.sol", "my_second_test_wrong.sol" will be generated.
```shell
python run.py wrong_solution _wrong
```
4. Run `checker.py` to check if the two programs produce the same result, by comparing testdata with suffix "_wrong" with the ones without suffix
```shell
python checker.py _wrong
```
You will receive the following output
```
Comparing answer files between 1_wrong.sol and 1.sol...
Testcase 1_wrong.sol is ok
Comparing answer files between a_big_testcase_wrong.sol and a_big_testcase.sol...
Testcase a_big_testcase_wrong.sol is not ok. 1808348672 vs 999999999000000000
Comparing answer files between my_second_test_wrong.sol and my_second_test.sol...
Testcase my_second_test_wrong.sol is ok
The program runs and terminate successfully
```
You can see that the outputs of both programs differ when run against the input inside `a_big_testcase.in`. The result identifies that both program different, and the input that both works differently on.
