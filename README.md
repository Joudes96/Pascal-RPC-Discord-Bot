

# Pascal RPC Bot on Discord

A simple python Discord bot that retrieves information from the PascalCoin blockchain using JSON RPC.

# Contributing
Pascal JSON RPC Documentation:
[RPC](https://www.pascalcoin.org/development/rpc)

Feel free to add more functions using the RPC documentation above

# Installation
The bot doesn't require having an account or private keys in the wallet, as long as the wallet is running and accepting rpc requests. 

Works on both linux and windows nodes.

## Pascal Wallet Installation:
In order for the bot to make RPC calls, a PascalCoin wallet/node must be installed and running locally or remotely with an open Port for the RPC connection.

For the bot to be able to retrieve information older than the current safebox you need to install the entire blockchain using the blockchainstream zip file and extracting it to the Data directory.

For Wallet installation guide see:

[Wallet Installation](https://www.pascalcoin.org/get_started)

Sourceforge link to download the entire blockchain files:

[BlockchainStream](https://sourceforge.net/projects/pascalcoin/)




# Install python and required packages
## Python Installation:
```bash
$ sudo apt-get update
$ sudo apt-get install python3.6
```
## Packages Installation:
```bash
pip install requests
pip install discord
pip install pycoingecko 
```

## Add your discord bot token to last line at client.run() 
This is needed for the bot to login to discord, token can be retrieved from discord developer portal:

More Info [Discord Developer Portal](https://discord.com/developers/docs/intro)

## Running the bot
For non interactive mode, use screen to run the bot then deattach
```bash
python3 bot.py
```
