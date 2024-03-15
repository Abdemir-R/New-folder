#define a function
def greet_employee():
    print("welcome!")
#call a function
greet_employee()

# Define a function named `alert()`
def alert(): 
    for i in range(3):
        print("Potential security issue. Investigate further.")
# Call the `alert()` function. will show alert message 3 times.
alert()

# Define a function named `list_to_string()`
def list_to_string():
  # Store the list of approved usernames in a variable named `username_list`
  username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
  # Write a for loop that iterates through the elements of `username_list` and displays each element
  for i in username_list:
    print(i)
# Call the `list_to_string()` function
list_to_string()


# Define a function named `list_to_string()`
def list_to_string():
  # Store the list of approved usernames in a variable named `username_list`
  username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
  # Assign `sum_variable` to an empty string
  sum_variable = ""
  # Write a for loop that iterates through the elements of `username_list` and displays each element
  for i in username_list:
    sum_variable = sum_variable + i + ", "
  # Display the value of `sum_variable`
  print(sum_variable)
# Call the `list_to_string()` function
list_to_string() #will print names with commans


# greet employees by name
def greet_employee(name):
   print("welcome!", name)
def greet_employee(firstname, lastname):
   print("welcome", firstname, lastname)
greet_employee("kim", "sim")


#return information from a function
def calculate_fails(total_attempts, failed_attempts):
   fail_percentage = failed_attempts / total_attempts
   return fail_percentage
#user has logged in 4 times with 2 failed attempts
percentage = calculate_fails(4,2)
if (percentage >= .5):
   print("account locked")


#explore max
a = 3
b = 9
c = 5
print(max(3,9,5))

#use the sorted function, sorts in alphabetical order
usernames= ["sim", "bom", "lisp", "jill"]
print(sorted(usernames))


#simple function with stored variable
month = "september"
print("investigate", month, "if more than", 100) #will display whole message


# Define a function named `analyze_logins()` that takes in two parameters, `username` and `current_day_logins`  
def analyze_logins(username, current_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)
analyze_logins("jill", 9) #call the function


# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)
    # Display a message about average number of login attempts the user has made that day 
    print("Average logins per day for", username, "is", average_day_logins)
# Call `analyze_logins()` 
analyze_logins("ejones", 9, 3)


# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)
    # Display a message about average number of login attempts the user has made that day 
    print("Average logins per day for", username, "is", average_day_logins)
    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
    login_ratio = current_day_logins / average_day_logins
    # Display a message about the ratio
    print(username, "logged in", login_ratio, "times as much as they do on an average day.")
# Call `analyze_logins()` 
analyze_logins("ejones", 9, 3)


# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)
    # Display a message about average number of login attempts the user has made that day 
    print("Average logins per day for", username, "is", average_day_logins)
    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
    login_ratio = current_day_logins / average_day_logins
    # Return the ratio
    return login_ratio
# Call `analyze_logins() and store the output in a variable named `login_analysis` 
login_analysis = analyze_logins("ejones", 9, 3)
# Display a message about the `login_analysis`
print("ejones", "logged in", login_analysis, "times as much as they do on an average day.")


# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)
    # Display a message about average number of login attempts the user has made that day 
    print("Average logins per day for", username, "is", average_day_logins)
    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
    login_ratio = current_day_logins / average_day_logins
    # Return the ratio used to store numbers added,subtracted,divided,multiplied
    return login_ratio
# Call `analyze_logins() and store the output in a variable named `login_analysis` 
login_analysis = analyze_logins("ejones", 9, 3)
# Conditional statement that displays an alert about the login activity if it's more than normal
if login_analysis >= 3:
    print("Alert! This account has more login activity than normal.")
   