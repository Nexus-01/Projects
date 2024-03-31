#import csv, random
import csv
import random

# open .txt file containing first/last names and set as 'usernames'
with open('names.txt', mode='r') as userNames:
	names = userNames.readlines()
	names = [x.strip() for x in names]
	# open .csv file in write mode and set as 'userFile'
	
	with open('usersTest.csv', mode='w') as userFile:
		# create an array name titleFields that contains the item names
		# then use the DictWriter method to use the dictionary structure for item:key pairs
		titleFields = ['firstName', 'lastName', 'department']
		contentWriter = csv.DictWriter(userFile, fieldnames=titleFields)
		
 		# write the headers 
		contentWriter.writeheader()

		# test list for departments
		departments = ['IT', 'HR', 'IAM', 'Admins', 'Billings', 'Finance']
		
		#set first and last names for each user
		for name in names:
			firstname = name.split(" ")[0]
			lastname = name.split(" ")[1]
			department = random.choice(departments)
			
			# create a new row containing each user's item:key pair
			contentWriter.writerow({'firstName': firstname, 'lastName': lastname, 'department':department})
			


