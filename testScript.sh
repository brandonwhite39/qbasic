#!/bin/bash

clear

echo “Performing day 1 tests”
echo ""
./qbank.py accounts.txt transactions1.txt < Day1session1.txt
./qbank.py accounts.txt transactions2.txt < Day1session2.txt
./qbank.py accounts.txt transactions3.txt < Day1session3.txt

echo “qbasicbackend”
./qbasicbackend.py masterAccFile.txt transactions1.txt transactions2.txt transactions3.txt

cp masterAccFile.txt masterAccFileDay1.txt

echo “Performing day 2 tests”
echo ""
./qbank.py accounts.txt transactions1.txt < Day2session1.txt
./qbank.py accounts.txt transactions2.txt < Day2session2.txt
./qbank.py accounts.txt transactions3.txt < Day2session3.txt

echo “qbasicbackend”
./qbasicbackend.py masterAccFile.txt transactions1.txt transactions2.txt transactions3.txt

cp masterAccFile.txt masterAccFileDay2.txt

echo “Performing day 3 tests”
echo ""
./qbank.py accounts.txt transactions1.txt < Day3session1.txt
./qbank.py accounts.txt transactions2.txt < Day3session2.txt
./qbank.py accounts.txt transactions3.txt < Day3session3.txt

echo “qbasicbackend”
./qbasicbackend.py masterAccFile.txt transactions1.txt transactions2.txt transactions3.txt

cp masterAccFile.txt masterAccFileDay3.txt

echo “Performing day 4 tests”
echo ""
./qbank.py accounts.txt transactions1.txt < Day4session1.txt
./qbank.py accounts.txt transactions2.txt < Day4session2.txt
./qbank.py accounts.txt transactions3.txt < Day4session3.txt

echo “qbasicbackend”
./qbasicbackend.py masterAccFile.txt transactions1.txt transactions2.txt transactions3.txt

cp masterAccFile.txt masterAccFileDay4.txt

echo “Performing day 5 tests”
echo ""
./qbank.py accounts.txt transactions1.txt < Day5session1.txt
./qbank.py accounts.txt transactions2.txt < Day5session2.txt
./qbank.py accounts.txt transactions3.txt < Day5session3.txt

echo “qbasicbackend”
./qbasicbackend.py masterAccFile.txt transactions1.txt transactions2.txt transactions3.txt

cp masterAccFile.txt masterAccFileDay5.txt
