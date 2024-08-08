# TODO Support BTC, ETH, ETC, and USDT
# TODO upon generating an address, check with a blockchain API to see if it already exists
# TODO setup argparse to handle CLI arguments

# TODO actually finish this

import argparse
import bitcoinlib
import eth_account
import requests
import qrcode
import os
from dotenv import load_dotenv

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

def generate_qr_code(data):
    qr = qrcode.make(data)

    # qr.save("wallet.png")


def check_existing_eth_account(address):
    url = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=asc&apikey={ETHERSCAN_API_KEY}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1' and len(data['result']) > 0:
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

    os.system('clear')
    print(f"Key: 0x{wallet.key.hex()}\nAddress: {wallet.address}")
    print("Take note of these! After you leave this screen, you won't see them again!")
    print("You may generate the address from the private key later on.")
    print("Do NOT give anyone your private key.")
    while True:
        enter = input("Press enter to leave this screen...")
        confirm = input("Are you sure? (hit enter again to confirm)")
        break
    os.system('clear')




def generate_etc_account():
    pass


def generate_btc_account():
    pass


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
     

if (__name__ == '__main__'):
    main()


