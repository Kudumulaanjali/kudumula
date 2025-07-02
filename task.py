# 1.  create a dictionary from two lists:
# a.  keys =['id','name','age']
# b.  values=[101,'jyo',23]
keys=['id','name','age']
values=[101,'jyo',23]
res=dict(zip(keys,values))
print(res)

#output:- {'id':101,'name':'jyo','age':23}

# 2.  create a dictionary to store  student name and age:
s={}
name=input("enter student name:")
roll_no=int(input("enter student roll no:"))
age=int(input("enter student age:"))

s[name]=roll_no,age
print(s)



# 3. create an empty dictionary and add key-value pairs one by one:
d={}
d['name']=input("enter your name:")
d['age']=int(input("enter your age:"))
d['city']=input("enter your city:")
d['pin']=int(input("enter your pin:"))
print(d)


# get the value of key "salary" from this dictionary:
# ex:employee={'name':'jyo','age':30,'salary':30000}
employee={'name':'jyo','age':30,'salary':30000}
print(employee['salary'])

#output:-30000

# remove the last inserted key-value pair from the dictionary using an appropriate method:
k={'name':'anjali','pin':101,'city':'hyd','mobile':7019834627}
emp=k.popitem()
print(k)

#define packing and unpacking in python.also,provide one example for both packing and unpacking:
#example of packing:-
x=1,2,3
print(x)

# output:-(1,2,3)

# example of unpacking:-
h=[10,20,30]
a,b,c=h
print(a)
print(b)
print(c)

# output:- 10
           #20
           #30