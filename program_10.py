a = int(input("Enter Your Age: "))
# if elif else Ladder
if(a >= 18):
    print("You Can Drive Your Vehicles")
elif(a < 0):
    print("You can not Enter the Invalid Age")
elif(a == 0):
    print("You can not Enter 0 In Age")
else:
    print("You Can not Drive")