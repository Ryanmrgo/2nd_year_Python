# CSE 2040 - Lecture 14 - Example 4
# Example illustrating sub lists and sub tuples

print()
# Tuple to store userID and password
userID_password = (("user_id1","aaaa"),("user_id2","bbbb"),("user_id3","cccc"))

# List to store other details
user_other_details = [["Jack",[12,12,2000],"Public"],["Jill",[9,8,2002],"Public"],["Tom",[1,3,2000],"Private"]]

# Tuple - Values at index 1
print("Tuple - At Index 1:")
print()
print(userID_password[1])

# Tuple - Values at index 2,1
print()
print("Tuple - At Index 2,1:")
print(userID_password[2][1])

# List - Values at index 2
print()
print("List - At Index 2:")
print(user_other_details[2])

# List - Values at index 2,1
print()
print("List - At Index 2,1:")
print(user_other_details[2][1])

# List - Values at index 2,1,2
print()
print("List - At Index 2,1,2:")
print(user_other_details[2][1][2])
print()

print()
print()
