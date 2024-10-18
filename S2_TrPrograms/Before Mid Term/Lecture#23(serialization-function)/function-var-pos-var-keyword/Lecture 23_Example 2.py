#Lecture 15 - Example 3

# Scope of variables - Example 1
global_var1 = 3000
global_var2 = 2000

def test_to_swap(local_var1, local_var2):
     def swap(local_var1,local_var2):
               temp_var = local_var1
               local_var1 = local_var2
               local_var2 = temp_var
               print("Swapping done! local_var1 is now " + str(local_var1) + " and local_var2 is now " + str(local_var2))
     def no_swap():
          #print("No swapping as " + str(global_var1) + " is greater than " + str(global_var2))
          print("No swapping as " + str(local_var1) + " is greater than " + str(local_var2))
     if (local_var1 <= local_var2):
          swap(local_var1,local_var2)
     else:
          no_swap()

# Calling the functions

test_to_swap(global_var1, global_var2)
print()

