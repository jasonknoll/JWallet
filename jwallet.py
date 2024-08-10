# TODO Add USDT
# TODO See if there are any cool data points to display upon creation
# TODO Potentially add things like balance and transaction
# TODO Add support for mnemonic key and backup wallets
# NOTE My main focus is around ocld storage, but should I store wallets too?

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

    elif coin == "bitcoin" or coin == "litecoin" or coin == "dogecoin":
        print(f"Key: {priv_key}\nAddress: {addr}") 

    print("TAKE NOTE of these values! After you leave this screen, you won't see them again!")
    print("You may generate the address from the private key later on.")
    print("Do NOT give anyone your private key.")
    while True: 
        enter = input("Press enter to leave this screen...")
        confirm = input("Are you sure? (hit enter again to confirm)")
        break
    os.system('clear') 


def generate_etc_account():
    wallet = eth_account.Account.create(os.urandom(32))

    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

    if not w3.is_connected():
        raise Exception("Could not connect to node!")

    account = w3.is_address(wallet.address)

    if account:
        wallet_info_prompt(priv_key=wallet.key, addr=wallet.address)

    #print(f"New Wallet balance: {w3.eth.get_balance(wallet.address)}!")


def generate_coin_account(coin="bitcoin"):
    bitcoinlib.wallets.wallet_delete_if_exists('jwallet')

    coins = ['bitcoin', 'litecoin', 'dogecoin']

    if coin not in coins:
        raise Exception(f"Error! {coin} not supported!")

    wallet = Wallet.create('jwallet', network=coin)

    key = wallet.new_key()

    wallet_info_prompt(priv_key=key.key_private.hex(), addr=key.address, coin=coin)


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
        generate_coin_account("bitcoin")
    elif (args.coin.lower() == "ltc"):
        generate_coin_account("litecoin")
    elif (args.coin.lower() == "doge"):
        generate_coin_account("dogecoin")
    elif (args.coin.lower() == "etc"):
        generate_etc_account()
    else:
        print(f"Coin {args.coin} not recognized")


if (__name__ == '__main__'):
    main()


