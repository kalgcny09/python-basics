first_name = raw_input("First Name: ")
last_name = raw_input("Last Name: ")
age = raw_input("How old are you?")
age_as_int = int(age)

if (first_name== last_name):
	print "Your first name is the same as your last name?"

if (age >= 21):
	print "you can buy beer"