'''no.of vowels in a string
s=input().strip()
vowels="aeiou"
count=0
for char in s:
    if char in vowels:
        count+=1
print(count)
'''

''''
#max occurred character in a string
s=input().strip()
char={}   #dictionary
for c in s: 
    if c in char:  #checking character in dictionary and incrementing count
        char[c]+=1  
    else:           #count is same if character is unique
        char[c]=1
count=0
character=''
for c in sorted(char.keys()):  #keys-characters
    if char[c]>count:
        count=char[c]          #count of char in dictionary
        character=c            
print(character)
'''
    
class Box:
    def __init__(self,data):
        self.data=data
        self.next=None
#block creation
o1=Box(51)
o2=Box(52)
o3=Box(53)
o4=Box(54)
o5=Box(55)
o1.next=o2
o2.next=o3
o3.next=o4
o4.next=o5
o5.next=None
print(o1.data)

