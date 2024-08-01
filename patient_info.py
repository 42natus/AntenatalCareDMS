# Author: Fortunatus Olorunsola

"""This module manages the Antenatal Care patients' personal information."""

import datetime
import os
import time


# to display current date
def dt():
    tday = datetime.date.today()
    today = tday.strftime("%a, %d %b, %Y")
    print(("Current Date: " + today).center(200))


# to receive input for patients' personal information
def patients():
    print("ANTENATAL CARE DATABASE".center(120))
    print("PATIENTS".center(118))

    while True:
        print("Fill in the following Patient Personal Info. details:\n")

        # receive user input
        id_num = input("ID Number: \n")
        sur = input("Surname: \n")
        nam = input("First Name: \n")
        addr = input("Home Address: \n")
        marsta = input("Marital Status (Single / Married / Widowed / Divorced): \n")
        dob = input("Date of Birth (E.g.: June 8, 2003): \n")
        state = input("State of Origin: \n")
        tel = input("Home Tel. Number (E.g.: 08123456789): \n")
        email = input("Email address: \n")
        tribe = input("Tribe: \n")
        print("\nConception Info.: \n")
        dcon = input("\tDate conceived [YYYY/MM/DD]: \n\t")
        edd = input("\tExpected Delivery Date [YYYY/MM/DD]: \n\t")

        # lmp = input("First day of Patient {}'s last menstrual period [YYYY/MM/DD]: \n".format(id_num))
        # dyear = int(lmp[:4])
        # dmonth = int(lmp[5:7])
        # dday = int(lmp[8:])
        #
        # d = datetime.date(dyear, dmonth, dday)
        # tdelta = datetime.timedelta(days=7)     # add 7 days to lmp
        # step1 = d + tdelta
        #
        # tdelta2 = datetime.timedelta(months=3)
        # step2 = step1 - tdelta2
        #
        # tdelta3 = datetime.timedelta(year=1)
        # step3 = step2 + tdelta3

        # open text file to store received Patient Info.
        if os.path.isdir("Antenatal_Care_Database") is False:
            print("""Apparently, the directory: \"Antenatal_Care_Database\" doesn't exist. 
            Tip: Try running the program properly from the Main Menu.""")
            quit()
        else:
            patients_file = open("Antenatal_Care_Database/patients.txt", "a")
            patients_file.write("\nPatient No.\t\t:\t" + id_num + "\n" +
                                "Patient Name\t\t:\t" + sur + ", " + nam + "\n" +
                                "Address\t\t\t:\t" + addr + "\n" +
                                "Marital Status\t\t:\t" + marsta + "\n" +
                                "Date of Birth\t\t:\t" + dob + "\n" +
                                "State of Origin\t\t:\t" + state + "\n" +
                                "Home Phone\t\t:\t" + tel + "\n" +
                                "Email address\t\t:\t" + email + "\n" +
                                "Tribe\t\t\t:\t" + tribe + "\n" +
                                "Date Conceived\t\t:\t" + dcon + "\n" +
                                "Expected Delivery Date\t:\t" + edd + "\n\n")

            patients_file.close()

        while True:
            question = input("\nDo you want to add information on another patient? [Y/N] \n").lower()
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
                print("Loading file: \"Antenatal_Care_Database/patients.txt\"\n")
                time.sleep(1.0)
                print("Optimising for Console...\n")
                time.sleep(0.7)
                print("Done! \n")
                time.sleep(0.5)
                view_patients()

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
                print("Data saved to \"patients\" file...\n")
                time.sleep(0.7)
                print("Closing program...\n")
                time.sleep(0.5)
                print("...bye")
                break
    return


# to display file in console
def view_patients():
    read_patients = open("Antenatal_Care_Database/patients.txt", "r")
    patients_r = read_patients.read()
    print(patients_r)

    read_patients.close()
    return
