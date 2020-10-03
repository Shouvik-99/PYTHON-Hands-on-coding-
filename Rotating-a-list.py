'''

Input Format

The first line contains two space-separated integers
and , the size of and the number of left rotations you must perform.
The second line contains space-separated integers


Output Format

Print a single line of
space-separated integers denoting the final state of the array after performing
left rotations.


Sample Input

5 4
1 2 3 4 5


Sample Output

5 1 2 3 4

'''
import time
#if __name__ == '__main__':
'''
nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))
'''
    
    
    
n,s=map(int,input().split())       # Using input format,in short manner
arr=list(map(int,input().split())) # better understandable also
t1=time.time()
def rotLeft(a, num):
    length = len(a)
    b = []
    if(num > length):
        num = num % length
    b = a[num:length] + a[0:num]
    return b
result = rotLeft(arr, s)
print(' '.join(map(str, result)))
t2=time.time()
print(t2-t1)


t3=time.time()
mod_arr=[0]*n
for i in range(n):
    ind=(i-s)%n
    mod_arr[ind]=arr[i]
print(*mod_arr)
t4=time.time()
print(t4-t3)

'''
O/P==>
5 4
1 2 3 4 5
5 1 2 3 4
0.002243518829345703
5 1 2 3 4
0.008288145065307617

Time complexity same O(n),
Using pyhton bidirectional indexing.
'''
