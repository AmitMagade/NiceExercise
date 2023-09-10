import pandas as pd
import methods

df = pd.read_csv("account.csv", parse_dates=["OPEN_DATE", "LOAN_RELEASE_DATE", "LOAN_MATURITY_DATE"])


def generateTxnCsvFile(account_no, No_of_txns):
    for ind in df.index:
        if account_no == df["NUMBER"][ind]:
            row_ind = ind

    accountType = df["TYPE"][row_ind]
    currentBalance = df["CURRENT_BALANCE"][row_ind]
    accountNumber = df["NUMBER"][row_ind]

    TRANSACTION_ID = methods.generateTxnId(No_of_txns)
    TYPE = methods.getType(No_of_txns, accountType)
    BUSINESS_DAY = methods.getBusinessDay(No_of_txns)
    DATE = methods.getDate(No_of_txns)
    TIME = methods.getCurrentTime(No_of_txns)
    AMOUNT, BALANCE = methods.getAmount(No_of_txns, currentBalance)
    ACCOUNT_NUMBER = methods.getAccountNumber(No_of_txns, accountNumber)
    COUNTERPARTY_NAME = methods.getName(No_of_txns)

    dic1 = {"TRANSACTION_ID":TRANSACTION_ID, "TYPE":TYPE, "BUSINESS_DAY":BUSINESS_DAY, "DATE":DATE, "TIME":TIME, "AMOUNT":AMOUNT, "BALANCE":BALANCE, "ACCOUNT_NUMBER":ACCOUNT_NUMBER, "COUNTERPARTY_NAME":COUNTERPARTY_NAME}
    txn_df = pd.DataFrame(dic1)
    print(txn_df)

    txn_df.to_csv('transaction.csv', index=False)


generateTxnCsvFile(410012, 15)
