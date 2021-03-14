#!/usr/bin/env bash

# Exit if any command fails
set -e

# Initialize the current directory as a Node project
npm init

# Install electron
npm install --save-dev electron@latest
