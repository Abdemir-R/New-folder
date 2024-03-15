# go from 0 to 5. in increments of 1
for i in range(0, 5, 1):
    print(i)
# same thing 0 to 5 since  include 0 it will be 0,1,2,3,4
for i in range(5):
    print(i)
# i will increase by one till it would reach 5 so 1,2,3,4
i = 1
while i < 5:
    print(i)
    i = i + 1
# will say login attempts 5 times starting from 0 ex:login_attempts: 0
login_attempts = 0
while login_attempts < 5:
    print("Login attempts:", login_attempts)
    login_attempts = login_attempts + 1
#will type try again 4 times.
count = 0
login_status = True
while login_status == True:
    print("Try again.")
    count = count + 1
    if count == 4:
        login_status = False
# will break at desktop20. will only output laptop1
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        break
    print(asset)
#will skip desktop20 in the interation
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        continue
    print(asset)

# Create a variable called `connection_attempts` that stores the number of times the user has tried to connect to the network
connection_attempts = 3
# Iterative statement using `for`, `range()`, a loop variable of `i`, and `connection_attempts`
# Display "Connection could not be established." as many times as specified by `connection_attempts`
for i in range(connection_attempts):
    print("Connection could not be established") #print connection attempts 3 times

# Assign `connection_attempts` to an initial value of 0, to keep track of how many times the user has tried to connect to the network
connection_attempts = 0
# Iterative statement using `while` and `connection_attempts`
# Display "Connection could not be established." every iteration, until connection_attempts reaches a specified number
while connection_attempts < 3:
    print("Connection could not be established")
    # Update `connection_attempts` (increment it by 1 at the end of each iteration)  
    connection_attempts = connection_attempts + 1 #will print connection attempt up to 3 times

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]
# For loop that displays the elements of `ip_addresses` one at a time
for i in ip_addresses:
    print(i)

# Assign `allow_list` to a list of IP addresses that are allowed to log in
allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]
# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]
# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
for i in ip_addresses:
	if i in allow_list:
		print("IP address is allowed")
	else:
		print("IP address is not allowed")

# Assign `allow_list` to a list of IP addresses that are allowed to log in
allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]
# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]
# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
              
for i in ip_addresses:
	if i in allow_list:
		print("IP address is allowed")
	else:
		print("IP address is not allowed. Further investigation of login activity required")
		break #stops loop if IP that isnt allowed is displayed
     
#You'll now complete another task. This involves automating the creation of new employee IDs.
#You have been asked to create employee IDs for a Sales department, with the criteria that the 
#employee IDs should all be numbers that are unique, divisble by 5, and falling between 5000 and 
#5150. The employee IDs can include both 5000 and 5150.
#Write a while loop that generates unique employee IDs for the Sales department by iterating through numbers and displays each ID created.
# Assign the loop variable `i` to an initial value of 5000
i = 5000
# While loop that generates unique employee IDs for the Sales department by iterating through numbers
# and displays each ID created
while i <= 5150: 
    print(i)
    i = i + 5
# Assign the loop variable `i` to an initial value of 5000
i = 5000

# While loop that generates unique employee IDs for the Sales department by iterating through numbers
# and displays each ID created
# This loop displays "Only 10 valid employee ids remaining" once `i` reaches 5100
while i <= 5150: 
    print(i)
    if i == 5100:
        print("Only 10 valid employee ids remaining")
    i = i + 5