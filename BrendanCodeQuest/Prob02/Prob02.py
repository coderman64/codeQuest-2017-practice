from __future__ import print_function

QUART_VAL = .25
DIME_VAL = .1
NICK_VAL = .05
PENN_VAL = .01

def greedyChange(change, amount):   
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    if change > QUART_VAL:
        newQuarts = int(change/QUART_VAL)
        quarters += newQuarts
        change -= newQuarts * QUART_VAL

    if change > DIME_VAL:
        newDimes = int(change/DIME_VAL)
        dimes += newDimes
        change -= newDimes * DIME_VAL
          
    if change > NICK_VAL:
       newNicks = int(change/NICK_VAL)
       nickels += newNicks
       change -= newNicks * NICK_VAL
       
    if change > PENN_VAL:
       newPenns = int(change/PENN_VAL)
       pennies += newPenns
       change -= newPenns * PENN_VAL
       
    print(change,amount)
    print('Quarters=',quarters, sep='')
    print('Dimes=',dimes,sep='')
    print('Nickels=',nickels,sep='')
    print('Pennies=',pennies,sep='')
             
f = open('Prob02.in.txt', 'r')
numTests = int(f.readline())

for x in xrange(0, numTests):
    amount = f.readline()
    change = float(amount[1:])
    greedyChange(change, amount)
    
f.close()