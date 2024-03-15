#turns input into string data
new_string = str(123)
print(type(new_string))

#using len() function to print length of string
cheese = "beanes"
print(len(cheese))

#make everything uppcase can also use .lower() to make everything lowercase
print("hello".upper())

#indexing starts at 0 then so on so this will return 1
"Hello"[1]
#this wille extact ell starts at 1 and ends before 4
"hello"[1:4]
#use index to locate E
print("hello".index ("e"))


#example len() function
device_id_length = len("h32rb17")
if device_id_length == 7:
    print("The device ID has 7 characters.")


# Assign `employee_id` to a four digit number as an initial value
employee_id = 4186
# Display the data type of `employee_id`
print(type(employee_id))
# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)
# Display the data type of `employee_id` now
print(type(employee_id))


# Assign `employee_id` to a four digit number as an initial value. condition display message if ID has less than 5 digits
employee_id = 4186
# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)
# Conditional statement that displays a message if the employee ID length is less than 5 digits
if len(employee_id) < 5:
    print("This employee ID has less than five digits. It does not meet length requirements.")


# Assign `employee_id` to a four digit number as an initial value.
employee_id = 4186
# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)
# Display the `employee_id` as it currently stands
print(employee_id)
# Conditional statement that updates the `employee_id` if its length is less than 5 digits
if len(employee_id) < 5:
    employee_id = "E" + employee_id
# Display the `employee_id` after the update
print(employee_id)


# Assign `device_id` to a string that contains alphanumeric characters
device_id = "r262c36"
# Extract the fourth character in `device_id` and display it
print(device_id[3]) #output is 2


# Assign `device_id` to a string that contains alphanumeric characters
device_id = "r262c36"
# Extract the first through the third characters in `device_id` and display the result
device_id[0:3] #outputs r26


# Assign `url` to a specific URL
url = "https://exampleURL1.com"
# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url`
ind = url.index(".com") #index auto counts to where .com is
# Extract the website name in `url` and display it 
print(url[8:ind]) #starts after // and leaves out .com which is "ind"


#display starting index for 192.168.243.140
ip_addresses = "192.168.140.81, 192.168.109.50, 192.168.243.140"
ip_addresses.index("192.168.243.140")