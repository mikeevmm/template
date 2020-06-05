#!/bin/bash

if ! which latexmk > /dev/null
then
    echo -e "\e[31mlatexmk is not installed, aborting.\e[0m"
    exit 1
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
mkdir -p "$DIR/out"

if latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdf -outdir="$DIR/out" "$DIR/main.tex"
then
    echo -e "\e[32mSuccess, output in out/main.pdf\e[0m"
else
    echo -e "\e[31mSomething went wrong, see above for details.\e[0m"
fi
