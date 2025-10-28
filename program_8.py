marks = {
    "Nirav": 100,
    "Rohan": 50,
    "Mohan": 23,
}

# print(marks, type[marks])

print(marks["Nirav"])

# Methods 

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Nirav": 99})
print("Marks of Nirav:", marks.get("Nirav"))