print('Hello World')
x=10
y=12.5
z='my name is danyal'
print (x,type(x))
print (y,type(y))
print (z,type(z))
# casting
print ('casting examples')
a=float(x) # convert from integer to float
b=str(y) # convert from integer to string
c=int('10')
print (a,type(a))
print (b,type(b))
print (c,type(c))

a=22
a=str(a)
b='My age  is '
print(b + a)

print('#'* 20)

age=23

print('I am ' + str(age) + ' year old' )

print('#'* 20)

fage=67
mage=55
print('I am ' + str(age) + ' year old ' + ' My mother is ' + str(mage) + ' year old '+ 'My father is ' + str(fage) + ' year old ' )
print('I am %d years old, My mother is %d years old, My father is %d years old, '%(age,mage,fage))

