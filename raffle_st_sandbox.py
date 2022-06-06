import streamlit as st
import json
from dataclasses import dataclass
from typing import Any, List
from datetime import datetime, timedelta
import pandas as pd
import hashlib
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3

#Import the functions from ethereum.py
#from ethereum import w3, generate_account, get_balance, send_transaction
#from web3 import Web3

#Connect to web3 provider, input local host here!
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))


#Set the contract address (input as deployed on local network-- copy from Remix)
receiver = 0x7912bd9E742a81c620FF0FcF1A9Dc6b9De543f69

st.write(account.address)

# #Price per ticket in ETH
# price_per_ticket = 1
# current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# #drawing_date = current_date + timedelta(weeks=1)
# drawing_date = datetime(2022, 6, 30).strftime("%Y-%m-%d")
# pot = 0

# #Displaying the name of the site
# st.markdown("# Ethereum Raffle")
# st.markdown("## Purchase a ticket using ethereum and win big!")

# #Displaying the current time and next drawing
# st.sidebar.text(current_date)
# st.sidebar.text(f"Next drawing: {drawing_date}")

# st.sidebar.markdown("## Tickets are available at 1 ETH")

# #Creating a streamlit data input  for sender
# account_address = st.sidebar.text_input("Ethereum Address")

# #Creating a streamlit data input  for Receiver
# Tickets = st.sidebar.number_input("Tickets",min_value=1,step=1)

# #Creating a streamlit data input  for Amount
# Cost = (Tickets*price_per_ticket)

# if 'purchased' not in st.session_state: 
#     st.session_state.purchased=False

# def callback(): 
#     st.session_state.purchased=True

# #Displaying the purchase button and asking for confirmation
# purchased = st.sidebar.button("Purchase", on_click=callback)
# if purchased or st.session_state.purchased:
#     st.write("Please confirm the following information:")
#     st.write(f"Ethereum Address: {account_address}")
#     st.write(f"Number of Tickets: {Tickets}")
#     st.write(f"Your total cost is: {Cost} ETH")

# #Confirmation button
#     if st.button("Confirm"):
#         st.write(f" Congratulations {account_address}! You have purchased {Tickets} tickets for {Cost} ETH.")
#         st.balloons()

#         # Construct a raw transaction
#         raw_tx = {
#         "to": receiver,
#         "from": account_address,
#         "value": Cost*1000000000000000000,
#         "gas": gas_estimate,
#         "gasPrice": 0,
#         "nonce": w3.eth.getTransactionCount(account.address)
#     }

#         # Sign the raw transaction with ethereum account
#         signed_tx = account.signTransaction(raw_tx)

#             # Send the signed transactions
#             return w3.eth.sendRawTransaction(signed_tx.rawTransaction)


#         #Increasing the pot
#         pot += Cost
#         st.session_state.purchased=False

#     #Cancel button
#     elif st.button("Cancel"):
#         st.write("Order Cancelled")
#         st.session_state.purchased=False

# #Displaying the current pot
# st.sidebar.text(f"The current pot is {pot} ETH")














# # Imports
# import streamlit as st

# # Import the functions from ethereum.py
# from ethereum import w3, generate_account, get_balance, send_transaction
# from web3 import Web3

# w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# # Streamlit application headings
# st.markdown("# Automating Ethereum with Streamlit!")

# # Generate the Ethereum account
# account = generate_account(w3)

# # The Ethereum Account Address
# st.text("\n")
# st.text("\n")
# st.markdown("## Ethereum Account Address:")

# # Write the Ethereum account address to the Streamlit page
# st.write(account.address)

# # Display the Etheremum Account balance
# st.text("\n")
# st.text("\n")
# st.markdown("## Ethereum Account Balance:")

# # Call the get_balance function and write the account balance to the screen
# ether_balance = get_balance(w3, account.address)
# st.write(ether_balance)

# # An Ethereum Transaction
# st.text("\n")
# st.text("\n")
# st.markdown("## An Ethereum Transaction")

# # Create inputs for the receiver address and ether amount
# receiver = st.text_input("Input the receiver address")
# ether = st.number_input("Input the amount of ether")

# # Create a button that calls the `send_transaction` function and returns the transaction hash
# if st.button("Send Transaction"):

#     transaction_hash = send_transaction(w3, account, receiver, ether)

#     # Display the Etheremum Transaction Hash
#     st.text("\n")
#     st.text("\n")
#     st.markdown("## Ethereum Transaction Hash:")

#     st.write(transaction_hash)