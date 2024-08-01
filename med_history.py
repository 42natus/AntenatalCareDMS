# Author: Fortunatus Olorunsola

"""This module manages the Antenatal Care patients' medical history."""

import datetime
import os
import time


# function for current date
def dt():
    tday = datetime.date.today()
    today = tday.strftime("%a, %d %b, %Y")
    print(("Current Date: " + today).center(200))


# function for receiving medical history record
def medhist():
    print("ANTENATAL CARE DATABASE".center(120))
    print("PATIENTS' MEDICAL HISTORY".center(120))

    while True:
        print("Record Patient's Available Medical History: \n")

        # receive user input
        id_num = input("ID Number: \n")
        reg_no = input("Registration Number: \n")
        alrgy_q = input("Does Patient {} have any allergies? [Y/N] ".format(id_num)).lower()
        if alrgy_q == "y":
            alrgy = input("\n\tAllergies: ".rjust(10))
            print("\n")
        else:
            alrgy = "nil"
            print("\n")

        med_q = input("Is Patient {} on any medication? [Y/N] ".format(id_num)).lower()
        if med_q == "y":
            med = input("\n\tMedication: ".rjust(10))
            print("\n")
        else:
            med = "nil"
            print("\n")

        religion_q = input("Does Patient {} belong to any religious group? "
                           "[Y (yes) / N (no) / P (prefer not to say)] ".format(id_num)).lower()
        if religion_q == "y":
            religion = input("\n\tReligion/Religious Beliefs: ".rjust(10))
            print("\n")
        elif religion_q == "p":
            religion = "Undisclosed"
            print("\n")
        else:
            religion = "nil"
            print("\n")

        cap_by = input("Captured By (Nurse): (E.g.: Jane Doe)\n")
        cap_date = input("Current Date [E.g.: YYYY/MM/DD]: \n")

        # open text file to store received Medical History Records.
        if os.path.isdir("Antenatal_Care_Database") is False:
            print("""Apparently, the directory: \"Antenatal_Care_Database\" doesn't exist. 
            Tip: Try running the program properly from the Main Menu.""")
            quit()
        else:
            medhist_file = open("Antenatal_Care_Database/patients_medical_history.txt", "a")
            medhist_file.write("\nPatient No.\t\t:\t" + id_num + "\n" +
                               "Patient's Reg No.\t:\t" + reg_no + "\n" +
                               "Allergies\t\t:\t" + alrgy + "\n" +
                               "Medication\t\t:\t" + med + "\n" +
                               "Religion\t\t:\t" + religion + "\n" +
                               "Captured by\t\t:\t" + cap_by + "\n" +
                               "Capture date\t\t:\t" + cap_date + "\n\n")

            medhist_file.close()

        while True:
            question = input("\nDo you want to record another patient's medical history? [Y/N] \n").lower()
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
                print("Loading file: \"Antenatal_Care_Database/patients_medical_history.txt\"")
                time.sleep(1.0)
                print("Optimising for Console...\n")
                time.sleep(0.7)
                print("Done! \n")
                time.sleep(0.5)
                view_medhist()

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
                print("Data saved to \"patients_medical_history\" file...\n")
                time.sleep(0.7)
                print("Closing program...\n")
                time.sleep(0.5)
                print("...bye")
                break
    return


def view_medhist():
    read_medhist = open("Antenatal_Care_Database/patients_medical_history.txt", "r")
    medhist_r = read_medhist.read()
    print(medhist_r)

    read_medhist.close()
    return
