# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
# My Solution - DFS

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        arr = set()
        x = ''
        def solve(N, K, arr, x, val):
            if len(x) >= N:
                if x not in arr:
                    arr.add(x)
                # Resetting x to empty string
                x = ''
                return
            
            x += str(val)
            # temp - stores the last digit of x
            temp = int(x[-1])
            
            # If the number that we get on adding K to temp is less than 10, then it is VALID.
            # So append that number to x
            if temp + K < 10:
                solve(N, K, arr, x, temp+K)
            
            # If the number that we get on subtracting K from temp is between 0 and 10, then it is VALID.
            # So append that number to x
            if temp - K in range(0,10):
                solve(N, K, arr, x, temp - K)
        
        # Base case: when N == 1 and K is anything
        if N == 1:
            return [x for x in range(10)]
       
        for i in range(1,10):
            solve(N, K, arr, x, str(i))
       
        return sorted(arr)

    
    # Method - 2 | BFS Solution
    '''
    We initial the current result with all 1-digit numbers, like cur = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

    Each turn, for each x in cur,
    we get its last digit y = x % 10.
    If y + K < 10, we add x * 10 + y + K to the new list.
    If y - K >= 0, we add x * 10 + y - K to the new list.

    We repeat this step N - 1 times and return the final result.
    '''
    
    
    class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        nums = range(10)
    
        for i in range(N-1):
            nums = {x * 10 + y for x in nums for y in [x % 10 + K, x % 10 - K] if x and y in range(0,10)}
        return nums
    
