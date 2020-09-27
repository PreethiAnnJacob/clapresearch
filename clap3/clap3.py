'''Your program must find the sum of the matrix produced by calculating the
Hadamard product of two matrices of arbitrary size.

First the program must take 't' as input, denoting the number of test cases.
Then for each test case it must take in a number 'N', denoting the size of the
square matrix to be processed.  The next N lines each contain N space separated
numbers, denoting the first matrix. The next N lines each contain N space
separated numbers, denoting the second matrix.

For each test case you must print the sum of the matrix produced by calculating
the Hadamard product of two matrices of arbitrary size.

For an example input of:

2
3
1 1 1.5
2 2 2
3 3 3.5
3 3 3
4 4 4
5 5 5.5
2
3 3
4 5
6 7
8 9

the output must be:

84
116


Take care that no extra things are printed otherwise the solution will be rejected.
'''

t=int(input())
a=[]
b=[]
sum=[]
for k in range(t):
    n=int(input())
    for i in range(n):
        a.append(float(int()) for j in input().split())
    for i in range(n):
        b.append(float(int()) for j in input().split())
    for i  in range(n):
        for j in range(n):
            sum.append(float(a[i][j])*float(b[i][j]))
for i in range(t):
    print(sum[i])
    
//Got Error
