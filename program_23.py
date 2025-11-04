''''
Write in File with (With Statement)
'''

f = open("Files/file3.txt")
print(f.read())
f.close()

# In This You dont need to Close the File, this will close the file automatically
with open("Files/file3.txt") as f:
    print(f.read())