import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from datetime import datetime, timedelta
import pandas as pd
import hashlib
from web3 import Web3

#Set the contract address (input as deployed on local network-- copy from Remix)
contract_address = 0x7912bd9E742a81c620FF0FcF1A9Dc6b9De543f69

#Price per ticket in ETH
price_per_ticket = 1
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#drawing_date = current_date + timedelta(weeks=1)
drawing_date = datetime(2022, 6, 30).strftime("%Y-%m-%d")
pot = 0

#Displaying the name of the site
st.markdown("# Ethereum Raffle")
st.markdown("## Purchase a ticket using ethereum and win big!")

#Displaying the current time and next drawing
st.sidebar.text(current_date)
st.sidebar.text(f"Next drawing: {drawing_date}")

st.sidebar.markdown("## Tickets are available at 1 ETH")

#Creating a streamlit data input  for sender
address = st.sidebar.text_input("Ethereum Address")

#Creating a streamlit data input  for Receiver
Tickets = st.sidebar.number_input("Tickets",min_value=1,step=1)

#Creating a streamlit data input  for Amount
Cost = (Tickets*price_per_ticket)

if 'purchased' not in st.session_state: 
    st.session_state.purchased=False

def callback(): 
    st.session_state.purchased=True

#Displaying the purchase button and asking for confirmation
purchased = st.sidebar.button("Purchase", on_click=callback)
if purchased or st.session_state.purchased:
    st.write("Please confirm the following information:")
    st.write(f"Ethereum Address: {address}")
    st.write(f"Number of Tickets: {Tickets}")
    st.write(f"Your total cost is: {Cost} ETH")

#Confirmation button
    if st.button("Confirm"):
        st.write(f" Congratulations {address}! You have purchased {Tickets} tickets for {Cost} ETH.")
        st.balloons()

            tx_hash = contract.functions.Raffle(
            contract_address
        ).transact({"from": address, "value": Cost*1000000000000000000, "gas": 2000000})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)


        #Increasing the pot
        pot += Cost
        st.session_state.purchased=False

    #Cancel button
    elif st.button("Cancel"):
        st.write("Order Cancelled")
        st.session_state.purchased=False

#Displaying the current pot
st.sidebar.text(f"The current pot is {pot} ETH")


# connect to the contract
#if st.button("Buy Philly Special NFT"):
 #   play_10_uri = "https://www.youtube.com/watch?v=y3Jqif1TUwQ"
##   tx_hash = contract.functions.mintTokens
#       address,
  #      play_10_uri,
   # ).transact({"from": address, "value": offer_price*1000000000000000000, "gas": 2000000})
    #receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    #st.write("Transaction receipt mined:")
    #st.write(dict(receipt))
