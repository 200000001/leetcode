class Solution:
    def confusingNumber(self, n: int) -> bool:
        a = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        
        
        
        b = []
        
        str_n = str(n)
        
        for c in reversed(S):
            if c not in a:
                return False
            b.append(a[c])
        
        
        return False if ''.join(b) == str_n else True
    
    
# leetcode 1056번 문제
