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
		PasswordNeverExpires = $False
		
	}
	# check if user by username already exists, create if not
	try {
    		Get-ADUser -Identity $($splat["SamAccountName"])
    		Write-Host "User $($splat["SamAccountName"]) already exists. Continuing..." -ForegroundColor Red
	}
	catch [Microsoft.ActiveDirectory.Management.ADIdentityResolutionException] {
    		Write-Host "User does not exist. Creating..." -ForegroundColor Green
    		New-ADUser @splat
		Write-Host "User $($splat["SamAccountName"]) created." -ForegroundColor Green
		Write-Host "" # newline
	}

}
Write-Host "Script Finished." -Foreground Cyan

