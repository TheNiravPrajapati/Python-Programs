# Create String Types 
name1 = 'Nirav'
name2 = "Nirav"
name3 = '''Nirav'''
nameShort = name1[1:4:1]

# print(nameShort)

name = input("Enter Your Name: \n")

print(f"Good Evening: {name}")

letter = '''
    Dear <name>
    You are the Awesome Developer and selected for google 
    and Joining on <date>
'''

print(letter.replace("<name>", name).replace("<date>", '24-10-2025'))
