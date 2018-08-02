# Runscript for multiple test
## Usage:
python performTests.py -p p1 p2 p3 ... pG -k 1000 -n 10000 -a 0.1.
- p: p-values for each of the group (including the unprotected group), which should sum upto 1
- k: size of the ranking to be generated
- n: number of the rankings to be tested
- a: significance level
- example) p = [0.5, 0.4, 0.1], k = 100, n = 1000, a = 0.1, then python performTests.py -p 0.5 0.4 0.1 -k 100 -n 1000 -a 0.1

After the script is run, it generates a .csv file, which contains the "slow" result of the single test in a folder /singleTest_multinom. 
The folder will be autonatically created if it does not exist.
The p-values, n, alpha and the result of the multiple tests will be shown by the name of the file.
