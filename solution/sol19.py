#Creater 2 list of student and address which contain name of student and there address and print student name with his addresss
def output():
    o=[]
def student():
    l=[]
    for i in range(3):
        a=input("Enter name:")
        l.append(a)
    return(l)
a=student()
print(a)

def address():
    c=[]
    for j in range(3):
        b=input("Enter address:")
        c.append(b)
    return(c)
b=address()
print(b)
for  m in range(3):
    o=print('{}-->{}'.format(student,address))
    output()
