/*
Raffle Engine
---------------------

This is a solidity smart contract that accepts user addresses that are then a entered into a raffle. 


*/
// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

import "hardhat/console.sol";

contract Raffle {
 // House address for fees
    address house =

 // Stores entered public addresses
    address[] entries;

    constructor() {
        console.log("Deployed!");
    }
 // This function returns a random number between 0 and the # of entries to select a winner
    function pickWinner() private view returns (uint) {
        uint random = uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp, entries)));
        uint index = random % entries.length;
        return index;
    }
 // Public function can be called outside the contract with Remix, payable indicates that we can transfer eth to this contract when called
    function enter() public payable {
        require(msg.value >= 1 ether, "Pay 1 Ether or more to enter the raffle");

        entries.push(msg.sender);
 //When the raffle hits the number of entries (in this case 5) it triggers the pick winner array
        if (entries.length >= 5) {
            uint winnerIndex = pickWinner();
            address winner = entries[winnerIndex];
            console.log(winner);
        // Gets the prize amount
            uint256 prizeAmount = address(this).balance;
        //Charges a 1% fee for the house along with the amount
            uint256 feeAmount = (address(this).balance / 100);
            (bool success, ) = (house).call{value: feeAmount}(""); 
            require(success, "Failed to withdraw money from the contact");
        // Sends the remaining money to the winners address with the prize amount
            (bool success, ) = (winner).call{value: prizeAmount}(""); 
            require(success, "Failed to withdraw money from the contact");
        

            delete entries;
        }
    }


    function getLength() public view returns (uint) {
        return entries.length;
    }
}