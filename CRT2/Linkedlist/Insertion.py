#insertion at tail(empty list)
class Box:
    def __init__(self,data):
        self.data=data
        self.next=None
def linkedlist(curr):
    while curr!=None:
        print(curr.data)
        curr=curr.next
def insertAtTailNode(head,ele):
    temp=Box(ele)
    if head==None:
        return temp
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
head=None
n=[12,32,43,56,75,24,88,85,34,76]
for ele in n:
    head=insertAtTailNode(head,ele)
print(linkedlist(head))

#insertion at beginning(empty list)
class Box:
    def __init__(self,data):
        self.data=data
        self.next=None
def linkedlist(curr):
    while curr!=None:
        print(curr.data,end="---->")
        curr=curr.next
def insertAtBeginning(head,ele):
    temp=Box(ele)
    if head==None:
        return temp
    temp.next=head
    return temp
def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtBeginning(head, ele)
 
    temp = Box(ele)
    currentIndex = 0 
    currentNode = head 
    while currentIndex != position - 1:
        currentIndex += 1 
        currentNode = currentNode.next 
 
    temp.next = currentNode.next 
    currentNode.next = temp 
    return head
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = insertAtBeginning(head, ele)
 
print(linkedlist(head))
head = insertAtSpecificPosition(head, 5, 1899)
print(linkedlist(head))


