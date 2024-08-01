# Author: Fortunatus Olorunsola

"""This module manages the Antenatal Care visit records."""

import datetime
import os
import time


# to display current date
def dt():
    tday = datetime.date.today()
    today = tday.strftime("%a, %d %b, %Y")
    print(("Current Date: " + today).center(200))


# to receive input for antenatal visit records
def anterec():
    print("ANTENATAL CARE DATABASE".center(120))
    print("ANTENATAL VISIT RECORDS".center(120))

    while True:
        print("Add/Update a Patient's Antenatal Visit Record:\n")

        # receive user input
        cdate = input("Current Date [E.g.: yyyy-mm-dd]: \n")
        id_num = input("Patient's ID Number: \n")
        sur = input("Surname: \n")
        nam = input("First Name: \n")
        age = input("Age: \n")
        blpress = input("Blood Pressure (mmHg) [E.g.: 120/80]: \n")
        # fine-tune blood pressure :)
        systolic = int(blpress[:3])
        diastolic = int(blpress[4:])

        if systolic <= 120 and diastolic <= 80:
            message = "Blood Pressure is in the Normal range (less than 120 over 80 (i.e. 120/80))."
        elif systolic >= 120 and diastolic <= 80:
            message = "Blood Pressure appears to be Elevated (120-129/less than 80)."
        elif systolic >= 130 and diastolic > 80:
            message = "Patient has reached Stage 1 High Blood Pressure (130-139/80-89)."
        elif systolic >= 140 and diastolic >= 90:
            message = "Patient has reached Stage 2 High Blood Pressure (140 and above/90 and above)."
        elif systolic > 180 and diastolic > 120:
            message = "Hypertension Crisis (higher than 180/higher than 120) — See proper doctor right away!"
        else:
            message = "(to be assessed)"

        # normal: less than 120 over 80(120 / 80)
        # elevated: 120 - 129 / less than 80
        # Stage 1 hbp: 130 - 139 / 80 - 89
        # Stage 2 hbp: 140 and above / 90 and above
        # Hypertension Crisis: higher than 180 / higher than 120 - See a doctor right away

        weight = input("Present Weight (kg): \n")
        bweight = input("Baby's weight (kg): \n")
        height = input("Height (m): \n")
        urine = input("Urine Test Result: \n")
        pcv = input("PCV Level: \n")
        other = input("If necessary, enter remark here: \n")
        # ultrasc = input("Ultra Scan Photo Location: \n")
        # nxtappt = input("Next Appointment Date [E.g.: YYYY/MM/DD]: \n")

        # for next appointment, use timedelta to calculate the date two weeks from <cdate>
        dyear = int(cdate[0:4])
        dmonth = int(cdate[5:7])
        dday = int(cdate[8:])

        d = datetime.date(dyear, dmonth, dday)
        tdelta = datetime.timedelta(days=14)
        nxtappt = d + tdelta  # for next appointment date

        # open text file to store received Patient Info.
        if os.path.isdir("Antenatal_Care_Database") is False:
            print("""Apparently, the directory: \"Antenatal_Care_Database\" doesn't exist. 
            Tip: Try running the program properly from the Main Menu.""")
            quit()
        else:
            # open text file to store received Antenatal Visit Records.
            anterec_file = open("Antenatal_Care_Database/antenatal_visit_records.txt", "a")
            anterec_file.write("\nCurrent Date\t\t:\t" + cdate + "\n" +
                               "Patient No.\t\t:\t" + id_num + "\n" +
                               "Patient Name\t\t:\t" + sur + ", " + nam + "\n" +
                               "Age\t\t\t:\t{} years old".format(age) + "\n" +
                               "Blood Pressure\t\t:\t" + blpress + " mmHg" + ". [Remark: " + message + "]" + "\n" +
                               "Weight\t\t\t:\t" + weight + "kg" + "\n" +
                               "(Baby's weight\t\t:\t" + bweight + "kg)" + "\n" +
                               "Height\t\t\t:\t" + height + "m" + "\n" +
                               "Urine Test\t\t:\t" + urine + "\n" +
                               "PCV\t\t\t:\t" + pcv + "\n" +
                               "Other\t\t\t:\t" + other + "\n" +
                               "Next Appointment\t:\t" + str(nxtappt) + "\n\n")

            anterec_file.close()

        while True:
            question = input("\nDo you want to add another record? [Y/N] \n").lower()
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
                print("Record saved successfully...\n")
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
                print("Loading file: \"Antenatal_Care_Database/antenatal_visit_records.txt\"\n")
                time.sleep(1.0)
                print("Optimising for Console...\n")
                time.sleep(0.7)
                print("Done! \n")
                time.sleep(0.5)
                view_anterec()

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
                print("Data saved to \"antenatal_visit_records\" file...\n")
                time.sleep(0.7)
                print("Closing program...\n")
                time.sleep(0.5)
                print("...bye")
                break
    return


# to display file in console
def view_anterec():
    read_anterec = open("Antenatal_Care_Database/antenatal_visit_records.txt", "r")
    anterec_r = read_anterec.read()
    print(anterec_r)

    read_anterec.close()
    return
