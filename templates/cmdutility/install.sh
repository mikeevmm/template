#!/bin/bash

##########################################
# Delete this once you've setup this file. 
echo "You must setup install.sh"
exit 1
##########################################

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo -e "This script will add a symlink from"
echo -e "$HOME/bin/"
echo -e "to"
echo -e "$DIR/[UTILITY NAME]"
echo -e "so that you can call [UTILITY NAME] from any directory."
read -p $'\033[33mIs this ok [N/y]?\033[0m ' -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi

if [ ! -d $HOME/bin ]; then
    echo -e "$HOME/bin does not exist, creating that directory."
    read -p "Is this ok [N/y]? " -n 1 -r
    if [[ ! $REPLY =~ ^[Yy]$ ]]
    then
        [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
    fi
    mkdir $HOME/bin
    export PATH="$HOME/bin:$PATH"
    echo -e "\033[32mCreated $HOME/bin\033[0m"
fi

if ln -s "$DIR/[UTILITY NAME]" "$HOME/bin/[UTILITY NAME]"
then
    echo -e "\033[32mDone.\033[0m"
    echo -e "Call \`[UTILITY NAME] --help\` for more info."
else
    echo -e "\033[91mSomething went wrong.\033[0m"
fi
