Structure of Days:

Day 1: Create accounts - Creates 3 accounts
Day 2: Deposit to all three accounts
Day 3: Withdraw from all three accounts
Day 4: Transfer from account 1 to 2, 2 to 3 and 3 to 1.
Day 5: Deletes all three accounts

Each day sessions are indicated by three text files per day. The individual days include positive and negative testing to ensure correct QA analysis is occurring.

The masterAccFileDay_ indicates the current balances of the valid accounts. 

Before Running the code, ensure accounts.txt contains only 0 and masterAccFile.txt is empty.

CD into ConnectedATM and type ‘./testScript.sh’ into the terminal. Will run the test script for the 5 day session.