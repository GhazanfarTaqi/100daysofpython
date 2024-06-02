name = "ghazanfar"
# We can use "" in string by using escape characters.
line = "I want,\" to eat an Apple\" "

print(name, line)
# We can create multi line strings as follows 
multist = '''
This is multiline
string.
'''
print(multist)

# We can print indiviual characters of string using indexes
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
# print(name[9]) #This will throw an error

# We can loop through string using for loop as follows
print("Using For Loop")
for charac in name:
    print(charac)
for charac in multist:
    print(charac)