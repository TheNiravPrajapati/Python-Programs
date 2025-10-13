# 3. For Listing of the Items in Directory 
import os

directory_path = 'D:\Learning\Python'

conents = os.listdir(directory_path)

for item in conents:
    print(item)