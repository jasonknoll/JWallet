# TODO Add ETC and USDT
# TODO upon generating an address, check with a blockchain API to see if it already exists
# TODO Potentially add things like balance and transactions

# TODO actually finish this

import argparse
import bitcoinlib
from bitcoinlib.wallets import Wallet
import eth_account
import web3
from web3 import Web3
import requests
import qrcode
import os
from dotenv import load_dotenv

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
# blockchain api key...
# tender api key...


# TODO setup qr code for EACH type of coin
def generate_qr_code(data):
    qr = qrcode.make(data)

    # qr.save("wallet.png")


def wallet_info_prompt(priv_key=None,addr=None,coin="etc"):
    os.system('clear')

    if coin == "etc":
        print(f"Key: {priv_key.hex()}\nAddress: {addr}")  

    elif coin == "btc" or coin == "ltc" or coin == "doge":
        print(f"Key: {priv_key}\nAddress: {addr}") 

    print("Take note of these! After you leave this screen, you won't see them again!")
    print("You may generate the address from the private key later on.")
    print("Do NOT give anyone your private key.")
    while True: 
        enter = input("Press enter to leave this screen...")
        confirm = input("Are you sure? (hit enter again to confirm)")
        break
    os.system('clear') 

def check_existing_eth_account(address):
    url = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=asc&apikey={ETHERSCAN_API_KEY}'

    # 
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':
            return True
    
    return False

# Probalby just gonna call the eth one as well
def generate_etc_account():
    wallet = eth_account.Account.create(os.urandom(32))

    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

    if not w3.is_connected():
        raise Exception("Could not connect to node!")

    account = w3.is_address(wallet.address)

    if account:
        wallet_info_prompt(priv_key=wallet.key, addr=wallet.address)

    #print(f"New Wallet balance: {w3.eth.get_balance(wallet.address)}!")


# TODO Consolidate into one function
# TODO Check if address already exists 
def generate_btc_account():
    bitcoinlib.wallets.wallet_delete_if_exists('bitcoin_wallet') 
    wallet = Wallet.create('bitcoin_wallet')
    
    # TODO check if wallet exists first

    key = wallet.new_key()

    wallet_info_prompt(priv_key=key.key_private.hex(), addr=key.address, coin="btc")


def generate_ltc_account():
    bitcoinlib.wallets.wallet_delete_if_exists('litecoin_wallet')
    wallet = Wallet.create('litecoin_wallet', network='litecoin')

    key = wallet.new_key()

    wallet_info_prompt(priv_key=key.key_private.hex(), addr=key.address, coin="ltc")


def generate_doge_account():
    bitcoinlib.wallets.wallet_delete_if_exists('dogecoin_wallet')
    wallet = Wallet.create('dogecoin_wallet', network='dogecoin')

    key = wallet.new_key()

    wallet_info_prompt(priv_key=key.key_private.hex(), addr=key.address, coin='doge')


#generate_eth_account()


def main():
    parser = argparse.ArgumentParser(
                prog="JWallet",
                description="A CLI tool built for securely generating paper wallets"
            )

    parser.add_argument("-c", "--coin", help="The selected cyrptocurrency")

    # TODO add generating wallet from existing priv key
    parser.add_argument("--from_key")

    args = parser.parse_args()
    
    if (not args.coin):
        raise Exception("Coin not recognized")

    if (args.coin.lower() == "btc"):
        generate_btc_account()
    elif (args.coin.lower() == "ltc"):
        generate_ltc_account()
    elif (args.coin.lower() == "doge"):
        generate_doge_account()
    elif (args.coin.lower() == "etc"):
        generate_etc_account()
    else:
        print(f"Coin {args.coin} not recognized")


if (__name__ == '__main__'):
    main()


