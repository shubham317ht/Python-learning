#varible can be defined in a linear fashion
x,y = 20,30
    
#string and other datatype can't be concatenated in python
#print('value of x is :'+x) #TypeError: can only concatenate str (not "int") to str

#Have to use comma operator to seperate string and other dataType (like integer, float)
print('value of x is',x,'\nvalue of y is',y)

#two string can be concatenated using the + (plus operator)
print('Shubham '+'Goenka')

#divding the number return a float value
print(9/3) #3.0

#double divide return a integer or floor value
print(9//3) #3

# \n is escape character and has special meaning 
#prints string followed by it to the next line
print(r'c:\windows\newfolder')

print('c:\windows\newfolder')

#print the string as raw or asitis use r followed by the string 
print(r'c:\windows\newfolder')

#another way to do this use the double slash 
print('c:\windows\\newfolder')

#print 10 time the string we passsed
#print(10*' shubham goenka\n')
#print(' shubham goenka\n'*10)

name = "SHUBHAM";
input(name[1:2])

list = ['shubham', 'goenka',80,'heaptrace']

list.append('suraj goenka')
input(list)

list.pop()
input(list)
