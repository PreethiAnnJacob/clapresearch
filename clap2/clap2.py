'''
CLAPRESEARCH Q2
Your program must generate the N'th Fibonacci number.

It must first take in 't' as the number of test cases and then on the next
't' lines it must take as input a number 'N'. For each such 'N' it must print
the 'N'th Fibonacci number.

For an example input of:

2
5
8

the output must be:

8
34


Take care that no extra things are printed otherwise the solution will be rejected.
'''
count = 2
fibo = [1,2]
ans = []
test = list(map(int,input().split(' ')))
t=test[0]
test.pop(0)
for n in test:
        if n<=count:
                ans.append(fibo[n-1])
        else:
                while(count<n):
                        fibo.append(fibo[count-1] + fibo[count-2])
                        count = count + 1
                ans.append(fibo[n-1]);
for i in ans:
        print(i)
