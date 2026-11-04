word = input("Enter your word: ")
character = input("Enter your character: ")

count = 0

for i in word:
    if i == character:
        count = count+1

print(count)