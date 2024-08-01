# Author: Fortunatus Olorunsola

"""This module manages information about the Antenatal Care patients' payment account transaction."""

import datetime
import os
import time


# to display current date
def dt():
    tday = datetime.date.today()
    today = tday.strftime("%a, %d %b, %Y")
    print(("Current Date: " + today).center(200))


# to receive input for patients' payment transaction details
def trans():
    print("ANTENATAL CARE DATABASE".center(120))
    print("PATIENTS' PAYMENT ACCOUNT TRANSACTIONS".center(118))

    while True:
        print("Patient's Transaction details:\n")

        # receive user input
        reg_no = input("Reg No.: \n")
        id_num = input("ID: \n")
        invoice = input("Invoice Number: \n")
        modpay = input("Mode of Payment: \n")
        transdt = input("Transaction Date: \n")
        description = input("Transaction Description: \n")
        fee = input("Amount Charged (₦): \n")
        payed = input("Amount Payed (₦): \n")
        bal = (float(fee) - float(payed))
        if bal != float(0):
            report = "Patient {} has yet to balance up.".format(id_num)
        else:
            report = "Patient {} has completed payment.".format(id_num)

        # open text file to store Patient Transactions Record.
        if os.path.isdir("Antenatal_Care_Database") is False:
            print("""Apparently, the directory: \"Antenatal_Care_Database\" doesn't exist. 
            Tip: Try running the program properly from the Main Menu.""")
            quit()
        else:
            patients_file = open("Antenatal_Care_Database/patients_transactions.txt", "a")
            patients_file.write("\nPatient's Reg No.\t:\t" + reg_no + "\n" +
                                "Patient No.\t\t:\t" + id_num + "\n" +
                                "Invoice Number\t\t:\t" + invoice + "\n" +
                                "Mode of Payment\t\t:\t" + modpay + "\n" +
                                "Transaction Date\t:\t" + transdt + "\n" +
                                "Description\t\t:\t" + description + "\n" +
                                "Amount Charged (NGN)\t:\t" + fee + "\n" +
                                "Amount Payed (NGN)\t:\t" + payed + "\n" +
                                "Balance (NGN)\t\t:\t{:.2f}".format(bal) + " (" + report + ")" + "\n\n")

            patients_file.close()

        while True:
            question = input("\nDo you want to add another entry of patient payment transactions? [Y/N] \n").lower()
            if question == "y":
                print("loading...\n\n")
                time.sleep(0.7)
                break
            elif question == "n":
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(0.2)
                print("Data saved successfully...\n")
                break
            else:
                print("Error: <invalid input>. Try again — press \"y\" for \"Yes\", and \"n\" for \"No\".\n")
                time.sleep(1.0)
                key = input("Press any key to continue...")
                if key is key:
                    time.sleep(0.2)
                    print("\n")
                    continue

        if question == "y":
            continue
        elif question == "n":
            question_2 = input("\nDo you want a quick view of the file? [Y/N] \n").lower()
            if question_2 == "y":
                print("Loading file: \"Antenatal_Care_Database/patients_transactions.txt\"\n")
                time.sleep(1.0)
                print("Optimising for Console...\n")
                time.sleep(0.7)
                print("Done! \n")
                time.sleep(0.5)
                view_trans()

                close = input("Do you want to exit the program? [Y/N] ").lower()
                if close == "y":
                    print("Closing program...")
                    time.sleep(0.5)
                    print("...bye")
                    break
                elif close == "n":
                    print("Okay then...\n")
                    time.sleep(0.7)
                    continue
            elif question_2 == "n":
                print("Data saved to \"patients_transactions\" file...\n")
                time.sleep(0.7)
                print("Closing program...\n")
                time.sleep(0.5)
                print("...bye")
                break
    return


# to display file in console
def view_trans():
    read_trans = open("Antenatal_Care_Database/patients_transactions.txt", "r")
    trans_r = read_trans.read()
    print(trans_r)

    read_trans.close()
    return
