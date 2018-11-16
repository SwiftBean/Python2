#Zachary Page
import random
while True:
    name = input("Enter your name: ")
    print(name[0])
    length = len(name)-1
    print(length)
    index_pos = random.randrange(0,length)
    if index_pos <= length:
        char = name[index_pos]
        print(char)
    else:
        print("That's out of the range")
    continue
