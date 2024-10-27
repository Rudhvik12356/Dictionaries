grades = {

}

grades["bob"] = 35
grades['rudhvik'] = 12
print(grades)
for i in grades.values():
    print(i)
print(grades.get("bob"))
if "bob" in grades:
    print("Yes")
else:
    print("No")     
grades.pop("rudhvik")          
print(grades)