# imports
import random
import string

# create/open the file to append to. all file names are subject to the user's choice.
with open("user-site.txt", "a+") as user_site:
	# create the username generator
	def user_generator(length, site):
		user = [''.join(random.choice(string.ascii_letters)) for i in range(length)]
		username = ''.join(user)
		print("username is {}".format(username))
		
		# append the information to user-site.txt
		user_site.write("Your information is below.\n\t username: {0}\n\t site: {1}\n\n".format(username, site))

	# values as per the function. Change as needed.
	user_generator(8, "www.example.com")
	user_generator(17, "www.example2.com")


# create/open the file to append to. all file names are subject to the user's choice.
with open("pass-site.txt", "a+") as pass_site:

	# generate the password
	def pass_generator(pass_length, p_site):
		password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(pass_length))
		print("password is {}.".format(password))

		# append the password to pass-site.txt
		pass_site.write("Your information is below.\n\t password: {0}\n\t site: {1}\n\n".format(password, p_site))


	# values as per the function. Change as needed.
	pass_generator(16, "www.example.com")
	pass_generator(22, "www.example2.com")
