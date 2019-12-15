def my_function():
    print("Hello From My Function!")
def greetings(name='kamal'):
	print('Hello %s' %name)
	return 5
	
print("x" * 50)

def greetings2(name1):
	print('Hello %s' %name1)
	return 10	

my_function()
output=greetings()
output1=greetings2(1234)
print(output) # this will reurn 5 because we have return 5 in greeting function


print("x" * 50)

def greetings3(name:str)->int:
	print('Hello %s' %name)
	return 'danyal'


output = greetings3(1234)
print(output, type(output))

print("x" * 50)

def iseven(x):
	if x%2==0:
		return True
	else:
		return False


for x in range(25):
	if iseven(x):
		print(x)