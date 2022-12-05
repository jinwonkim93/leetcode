from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        self_node = self
        other_node = other
        while self_node:
            if other_node is None:
                return False

            if self_node.val != other_node.val:
                return False
            self_node = self_node.next
            other_node = other_node.next
        return True


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        node = head
        while node:
            node_list.append(node)
            node = node.next
        n = len(node_list)
        middle = n//2
        return node_list[middle]

def list_to_node(nums):
    root = ListNode(nums[0])
    cur_node = root
    for i in range(1, len(nums)):
        cur_node.next = ListNode(nums[i])
        cur_node = cur_node.next
    return root
    
head1 = list_to_node([1,2,3,4,5])
head2 = list_to_node([1,2,3,4,5,6])
solution = Solution()
assert solution.middleNode(head1) == list_to_node([3,4,5]), "Example1"
assert solution.middleNode(head2) == list_to_node([4,5,6]), "Example2"