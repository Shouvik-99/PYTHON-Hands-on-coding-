"""

Input Format

The first line contains an integer
the total number of country stamps.
The next

lines contains the name of the country where the stamp is from.

Constraints

Output Format

Output the total number of distinct country stamps on a single line.

Sample Input

7
UK
China
USA
France
New Zealand
UK
France

Sample Output

5
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import time
from collections import defaultdict
s = set()
t1=time.time()
for _ in range(0,int(input())):
    s.add(input())
print(len(s)) #length of set
t2=time.time()
print(t2-t1)

d=defaultdict(int)
t1=time.time()
for i in range(0,int(input())):
    d[i]+=1
print(len(d)) #length of dictionary
t2=time.time()
print(t2-t1)

'''
    A different approach using dictionary as a set
        tc==>O(n)
    For both method
    Here the O/P with running time with both method.
    
7
UK
China
USA
France
New Zealand
UK
France
5
2.095736503601074

7
UK
China
USA
France
New Zealand
UK
France
7
2.3257291316986084

'''
