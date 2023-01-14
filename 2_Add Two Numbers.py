class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        num = dummy
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = l1.val if l1 else 0
            val2  = l2.val if l2 else 0
            
            add_val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
                      
            num.next = ListNode(add_val)
            num = num.next                      
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
               
        return dummy.next
        
        
        
 # https://leetcode.com/problems/add-two-numbers/
