p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter the Message: ")

if((p1.lower() in message.lower()) or (p2.lower() in message.lower()) or (p3.lower() in message.lower()) or (p4.lower() in message.lower())):
    print("This is the Scam, Stay Alert")
else:
    print("This is the Verified message")