#import csv library
import csv

# open .csv file in write mode and set as 'userFile'
with open('usersTest.csv', mode='w') as userFile:
	# create an array named titleFields that contains the item names
	# then use the DictWriter method to use the dictionary structure for item:key pairs
	titleFields = ['firstName', 'lastName', 'department']
	contentWriter = csv.DictWriter(userFile, fieldnames=titleFields)

	# write the headers, then create a new row containing each user's item:key pair
	contentWriter.writeheader()
	contentWriter.writerow({'firstName':'John', 'lastName':'Smith', 'department':'IT'})
	contentWriter.writerow({'firstName':'Jane', 'lastName':'Doe', 'department':'Engineering'})
	contentWriter.writerow({'firstName':'Test', 'lastName':'', 'department':'HR'})


## TODO:
#	Create a generator for random zip codes and add the zip code header. Assign each user a random zip code.
#	Do the same as the zip code generate and header, but for phone numbers.
#	Perform checks to ensure duplicate names don't occur. Having duplicates will result in the powershell script failing to add the duplicate user due to having the same names.
#	More to come after the above is completed.
