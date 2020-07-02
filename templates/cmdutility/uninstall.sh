#!/bin/bash

##########################################
# Delete this once you've setup this file. 
echo "You must setup uninstall.sh"
exit 1
##########################################

echo "Removing [UTILITY NAME] link..."
if rm "$HOME/bin/[UTILITY NAME]"; then
    echo -e "\033[32mDone.\033[0m"
else
    echo "Something went wrong."
fi
