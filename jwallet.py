# TODO Support BTC, ETH, ETC, and USDT
# TODO upon generating an address, check with a blockchain API to see if it already exists
# TODO setup argparse to handle CLI arguments

# TODO actually finish this

import argparse
import bitcoinlib
from bitcoinlib.wallets import Wallet
import eth_account
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


def wallet_info_prompt(priv_key=None,addr=None,coin="eth"):
    os.system('clear')

    if coin == "eth":
        print(f"Key: 0x{priv_key.hex()}\nAddress: {addr}")  

    elif coin == "btc" or coin == "ltc":
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

def generate_eth_account():
    # Create a private key and address combo, with a random number for extra randomness
    wallet = eth_account.Account.create(os.urandom(32))

    # TODO display address and key  with warning before exit
    # NOTE make sure to check that wallet doesn't exist and that it doesn't
    # save to bash history

    if (check_existing_eth_account(wallet.address)):
        print("wow! that wallet address already exists. Trying again!")
        generate_eth_account()

    wallet_info_prompt(priv_key=wallet.key, addr=wallet.address)



# Probalby just gonna call the eth one as well
def generate_etc_account():
    pass


def generate_btc_account():
    bitcoinlib.wallets.wallet_delete_if_exists('bitcoin_wallet') 
    wallet = Wallet.create('bitcoin_wallet')
    
    # TODO check if wallet exists first

    key = wallet.new_key()

    wallet_info_prompt(priv_key=key.key_private.hex(), addr=key.address, coin="btc")


def generate_ltc_account():
    bitcoinlibe.wallets.wallet_delete_if_exists('litecoin_wallet')
    wallet = Wallet.create('litecoin_wallet', network='litecoin')

    key = wallet.new_key()

    wallet_info_prompt(priv_key=key.key_private.hex(), addr=key.address, coin="ltc")



#generate_eth_account()

def main():
    parser = argparse.ArgumentParser(
                prog="JWallet",
                description="A CLI tool built for securely generating paper wallets"
            )

    parser.add_argument("-c", "--coin", help="The selected cyrptocurrency. (eth only for now)")
    parser.add_argument("--from_key")

    args = parser.parse_args()
    
    if (not args.coin):
        raise Exception("Coin not recognized")

    if (args.coin.lower() == "eth"):
        generate_eth_account()
    elif (args.coin.lower() == "btc"):
        generate_btc_account()

if (__name__ == '__main__'):
    main()


