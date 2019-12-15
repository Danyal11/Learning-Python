# How to define a list 
mylist = []
print(mylist, type (mylist))
# defining list 2nd method
second_list = list()
print(second_list, type (second_list))

xlist = ['danyal',  23, 23.5, '!']
print(xlist)


for x in xlist:
	print(x, type(x))
print(len(xlist))

print('#' *20)

i=len(xlist);

while(i > 0):
	print(xlist[i-1], type(xlist[i-1]))
	i-=1
print('#' *20)
	
even_list=[]
odd_list=[]

a=1

while a<=100:
	if a%2==0:
		even_list.append(a)
	else:
		odd_list.append(a)
	a+=1
print('Even list = %s'%even_list)
print('Odd list = %s'%odd_list)


print('#' *20)

new_list = ['danyal', 'ahmad', '1','2','3']

for index,item in enumerate (new_list):
	print(index,item)

#mylist.append(4)
#mylist.append(5)
#mylist.append(6)
# print(mylist[0]) # prints 1
# print(mylist[1]) # prints 2
# print(mylist[2]) # prints 3

# # prints out 1,2,3
# for x in mylist:
#     print(x)
    	


# print('#' *20)

print('#' * 20)

for x in range(100):
	if x%2==0:
		print('%d is even ' %x)
	else:
		print('%d is odd' %x)

