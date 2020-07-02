#!/bin/bash

echo "Removing latextemplate, template links..."
if rm "$HOME/bin/latextemplate" && rm "$HOME/bin/template"; then
    echo -e "\033[32mDone.\033[0m"
else
    echo "Something went wrong."
fi

echo ""

echo -e "\e[33mPlease remove the LATEX_TEMPLATES_DIR environment"
echo -e "variable from your ~/.bashrc or equivalent.\e[0m"
