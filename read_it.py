print("\nReading characters from the file.")
text_file = open("C:\\Users\\zachary.page\\Desktop\\File Examples\\read_it.txt", "r")
print(text_file.read(1))
text_file.close()

print("\nReading the entire file at once.")
text_file = open("C:\\Users\\zachary.page\\Desktop\\File Examples\\read_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("\nReading characters from a line.")
text_file = open("C:\\Users\\zachary.page\\Desktop\\File Examples\\read_it.txt", "r")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print("\nReading one line at a time")
text_file = open("C:\\Users\\zachary.page\\Desktop\\File Examples\\read_it.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nReading the entire file into a list.")
text_file = open("C:\\Users\\zachary.page\\Desktop\\File Examples\\read_it.txt", "r")
lines = text_file.readlines()
print(lines)
text_file.close()


































