word= input("enter a five letter word like pizza")

print("Enter the beginning and ending index for your slice")
start = None
while start != "":
    start = (input("\nStart: "))

    if start:
        start = int(start)
        finish = int(input("Finish: "))
        print("word[", start, ":", finish, "] is", end = "")

        print(word[start:finish])

input("\n\nPress the enter key to exit.")
