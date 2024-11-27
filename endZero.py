# Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.

# Examples:

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.
# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.
# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 105

class Solution:
    def pushZerosToEnd(self,arr):
        n=len(arr)
        a=[]
        for i in arr:
            if i!=0:
                a.append(i)
        m=len(a)
        for k in range(m,n):
            a.append(0)
        for i in range(n):
            arr[i]=a[i]
    	                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends