import random
from datetime import datetime
from datetime import date
from faker import Faker

fake = Faker()


def generateTxnId(n):
    list1 = []
    for i in range(n):
        txnid = random.randint(1, 100000)
        if txnid not in list1:
            list1.append(txnid)
    return list1


def getType(n, value):
    list1 = []
    for i in range(n):
        list1.append(value)
    return list1


def getBusinessDay(n):
    list1 = []
    for i in range(n):
        dt = datetime.now()
        day = dt.strftime('%A')
        list1.append(day)
    return list1


def getDate(n):
    list1 = []
    for i in range(n):
        today = date.today()
        d1 = today.strftime("%m/%d/%Y")
        list1.append(d1)
    return list1


def getCurrentTime(n):
    list1 = []
    for i in range(n):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        list1.append(current_time)
    return list1


def getAmount(n, current_balance):
    list1 = []
    list2 = []
    txn_amt = 0
    for i in range(n):
        if txn_amt<current_balance:
            new_txn_amt = random.randint(1, 1000)
            txn_amt = txn_amt + new_txn_amt
            list1.append(new_txn_amt)
            balance = current_balance - txn_amt
            list2.append(balance)
    return list1, list2


def getAccountNumber(n, account_number):
    list1 = []
    for i in range(n):
        list1.append(account_number)
    return list1

def getName(n):
    list1 = []
    for i in range(n):
        name = fake.name()
        list1.append(name)
    return list1
