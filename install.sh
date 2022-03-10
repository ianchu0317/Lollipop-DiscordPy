#!/bin/sh

# Install latest python and requeriments
echo "Installing python3 and required modules... "
sudo apt install python3 && sudo apt install python3-pip
pip install -r requeriments

# Set up executables
chmod +x Lollipop.py

# Set up discord token for bot, write it to file
printf "Enter discord bot token (get token here https://discord.com/developers/): "
read token
echo token > token.txt


echo "[+] Your Lollipop is ready to go !"
