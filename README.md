# JWallet
A way to generate paper wallets in your CLI

**WARNING** *JWallet is a hobby project and may be unstable at times. I do not recommending using JWallet for large amounts of money. Use at your own risk.*

With an emphasis on security and cold storage, JWallet displays a private key 
and a public address for the new wallet in the coin of your choice. These values are not stored, nor are they displayed in the bash terminal directly. A user should *write down*
the displayed keys for later use. Once the screen dissapears, the values cannot 
be accessed again. 

JWallet currently only generates paper wallets, meaning nothing is stored, however
I think it could be fun to try to handle locally stored wallets and the
encryption that comes along with it.

## How to Use
`jwallet.py -c <coin>` <br>
JWallet currently generates wallets for:
- Ethereum Classic `etc`
- Bitcoin `btc`
- Litecoin `ltc`
- Dogecoin `doge`


