#deletion at end
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
def deleteAtTailNode(head,ele):
    curr=head
    if curr==None or curr.next==None:
        return None
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = insertAtBeginning(head, ele)
 
print(linkedlist(head))
head=deleteAtTailNode(head,ele)
print(linkedlist(head))
head=deleteAtTailNode(head,ele)
print(linkedlist(head))


#deletion at beginning
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
def deleteHeadNodeInLinkedList(head):
    if head==None:
        return None
    secondNode=head.next
    head.next=None
    return secondNode
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = insertAtBeginning(head, ele)
 
print(linkedlist(head))
head=deleteHeadNodeInLinkedList(head)
print(linkedlist(head))
head=deleteHeadNodeInLinkedList(head)
print(linkedlist(head))


#delete node at specific position
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
def deleteHeadNodeInLinkedList(head):
    if head==None:
        return None
    secondNode=head.next
    head.next=None
    return secondNode
def deleteNodeAtSpecificPosition(head,position):
    if position==0:   #only one node then it is head
        return deleteHeadNodeInLinkedList(head)
    currentIndex=0
    currentNode=head
    while currentIndex!=position-1:
        currentIndex+=1
        currentNode=currentNode.next
    nodeToBeDeleted=currentNode.next
    currentNode.next=nodeToBeDeleted.next
    nodeToBeDeleted.next
    return head
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = insertAtBeginning(head, ele)
 
print(linkedlist(head))
head=deleteNodeAtSpecificPosition(head,5)
print(linkedlist(head))
head=deleteNodeAtSpecificPosition(head,3)
print(linkedlist(head))