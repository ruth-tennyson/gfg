# Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

# Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

# Examples:

# Input: arr = [2, 4, 1, 7, 5, 0]
# Output: [2, 4, 5, 0, 1, 7]
# Explanation: The next permutation of the given array is {2, 4, 5, 0, 1, 7}.
# Input: arr = [3, 2, 1]
# Output: [1, 2, 3]
# Explanation: As arr[] is the last permutation, the next permutation is the lowest one.
# Input: arr = [3, 4, 2, 5, 1]
# Output: [3, 4, 5, 1, 2]
# Explanation: The next permutation of the given array is {3, 4, 5, 1, 2}.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 105

class Solution:
    def nextPermutation(self, arr):
        # code here
        n=len(arr)
        temp=[]
        j=0
        pivot=0
        for i in range(n-1,0,-1):
            if arr[i]>arr[i-1]:
                pivot=arr[i-1]
                j=i
                break
        low=j
        for i in range(j+1,n):
            if arr[i]>pivot and arr[i]<arr[low]:
                low=i
        temp=arr[j-1]
        arr[j-1]=arr[low]
        arr[low]=temp
        k=n-1
        for i in range(j,j+int((n-j)/2)):
            temp=arr[i]
            arr[i]=arr[k]
            arr[k]=temp
            k=k-1
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends