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
