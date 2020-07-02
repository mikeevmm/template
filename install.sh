#!/usr/bin/env bash

echo -e "\e[1mChecking that python3 is installed...\e[0m"
which python3
if [[ $? -ne 0 ]]
then
    echo -e "\e[31mCould not find a python3 installation, aborting.\e[0m"
    exit 1
else
    echo -e "\e[32mPython3 installed!\e[0m"
fi

echo ""

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo -e "\e[1mThis script\e[0m will add a symlink from"
echo -e "$HOME/bin/"
echo -e "to"
echo -e "$DIR/latextemplate.py"
echo -e "so that you can call latextemplate from any directory."
echo -e "\`template\` is also added as an alias."
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

if ln -s "$DIR/latextemplate.py" "$HOME/bin/latextemplate" && \
	ln -s "$DIR/latextemplate.py" "$HOME/bin/template"
then
    echo -e "\033[32mDone.\033[0m"
else
    echo -e "\033[91mSomething went wrong.\033[0m"
	exit 1
fi

echo ""

echo -e "\e[1m\e[33mPlease add the following line to your ~/.bashrc"
echo -e "or equivalent:\e[0m\e[0m"
echo "export LATEX_TEMPLATES_DIR=$DIR/templates"
echo -e "\e[33mTo uninstall, run the uninstall.sh script.\e[0m"

echo ""

echo -e "Call \`template --help\` for more info."
