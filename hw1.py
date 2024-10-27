number = {
    1:'apple',
    2:'bannana',
    3:'orange'
}

# access items
i = number[2]
print(i)
# get keys
b = number.keys()
print(b)
#get values
c = number.values()
print(c)
#list of key value pairs
number.items()
print(number)
# if key exists in dictionary
if 5 in number:
    print("Yes")
else:
    print("No")
#changing values
number.update({3:"pear"})
print(number)
#add a key value pair
number[4] = "watermelon"
print(number)
#delete key value pair
number.pop(2)
print(number)
#loop through values in dictionaries
for x in number.values():
    print(x)