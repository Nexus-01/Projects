#import csv library
import csv

# open .csv file in write mode and set as 'userFile'
with open('usersTest.csv', mode='w') as userFile:
	# create an array name titleFields that contains the item names
	# then use the DictWriter method to use the dictionary structure for item:key pairs
	titleFields = ['firstName', 'lastName', 'department']
	contentWriter = csv.DictWriter(userFile, fieldnames=titleFields)

	# write the headers, then create a new row containing each user's item:key pair
	contentWriter.writeheader()
	contentWriter.writerow({'firstName':'John', 'lastName':'Smith', 'department':'IT'})
	contentWriter.writerow({'firstName':'Jane', 'lastName':'Doe', 'department':'Engineering'})
	contentWriter.writerow({'firstName':'Test', 'lastName':'', 'department':'HR'})
