def list_op():
    l1=input("Enter a list : ")
    s=list(map(int,l1.split()))
    l2=sorted(s)
    l3=list(reversed(s))

    print("Original List : ",s)
    print("Sorted List : ",l2)
    print("reverse list : ",l3)

def dictionary_op():
    d1={'name':'Aniket','rollno':17,'class':"Fy",'branch':'computer Science'}
    d2={'sname':'Chirag','rollno':28,'class':"Fy",'sbranch':'computer Science'}

    keys1,keys2=d1.keys(), d2.keys() 
    ckey=keys1 & keys2
    d1.update(d2)

    print("Merged Dictionary is :",d1)
    print("Common keys are",ckey)


# dictionary_op()
# list_op()