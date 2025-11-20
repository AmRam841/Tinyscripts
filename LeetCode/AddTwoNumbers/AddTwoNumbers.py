class Solution:
    def addTwoNumbers(self, l1, l2):
        # Traverse l1 to build a list of digits
        current = l1
        list1 = []
        while current is not None:
            list1.append(current.val)
            current = current.next

        # Traverse l2 to build a list of digits
        current2 = l2
        list2 = []
        while current2 is not None:
            list2.append(current2.val)
            current2 = current2.next

        # Reverse the lists to build numbers
        la = list1[::-1]
        lb = list2[::-1]

        # Convert to strings, then to integers
        finallist = ''.join(map(str, la))
        finallist2 = ''.join(map(str, lb))
        FinalList = int(finallist) + int(finallist2)

        # Convert sum back to a list of digits
        ListToNodes = list(str(FinalList))
        ListToNodesRev = ListToNodes[::-1]
        # Build the resulting linked list
        head1 = None
        current3 = None
        for value in ListToNodesRev:
            newnode = ListNode(int(value))
            if head1 is None:
                head1 = current3 = newnode
            else:
                current3.next = newnode
                current3 = newnode

        # Return the head of the new linked list
        return head1