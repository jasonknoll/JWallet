# TODO import dependencies for bitcoin, ethereum, and QR codes
# TODO upon generating an address, check with a blockchain API to see if it already exists
# TODO setup argparse to handle CLI arguments

# TODO actually finish this

import argparse
import bitcoinlib
import eth_account
import requests
import qrcode


def generate_qr_code(data):
    qr = qrcode.make(data)

    # qr.save("wallet.png")
