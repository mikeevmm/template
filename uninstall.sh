#!/bin/bash

echo "Removing template link..."
if rm "$HOME/bin/template"; then
    echo -e "\033[32mDone.\033[0m"
else
    echo "Something went wrong."
fi

echo ""

echo -e "\e[33mPlease remove the TEMPLATES_DIR environment"
echo -e "variable from your ~/.bashrc or equivalent.\e[0m"
