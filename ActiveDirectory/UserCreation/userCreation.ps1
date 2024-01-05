# imports the ActiveDirectory library that includes the functions needed
import-module ActiveDirectory

# import the .csv file to raed from to create users and assign to the variable $userlist
$userlist = Import-Csv -Path C:\Users\testAdmin\usersTest.csv

# loops through each line in the userlist
foreach ($user in $userlist) {
	# create a splat to pass multiple parameters in a single object for ease of readability
	$splat = @{
		Name = $user.firstName + ' ' + $user.lastName
		GivenName = $user.firstName
		Surname = $user.lastName
		SamAccountName = ($user.firstName[0] + $user.lastName).ToLower()
		Enabled = $True
		AccountPassword = (Read-Host -AsSecureString 'AccountPassword')
		EmailAddress = ($user.firstName[0] + $user.lastName + '@contoso.org').ToLower()
		Department = $user.department
		PasswordNeverExpired = $False
		
	}
	New-ADUser @splat
}


# TODO:
#	Generate a report of the users created.
#	Read basic information from each created user and direct the output to a json file. This can aid in viewing specific attributes without the need for powershell commands. This will also help in later scripts.
