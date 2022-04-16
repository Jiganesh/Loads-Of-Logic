# https://leetcode.com/problems/design-an-atm-machine/
class ATM:

    # Runtime: 689 ms, faster than 83.33% of Python3 online submissions for Design an ATM Machine.
    # Memory Usage: 17.5 MB, less than 100.00% of Python3 online submissions for Design an ATM Machine.

    def __init__(self):
        self.denominations= [20, 50, 100,200,500]
        self.noOfDenominations= [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount):
        for i in range (len(banknotesCount)):
            self.noOfDenominations[i]+= banknotesCount[i]

    def withdraw(self, amount: int) :
        withdrawn =[0, 0,0,0,0]

        endPointer = 4
        initialState = self.noOfDenominations

        while endPointer>=0:

            if self.noOfDenominations[endPointer]:
                maxNotesAvailabe = min(self.noOfDenominations[endPointer], amount//(self.denominations[endPointer]))
                amount-= maxNotesAvailabe * self.denominations[endPointer]
                withdrawn[endPointer]= maxNotesAvailabe
            endPointer-=1

        if amount ==0:
            for i in range (len(withdrawn)):
                self.noOfDenominations[i]-=withdrawn[i]
            return withdrawn

        else:
            self.noOfDenominations = initialState
            return [-1]

