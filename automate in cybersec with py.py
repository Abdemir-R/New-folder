#example of opening text file in python
with open("login_attempt.txt", "r") as file: #if in directory use directory instead /home/analyst/file
    file_text = file.read()
print(file_text) #print from text outputs 

with open("login_attempt.txt", "r") as file: #if in directory use directory instead /home/analyst/file
    file_text = file.read()
print(file_text.split()) #splits into a list with commas.
usernames = file.text.split() #save list under new variable run code again if added later. now list can be used in other code



# Assign `import_file` to the name of the text file that contains the security log file
import_file = "login.txt"
# The `with` statement
# Use `open()` to import security log file and store it as a string
with open(import_file, "r") as file:
  # Use `.read()` to read the imported file and store the result in a variable named `text`
  text = file.read()
# Display the contents of `text`
print(text)



# Assign `import_file` to the name of the text file that contains the security log file
import_file = "login.txt"
# Assign `missing entry` to a log that was not recorded in the log file
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"
# Use `open()` to import security log file and store it as a string
# Pass in "a" as the second parameter to indicate that the file is being opened for appending purposes
with open(import_file, "a") as file:
    # Use `.write()` to append `missing_entry` to the log file
    file.write(missing_entry)
# Use `open()` with the parameter "r" to open the security log file for reading purposes
with open(import_file, "r") as file:
    # Use `.read()` to read in the contents of the log file and store in a variable named `text`
    text = file.read()
# Display the contents of `text`
print(text)


with open("login_attemtps.txt", "r") as file:
    file_text = file.read()
username = file_text.split()
#create function that countrs a users failed login attempts
def login_check(login_list, current_user):
    counter = 0
    for i in login_list:
        if  1 == current_user:
            counter = counter + 1
    if counter >= 3:
        return "you have tried to login three or more times, account locked"
    else:
        return "you can log in!"
login_check(usernames, "elarson") #displays user can login. 



 
 # Define a function named `update_file` that takes in two parameters: `import_file` and `remove_list`
# and combines the steps you've written in this lab leading up to this
def update_file(import_file, remove_list):
  # Build `with` statement to read in the initial contents of the file
  with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
    ip_addresses = file.read()
  # Use `.split()` to convert `ip_addresses` from a string to a list
  ip_addresses = ip_addresses.split()
  # Build iterative statement
  # Name loop variable `element`
  # Loop through `ip_addresses`
  for element in ip_addresses:
    # Build conditional statement
    # If current element is in `remove_list`,
    if element in remove_list:
      # then current element should be removed from `ip_addresses`
      ip_addresses.remove(element)
  # Convert `ip_addresses` back to a string so that it can be written into the text file 
  ip_addresses = " ".join(ip_addresses)       
  # Build `with` statement to rewrite the original file
  with open(import_file, "w") as file:
    # Rewrite the file, replacing its contents with `ip_addresses`
    file.write(ip_addresses)
# Call `update_file()` and pass in "allow_list.txt" and a list of IP addresses to be removed
update_file("allow_list.txt", ["192.168.25.60"])
# Build `with` statement to read in the updated file
with open("allow_list.txt", "r") as file:
  # Read in the updated file and store the contents in `text`
  text = file.read()
# Display the contents of `text`
print(text)

