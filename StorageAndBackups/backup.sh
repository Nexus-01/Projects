#!/bin/bash

#  user home directory
user=$(whoami)
input=/home/$user

# backup destination (change as needed)
output=/tmp/${user}_home_$(date +%Y-%m-%d_%H%M%S).tar.gz

# tar command to backup user's home directory
tar -cfz $output $input

# output information about backup
echo "Backup of $input information:"
ls -l $output
