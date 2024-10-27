import string

alaphabetCount = {}

for i in string.ascii_lowercase:
    alaphabetCount[i] = False
    
print(alaphabetCount)
message = input("Enter your message: ").lower()   

for a in message:
    if a in alaphabetCount:
        alaphabetCount[a] = True
        
print(all(alaphabetCount.values()))
if all(alaphabetCount.values()):
    print("Its a pangram")
else:
    print("It is not a pangram")    
print(alaphabetCount.keys()) 
alaphabetCount.clear()   
print(alaphabetCount)    