import requests
import json
import discord
from discord.ext import commands
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


client = commands.Bot(command_prefix="$")
url = 'http://localhost:4003'


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='$help'))
    print('We have logged in as {0.user}'.format(client))


@client.command(brief="gets the current node block")
# get block
async def getnodeblock(ctx):
    dada = '{"jsonrpc": "2.0", "method": "getblockcount"}'
    x = requests.post(url, data=dada)
    pretty_json = json.loads(x.text)
    block = str((json.dumps(pretty_json, indent=2)))
    await ctx.send(block)


@client.command(brief="gets an account information using it's number", description="(syntax: $getaccount <account#>")
# get account info
async def getaccount(ctx, nr):
    userinput = nr
    x = requests.post(
        url,
        json={
            "jsonrpc": "2.0",
            "method": "getaccount",
            "params": {"account": userinput},
        },
    )
    pretty_json = json.loads(x.text)
    account = str((json.dumps(pretty_json, indent=2)))
    await ctx.send(account)


@client.command(brief="shows a given block's operations", description="(syntax: $getblockops <block#>")
# gets ops of a block and writes them to a text file
async def getblockops(ctx, blocknr):
    userinput = blocknr
    x = requests.post(
        url,
        json={
            "jsonrpc": "2.0",
            "method": "getblockoperations",
            "params": {"block": userinput},
        },
    )
    pretty_json = json.loads(x.text)
    block = str((json.dumps(pretty_json, indent=2)))
    text_file = open("getblockops.txt", "w")
    text_file.write(block)
    text_file.close()
    await ctx.send(file=discord.File('getblockops.txt'))


@client.command(brief="finds an account using it's name", description="(syntax: $findpasabyname <name>")
# finds an account by name
async def findpasabyname(ctx, name):
    userinput = name
    x = requests.post(
        url,
        json={
            "jsonrpc": "2.0",
            "method": "findaccounts",
            "params": {"name": userinput},
        },
    )
    pretty_json = json.loads(x.text)
    account = str((json.dumps(pretty_json, indent=2)))
    await ctx.send(account)


@client.command(brief="shows a list of accounts with a min balance of",
                description="(Syntax: $findpasabyminbalance <balance>)")
# finds an accounts by min balance
async def findpasabyminbalance(ctx, minbalance):
    userinput = minbalance
    x = requests.post(
        url,
        json={
            "jsonrpc": "2.0",
            "method": "findaccounts",
            "params": {"min_balance": userinput},
        },
    )
    pretty_json = json.loads(x.text)
    account = str((json.dumps(pretty_json, indent=2)))
    text_file = open("byminbalance.txt", "w")
    text_file.write(account)
    text_file.close()
    await ctx.send(file=discord.File('byminbalance.txt'))


@client.command(brief="shows a list of account with a max balance of",
                description="(Syntax: $findpasabymaxbalance <balance>)")
# finds an accounts by maxbalance
async def findpasabymaxbalance(ctx, maxbalance):
    userinput = maxbalance
    x = requests.post(
        url,
        json={
            "jsonrpc": "2.0",
            "method": "findaccounts",
            "params": {"max_balance": userinput},
        },
    )
    pretty_json = json.loads(x.text)
    account = str((json.dumps(pretty_json, indent=2)))
    text_file = open("bymaxbalance.txt", "w")
    text_file.write(account)
    text_file.close()
    await ctx.send(file=discord.File('bymaxbalance.txt'))


@client.command(brief="shows a list of accounts with a given public key", description="(syntax: $findpasabypubkey)")
# finds an accounts by publickey
async def findpasabypubkey(ctx, pubkey):
    userinput = pubkey
    x = requests.post(
        url,
        json={
            "jsonrpc": "2.0",
            "method": "findaccounts",
            "params": {"enc_pubkey": userinput},
        },
    )
    pretty_json = json.loads(x.text)
    account = str((json.dumps(pretty_json, indent=2)))
    text_file = open("bypubkey.txt", "w")
    text_file.write(account)
    text_file.close()
    await ctx.send(file=discord.File('bypubkey.txt'))


@client.command(brief="shows a list of accounts with a given type", description="(syntax: $findpasabytype: <Type#>)")
# finds an accounts by type
async def findpasabytype(ctx, typenr):
    userinput = typenr
    x = requests.post(
        url,
        json={
            "jsonrpc": "2.0",
            "method": "findaccounts",
            "params": {"type": userinput},
        },
    )
    pretty_json = json.loads(x.text)
    account = str((json.dumps(pretty_json, indent=2)))
    text_file = open("bytype.txt", "w")
    text_file.write(account)
    text_file.close()
    await ctx.send(file=discord.File('bytype.txt'))


@client.command(brief="shows a given block's information", description="(syntax: $getblockinfo <Block#>")
# gets info about given block
async def getblockinfo(ctx, blocknr):
    userinput = blocknr
    x = requests.post(
        url,
        json={
            "jsonrpc": "2.0",
            "method": "getblock",
            "params": {"block": userinput},
        },
    )
    pretty_json = json.loads(x.text)
    block = str((json.dumps(pretty_json, indent=2)))
    text_file = open("blockinfo.txt", "w")
    text_file.write(block)
    text_file.close()
    await ctx.send(file=discord.File('blockinfo.txt'))


@client.command(brief="shows the current price of Pascalcoin (Coingecko API)")
# price from coingecko api
async def price(ctx):
    x = cg.get_price(ids='pascalcoin', vs_currencies='usd')
    await ctx.send(x)


@client.command(brief="shows blaise wallets download links")
# blaise wallets download links
async def blaise(ctx):
    await ctx.send(
        'Download Blaise wallet for Android: https://play.google.com/store/apps/details?id=com.appditto.blaise')
    await ctx.send(
        'Download Blaise wallet for IOS: https://apps.apple.com/us/app/blaise-pascal-wallet/id1473011216')


client.run("Insert your bot token here")