class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
            
        odd = []
        even = []
        curr = head
        index = 1

        while curr:
            if index % 2 == 1:
                odd.append(curr)
            else:
                even.append(curr)
            curr = curr.next
            index += 1

        for i in range(len(odd) - 1):
            odd[i].next = odd[i + 1]

        for i in range(len(even) - 1):
            even[i].next = even[i + 1]

        if even:
            odd[-1].next = even[0]
            even[-1].next = None
        else:
            odd[-1].next = None
        return odd[0]

values = list(map(int, input("Enter elements: ").split()))
head = ListNode(values[0])
curr = head

for x in values[1:]:
    curr.next = ListNode(x)
    curr = curr.next

sol = Solution()
newHead = sol.oddEvenList(head)

print("Output:", end=" ")
curr = newHead
while curr:
    print(curr.val, end=" ")
    curr = curr.next