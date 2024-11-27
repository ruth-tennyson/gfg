# You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

# Note: The answer should be returned in an increasing format.

# Examples:

# Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
# Output: [5, 6]
# Explanation: 5 and 6 occur more n/3 times.
# Input: arr[] = [1, 2, 3, 4, 5]
# Output: []
# Explanation: no candidate occur more than n/3 times.
# Constraint:
# 1 <= arr.size() <= 106
# -109 <= arr[i] <= 109
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n=len(arr)
        temp=[]
        k=0
        com=[]
        for i in range(n):
            if arr[i] not in com:
                count1=0
                for j in range(i,n):
                    if arr[i]==arr[j]:
                        count1=count1+1
                        if count1>n/3 :
                            temp.append(arr[i])
                            k=k+1
                            break
                com.append(arr[i])
                
 
            if k>1:
                break
        temp.sort()
        return temp

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends