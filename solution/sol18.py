# WAS to enter 5 string in list and print those string whos lenth is Even number
def createlist():
    l=[]
    for i in range(5):
        a=input("Enter string:")
        l.append(a)
    return(l)
a=createlist()
for i in a:
    print(i)



