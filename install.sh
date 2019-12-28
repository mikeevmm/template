#!/usr/bin/env bash

echo "This script will install latextemplate to your system."
read -p "Continue [y/N]?" -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
else
    echo ""
fi

echo ""

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

echo -e "\e[1mChecking that pip3 is installed...\e[0m"
which pip3
if [[ $? -ne 0 ]]
then
    echo -e "\e[31mCould not find a pip3 installation, aborting.\e[0m"
    exit 1
else
    echo -e "\e[32mpip3 installed!\e[0m"
fi

echo ""

echo -e "\e[1mInstalling python requirements...\e[0m"
pip3 install -r requirements.txt
if [[ $? -ne 0 ]]
then
    echo -e "\e[31mInstalling requirements failed, aborting.\e[0m"
    exit 1
else
    echo -e "\e[32mRequirements installed successfully!\e[0m"
fi

echo ""

PREFIX="${PREFIX:-$HOME}"
INSTALL="$PREFIX/latextemplate"
echo -e "\e[1mInstalling files into $INSTALL...\e[0m"

mkdir "$INSTALL"

if [[ $? -ne 0 ]]
then
    exit 1
fi

cp -r . "$INSTALL"

if [[ $? -ne 0 ]]
then
    exit 1
fi

sed -i "s@INSTALL=\"\"@INSTALL=\"$INSTALL\"@" "$INSTALL/remove.sh"

echo ""

echo -e "\e[1mMaking python module file executable...\e[0m"
chmod +x "$INSTALL/latextemplate.py"

if [[ $? -ne 0 ]]
then
    exit 1
fi

echo ""

echo -e "\e[1mCreating link in $HOME/bin...\e[0m"
ln "$INSTALL/latextemplate.py" "$HOME/bin/latextemplate"

if [[ $? -ne 0 ]]
then
    exit 1
fi

echo ""

echo -e "\e[32mSuccessfully installed latextemplate!\e[0m"

echo ""

echo -e "\e[1m\e[33mPlease add the following line to your ~/.bashrc"
echo -e "or equivalent:.\e[0m\e[0m"
echo "export LATEX_TEMPLATES_DIR=$INSTALL/templates"
echo -e "\e[33mTo uninstall, run the remove.sh script.\e[0m"

echo ""

echo -e "\e[1m\e[32mCall latextemplate to start.\e[0m\e[0m"
