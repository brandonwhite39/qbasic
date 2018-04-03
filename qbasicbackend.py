#!/usr/bin/env python
# Submitted by BFK Inc. for CISC 327
# Brandon White
# Karim Atta
# Fang Xu
# Dean Wilkins-Reeves
# November 2017

import argparse

def main():
    #argument parsing so that the program can be run from the command line
    
    p = argparse.ArgumentParser()
    p.add_argument('masterAccountFile')
    p.add_argument('transactionFiles', type=file, nargs='+')
    args = p.parse_args()
    master = args.masterAccountFile
    masterAccList = masterList()
    
    #transactionList1 = fileToList('transactions1.txt')
    
    #************************************************************
    #to merge all transaction files into one file
    merged = open("merged.txt", "w")
    for tFile in args.transactionFiles:
        line = tFile.readline()
        while line:
            if line != "EOS 0000000 000 0000000 ***"+"\n":
                merged.write(line)
            line = tFile.readline()
    merged.close()

    #function call to make the merged.txt file into a list to be easier to alter 
    transactionsList = mergeTransactions()
    newMaster = backend(transactionsList, masterAccList)
    #*************************************************************
    print("Master Acc List:")
    print(masterAccList)
    print("New Master Acc List:")
    print(newMaster)
    createMasterAccountsFile(newMaster)
    createAccountListFile()

def masterList():
    lis = []
    with open("masterAccFile.txt") as openfile:
        for line in openfile:
            line = line.rstrip("\n")
            lis.append(line)
        
    return lis

def fileToList(name):
    lis = []
    with open(name) as openfile:
        for line in openfile:
            line = line.rstrip("\n")
            lis.append(line)
        
    return lis

def mergeTransactions():
    #takes a long transaction file and makes it a list
    transactionsList = []
    with open("merged.txt", "r") as openfile:
        for line in openfile.readlines():
            line = line.rstrip('\n')
            transactionsList.append(line)
        
    return transactionsList

def backend(transL, oldM):

    #loops through transList
    for i in range(0,len(transL)):
        if transL[i][0:3] == "DEP":
            deposit(transL[i],oldM)
        elif transL[i][0:3] == "WDR":
            withdraw(transL[i],oldM)
        elif transL[i][0:3] == "XFR":
            transfer(transL[i],oldM)
        elif transL[i][0:3] == "DEL":
            for j in range(0, len(oldM)):
                print(oldM[j][0:7])
                print(transL[i][16:23])
                print(oldM[j][0:7] == transL[i][16:23])
                l = len(transL[i][24:])
                if oldM[j][0:7] == transL[i][16:23]:
                    print("deleted!!")
                    break
        elif transL[i][0:3] == "NEW":
            out = transL[i][4:11]+ " 000 " + transL[i][17:]
            oldM.append(out)
            print("created!!")
        else:
            print("Wrong format of transaction file")
            
    return oldM

def deposit(transaction, masterAcc):

    print(transaction)
    accNum = transaction.split(' ')[1]
    for i in range(0,len(masterAcc)):
        number = masterAcc[i].split(' ')[0]
        if accNum == number:
            balance = int(masterAcc[i].split(' ')[1])
            dep = int(transaction.split(' ')[2])
            balance += dep
            lineList = lineToList(masterAcc[i])
            lineList[1] = balance
            masterAcc[i] = listToLine(lineList)
            return masterAcc
        else:
            continue
    return masterAcc

def lineToList(line):
    lineList = line.split(' ')
    print(lineList)
    return lineList

def listToLine(newlist):
    newLine = ""
    for word in newlist:
        newLine = newLine + str(word) + " "
    return newLine


def withdraw(transaction, masterAcc):
    accNum = transaction.split(' ')[3]
    for i in range(0,len(masterAcc)):
        number = masterAcc[i].split(' ')[0]
        if accNum == number:
            balance = int(masterAcc[i].split(' ')[1])
            withD = int(transaction.split(' ')[2])
            balance -= withD
            lineList = lineToList(masterAcc[i])
            lineList[1] = balance
            masterAcc[i] = listToLine(lineList)
            return masterAcc
    return masterAcc
        

def transfer(transaction, masterAcc):
    toAcc = transaction.split(' ')[1]
    fromAcc = transaction.split(' ')[3]
    for i in range(0,len(masterAcc)):
   
        number = masterAcc[i].split(' ')[0]
        if toAcc == number:
            balance = int(masterAcc[i].split(' ')[1])
            dep = int(transaction.split(' ')[2])
            balance += dep

            lineList = lineToList(masterAcc[i])
            lineList[1] = balance
            masterAcc[i] = listToLine(lineList)
        
        elif fromAcc == number:
            balance = int(masterAcc[i].split(' ')[1])
            withD = int(transaction.split(' ')[2])
            balance -= withD
            
            lineList = lineToList(masterAcc[i])
            lineList[1] = balance
            masterAcc[i] = listToLine(lineList)
            
        else:
            continue
    return masterAcc

            
def createMasterAccountsFile(masterAccList):
    #Creates a master accounts file from a master account list
    print("Method Master Account List:")
    print(masterAccList)
    print("Writing master account list to file")
    with open('masterAccFile.txt','w') as masterList:
        for line in masterAccList:
            print(line)
            masterList.write(line + '\n')
    return
    

def createAccountListFile():
    #takes a master accounts file and loops through it to find all valid account numbers to create a list of them (returns in file format)
    lineList = []
    masterAccounts = open('masterAccFile.txt','r')
    
    for line in masterAccounts:
        lineList.append(line.split()[0])

    with open('accounts.txt','w') as accList:
        accList.write("0\n")
        for line in lineList:
            accList.write(line + '\n')
    return


main()
