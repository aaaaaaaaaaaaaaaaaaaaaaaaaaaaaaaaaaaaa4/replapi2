import replapi2
username = input("Enter your username here: > ")
print("You have " + str(replapi2.UserInfo(username).replit_cycles()) + " cycles")