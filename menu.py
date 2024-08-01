# Author: Fortunatus Olorunsola

"""This module runs the Main Menu of the Antenatal Care Data Management System"""

import datetime
import os
import time
import patient_info
import antenatal_visit
import med_history
import patient_trans


if os.path.isdir("Antenatal_Care_Database") is False:
    os.mkdir("Antenatal_Care_Database")
    # create necessary files in <Antenatal Care Database> folder

    patients_file = open("Antenatal_Care_Database/patients.txt", "a")
    patients_file.write("ANTENATAL CARE DATABASE".center(155) + "\n" + "PATIENTS".center(153))
    patients_file.close()

    anterec_file = open("Antenatal_Care_Database/antenatal_visit_records.txt", "a")
    anterec_file.write("ANTENATAL CARE DATABASE".center(155) + "\n" + "ANTENATAL VISIT RECORDS".center(155))
    anterec_file.close()

    medhist_file = open("Antenatal_Care_Database/patients_medical_history.txt", "a")
    medhist_file.write("ANTENATAL CARE DATABASE".center(155) + "\n" + "PATIENTS' MEDICAL HISTORY".center(155))
    medhist_file.close()

    transactions_file = open("Antenatal_Care_Database/patients_transactions.txt", "a")
    transactions_file.write("ANTENATAL CARE DATABASE".center(155) + "\n" +
                            "PATIENTS' PAYMENT ACCOUNT TRANSACTIONS".center(153))
    transactions_file.close()
else:
    pass

tday = datetime.date.today()
today = tday.strftime("%a, %d %b, %Y")
print(("Current Date: " + today).center(200))

print("{:*^7}".format("Fortunatus\' Program :)").center(120))
print("\n\n")
time.sleep(1.0)
print("ANTENATAL CARE DATA MANAGEMENT SYSTEM\n".center(120))
time.sleep(0.7)

while True:
    # display the main menu
    # print("=================MENU=================")
    print("{:=^40}".format("MENU").center(120))
    print("#      [1] Patient Information         #".center(120))
    print("#      [2] Antenatal Visit Record      #".center(120))
    print("#      [3] Patients' Medical History   #".center(120))
    print("#      [4] Transactions                #".center(120))
    print("#      [5] Exit                        #".center(120))
    print("{:=^40}".format("=").center(120))

    time.sleep(0.2)
    option = input("Pick an option from the menu above to proceed [1-5]\n")

    # sub-menu for option 1
    if option == "1":
        while True:
            print("{:=^40}".format("Patient Information").center(120))
            print(" #   [1] Enter New Patient Information  #".center(120))
            print(" #   [2] View Patient Information       #".center(120))
            print("{:=^40}".format("=").center(120))

            time.sleep(0.2)
            sub_option = input("Enter [1] or [2] to proceed: ")
            if sub_option == "1":
                patient_info.dt()
                patient_info.patients()
                break
            elif sub_option == "2":
                patient_info.view_patients()
                break
            else:
                print("ERROR <invalid input> : Pick either option [1] or [2].\n\n")
                time.sleep(1.5)
                continue

        time.sleep(0.5)
        # loop back to main menu
        key = input("\npress any key to return to the main menu...")
        if key is key:
            time.sleep(0.5)
            print("\nreturning to main menu...")
            time.sleep(1.0)
            print("\n")
            continue

    # sub-menu for option 2
    elif option == "2":
        while True:
            print("{:=^40}".format("Antenatal Visit Record").center(120))
            print(" #  [1] Add New Antenatal Visit Record  #".center(120))
            print(" #  [2] View Antenatal Visit Records    #".center(120))
            print("{:=^40}".format("=").center(120))

            time.sleep(0.2)
            sub_option = input("Enter [1] or [2] to proceed: ")
            if sub_option == "1":
                antenatal_visit.dt()
                antenatal_visit.anterec()
                break
            elif sub_option == "2":
                antenatal_visit.view_anterec()
                break
            else:
                print("ERROR <invalid input> : Pick either option [1] or [2].\n\n")
                time.sleep(1.5)
                continue

        time.sleep(0.5)
        # loop back to main menu
        key = input("\npress any key to return to the main menu...")
        if key is key:
            time.sleep(0.5)
            print("\nreturning to main menu...")
            time.sleep(1.0)
            print("\n")
            continue

    # sub-menu for option 3
    elif option == "3":
        while True:
            print("{:=^40}".format("Patients' Medical History").center(120))
            print(" #  [1] Add a Patient's Medical History #".center(120))
            print(" #  [2] View Patients' Medical History  #".center(120))
            print("{:=^40}".format("=").center(120))

            time.sleep(0.2)
            sub_option = input("Enter [1] or [2] to proceed: ")
            if sub_option == "1":
                med_history.dt()
                med_history.medhist()
                break
            elif sub_option == "2":
                med_history.view_medhist()
                break
            else:
                print("ERROR <invalid input> : Pick either option [1] or [2].\n\n")
                time.sleep(1.5)
                continue

        time.sleep(0.5)
        # loop back to main menu
        key = input("\npress any key to return to the main menu...")
        if key is key:
            time.sleep(0.5)
            print("\nreturning to main menu...")
            time.sleep(1.0)
            print("\n")
            continue

    # sub-menu for option 4
    elif option == "4":
        while True:
            print("{:=^44}".format("Transactions").center(120))
            print(" # [1] Add New Patients' Transaction Record #".center(120))
            print(" # [2] View Patients' Transaction Records   #".center(120))
            print("{:=^44}".format("=").center(120))

            time.sleep(0.2)
            sub_option = input("Enter [1] or [2] to proceed: ")
            if sub_option == "1":
                patient_trans.dt()
                patient_trans.trans()
                break
            elif sub_option == "2":
                patient_trans.view_trans()
                break
            else:
                print("ERROR <invalid input> : Pick either option [1] or [2].\n\n")
                time.sleep(1.5)
                continue

        time.sleep(0.5)
        # loop back to main menu
        key = input("\npress any key to return to the main menu...")
        if key is key:
            time.sleep(0.5)
            print("\nreturning to main menu...")
            time.sleep(1.0)
            print("\n")
            continue

    # exit code for option 5
    elif option == "5":
        while True:
            # confirmation message
            u_inp = input("\nAre you sure you want to exit the program? [Y/N] \n").lower()
            if u_inp == "y":
                print("CLOSING PROGRAM...")
                time.sleep(0.5)
                quit()
            elif u_inp == "n":
                print("RETURNING TO MAIN MENU...\n")
                time.sleep(0.5)
                break
            else:
                print("ERROR <invalid input> : Enter \"y\" for \"Yes\", or \"n\" for \"No\"\n")
                time.sleep(1.0)
                continue

    # to handle invalid numerical input from user
    else:
        print("ERROR <invalid input> : Choose an option from 1 to 5.\n\n")
        time.sleep(1.5)
        continue

# (note to self: add in Exception handling...)
