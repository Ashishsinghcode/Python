# Write a programe to store seven fruits in a list entered by user
arr=[]
a=input("Enter first fruit name")
arr.append(a)
b=input("Enter second fruit name")
arr.append(b)
c=input("Enter third fruit name")
arr.append(c)
d=input("Enter fourth fruit name")
arr.append(d)
e=input("Enter fifth fruit name")
arr.append(e)
f=input("Enter sixth fruit name")
arr.append(f)
g=input("Enter seventh fruit name")
arr.append(g)
print(arr)

# Write a programe to accept marks of 6 students and display them in a sorted manner
arr=[]
a=input("Enter first student marks")
arr.append(a)
b=input("Enter second student marks")
arr.append(b)
c=input("Enter third student marks")
arr.append(c)
d=input("Enter fourth student marks")
arr.append(d)
e=input("Enter fifth student marks")
arr.append(e)
f=input("Enter sixth student marks")
arr.append(f)
arr.sort()
print(arr)

# Check that a tuple cannot be changed in Python
arr=(1,2,3,4,5,6)
arr[2]= 5
print(arr)

# Write a programe for sum of list with four items
arr=[1,2,3,4]
a= arr[0]+arr[1]+arr[2]+arr[3]
print(a)

# Write a programe to count the number of zeros in the folloeing tuple
tup=(7,0,8,0,0,9)
print(tup.count(0))