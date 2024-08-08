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


def generate_qr_code(data):
    qr = qrcode.make(data)

    # qr.save("wallet.png")


def generate_eth_account():
    # Create a private key and address combo, with a random number for extra randomness
    wallet = eth_account.Account.create(os.urandom(32))

    # print(f"Key: {wallet.key.hex()}\nAddress: {wallet.address}")
    # TODO display address and key in secure way, with warning before exit
    # NOTE make sure to check that wallet doesn't exist and that it doesn't
    # save to bash history


def generate_btc_account():
    pass


