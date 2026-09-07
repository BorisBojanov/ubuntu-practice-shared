#!/bin/csh

# Assignment 2 Problem 11
# Boris Bojanov
# Sep 2026
# 
# Write a C Shell script to process ~/.login and ~/.cshrc, 
#   list all exported environment variables and their values. 
#   Include the script and a screenshot of execution, then explain each variable's purpose.
# 
# To make it executable
# chmod +x assignment2problem11.csh
# To execute the script
# ./assignment2problem11.csh

# Check if ~/.login exists
if ( -e ~/.login ) then
    echo "Loading ~/.login"
    source ~/.login
    set loginfile = ~/.login
    set outlog = ( `grep "^" "$loginfile"` )
    echo "This is the contents of ~/.login: $outlog"
    echo ""
    # printenv
else
    echo "Could not find ~/.login"
endif

echo ""

# Check id ~./cshrc exists
if ( -e ~/.cshrc ) then
    echo "Loading ~/.cshrc"
    source ~/.cshrc
    set cshrcfile = ~/.cshrc
    set outcsh = ( `grep "^" "$cshrcfile"` )
    echo "This is the contents of ~/.cshrc: $outcsh"
    echo ""
    printenv
else
    echo "Could not find ~/.cshrc"
endif

echo ""
echo "Done"