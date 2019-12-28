#!/usr/bin/env bash

INSTALL="/home/miguelmurca/latextemplate"

echo -e "\e[1mRemoving $HOME/bin link...\e[0m"
rm $HOME/bin/latextemplate

echo ""

if [ -z $INSTALL ]
then
    echo -e "\e[31mInstallation directory variable was not set,"
    echo -e "cannot remove files. Please manually remove your"
    echo -e "latextemplate installation.\e[0m"
else
    echo -e "\e[1mRemoving latextemplate installation...\e[0m"
    rm -r $INSTALL
fi

echo ""

echo -e "\e[33mPlease remove the LATEX_TEMPLATES_DIR environment"
echo -e "variable from your ~/.bashrc or equivalent.\e[0m"