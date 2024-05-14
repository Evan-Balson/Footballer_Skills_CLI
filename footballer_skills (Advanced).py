# Evan Balson, Student ID: BAL18466416, Player Salary Calculator.
# ALL Player's details in ordered lists:
import os
from tabulate import tabulate
from datetime import datetime
import re
ALL_AGES = []
ALL_DOB = []
ALL_PID = []
ALL_PFN = []
ALL_PLN = []
ALL_PSR = []
ALL_PSHR = []
ALL_PPASR = []
ALL_PDR = []
ALL_PDBBR = []
ALL_PPHYR = []
ALL_PSKLR = []
ALL_PPLSR = []
ALL_PIMPR = []
ALL_PPSLY = []
ALL_SCORES = []
ALL_OVR = []
ALL_SALARIES = []
# defining salary variables for later.
Salary_1 = 1000
Salary_2 = 700
Salary_3 = 500
Salary_4 = 400
Payment_rate = 100/30
rating_set = [0, 1, 2, 3, 4, 5]
# Validation Rules


def Name_Check(message):
    while True:
        try:
            user_input_for_first_name = str(input(message))
            # if not user_input_for_first_name.replace(" ", "").isalpha():
            #     while not user_input_for_first_name.isalpha():
            #         print("The rating you entered was invalid\n")
            #         user_input_for_first_name = input(message)
            #         user_input_for_first_name.isalpha()
            #     return user_input_for_first_name.lower()
            # else:
            #     return user_input_for_first_name.lower()
            return user_input_for_first_name.lower()
        except ValueError:
            print("The rating you entered was invalid")
            continue


def R_CHK(message):
    while True:
        try:
            user_INSPR = int(input(message))
            while user_INSPR not in rating_set:
                print("The rating you entered was invalid")
                user_INSPR = int(input(message))
            return int(user_INSPR)
        except ValueError:
            print("The rating you entered was invalid")
            continue


def calculate_rating(SPD, SHOOT, PASS, DEFEN, DRIBB, PHYS):
    Player_Score = int(SPD) + int(SHOOT) + int(PASS) + int(DEFEN) + int(DRIBB) + int(PHYS)
    return Player_Score


# Calculations to determine Overall Rate
def Overall_Rate_Calculator(Player_Score):
    ORresult = Player_Score * Payment_rate
    return ORresult


# Calculations to determine Salary
def calculate_salary(Overall_Rate):
    if Overall_Rate >= 80:
        Player_Salary = str(Salary_1)
    elif Overall_Rate < 80 and Overall_Rate > 60:
        Player_Salary = str(Salary_1) + " " + str(Salary_2)
    elif Overall_Rate == 60:
        Player_Salary = str(Salary_2)
    elif Overall_Rate < 60 and Overall_Rate > 45:
        Player_Salary = str(Salary_2) + " " + str(Salary_3)
    elif Overall_Rate == 45:
        Player_Salary = str(Salary_3)
    elif Overall_Rate < 45 and Overall_Rate > 30:
        Player_Salary = str(Salary_3) + " " + str(Salary_4)
    elif Overall_Rate <= 30 and Overall_Rate >= 0:
        Player_Salary = str(Salary_4)
    return Player_Salary


# Tabulation options
def imported_P_Tab():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    data = []
    for i in range(len(ALL_PFN)):
        player_data = [ALL_PID[i], ALL_PFN[i],
                       ALL_DOB[i], ALL_AGES[i],
                       ALL_OVR[i], ALL_SALARIES[i]]
        data.append(player_data)
    headers = ["ID", "Name", "D.o.B", "Age", "Score", "Salary Range"]
    table = tabulate(data, headers, tablefmt="simple")
    print(table)
    file_path = os.path.join(script_directory, "players.txt")
    # Save the table to the TXT file
    with open(file_path, "w") as file:
        file.write(table)
    print("\nTable has been saved.")


# Tabulation options
def P_Tab():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    data = []
    for i in range(len(ALL_PFN)):
        player_data = [ALL_PID[i], ALL_PFN[i],
                       ALL_DOB[i], ALL_AGES[i],
                       ALL_OVR[i], ALL_SALARIES[i]]
        data.append(player_data)
    headers = ["ID", "Name", "D.o.B", "Age", "Score", "Salary Range"]
    sorted_data = sorted(data, key=lambda x: x[0])
    table = tabulate(sorted_data, headers, tablefmt="simple")
    print(table)
    file_path = os.path.join(script_directory, "players.txt")
    # Save the table to the TXT file
    with open(file_path, "w") as file:
        file.write(table)
    print("\nTable has been saved.")


def verify_age(dob):
    dob_date = datetime.strptime(dob, '%Y-%m-%d')
    today = datetime.today()
    age = (today.year - dob_date.year -
           ((today.month, today.day) <
            (dob_date.month, dob_date.day)))
    return age


def date_validate():
    Valid = None
    while Valid != 1:
        input_date = input("Enter the year (YYYY-mm-dd): ")
        # Define the ISO date pattern
        iso_date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        # Check if the input matches the pattern
        if not iso_date_pattern.match(input_date):
            print("The date you entered was invalid.")
        # Check if it's a valid date using the datetime module
        try:
            datetime.strptime(input_date, '%Y-%m-%d')
            Valid = 1
            player_age = verify_age(input_date)
            return input_date, player_age
        except ValueError:
            print("The date you entered was invalid.")


def end_now():
    if ID_input.lower() == "end":
        return 1
    else:
        return 0


def ID_check(message):
    result = "invalid"
    global ID_input
    while result == "invalid":
        ID_input = input(message)
        end_check = end_now()
        if end_check == 1:
            result = "valid"
            return ID_input
        elif len(ID_input) == 2:
            try:
                int(ID_input)
                if ID_input in ALL_PID:
                    print("The ID you entered is already taken.")
                    result = "invalid"
                else:
                    result = "valid"
                return ID_input
            except ValueError:
                print("The ID you entered was invalid")
        else:
            print("The ID you entered was invalid")
    return ID_input


def read_data_from_file(filename):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # path to save the table
    file_path = os.path.join(script_directory, f"{filename}")
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return lines


def advanced(filename):
    global ALL_PID, ALL_PFN, ALL_PLN, ALL_DOB
    global ALL_AGES, ALL_PSR, ALL_PSHR, ALL_PPASR
    global ALL_PDR, ALL_PDBBR
    global ALL_PPHYR, ALL_PSKLR, ALL_PPLSR, ALL_PIMPR
    global ALL_PPSLY, ALL_SCORES, ALL_OVR, ALL_SALARIES
    lines = read_data_from_file(filename)
    UID_list = []
    Name_list = []
    DOB_list = []
    Speed_list = []
    Shooting_list = []
    Passing_list = []
    Defending_list = []
    Dribbling_list = []
    Physicality_list = []
    for line in lines[1:]:  
        # Start from the second line to skip the header
        entry = line.strip().split(',')
        UID_list.append(entry[0])
        Name_list.append(entry[1])
        DOB_list.append(entry[2])
        Speed_list.append(entry[3])
        Shooting_list.append(entry[4])
        Passing_list.append(entry[5])
        Defending_list.append(entry[6])
        Dribbling_list.append(entry[7])
        Physicality_list.append(entry[8])
    # append the resulting lists
    ALL_PID = ALL_PID + UID_list
    ALL_PFN = ALL_PFN + Name_list
    ALL_DOB = ALL_DOB + DOB_list
    ALL_PSR = ALL_PSR + Speed_list
    ALL_PSHR = ALL_PSHR + Shooting_list
    ALL_PPASR = ALL_PPASR + Passing_list
    ALL_PDR = ALL_PDR + Defending_list
    ALL_PDBBR = ALL_PDBBR + Dribbling_list
    ALL_PPHYR = ALL_PPHYR + Physicality_list
    # Calculating data.
    Age_list = []
    Score_list = []
    OVR_list = []
    Salaries_list = []
    imported_players = len(UID_list)-1
    position = 0
    while imported_players >= 0:
        Player_Score = (int(Speed_list[position]) +
                        int(Shooting_list[position]) +
                        int(Passing_list[position]) +
                        int(Defending_list[position]) +
                        int(Dribbling_list[position]) +
                        int(Physicality_list[position]))
        date_of_birth = DOB_list[position]
        date_of_birth = date_of_birth.replace(' ', '')
        current_age = verify_age(date_of_birth)
        Overall_Rate = Overall_Rate_Calculator(Player_Score)
        SALARIES_Data_imp = calculate_salary(Overall_Rate)
        Score_list.append(Player_Score)
        OVR_list.append(Overall_Rate)
        Salaries_list.append(SALARIES_Data_imp)
        Age_list.append(current_age)
        imported_players -= 1
        position += 1
    ALL_AGES = ALL_AGES + Age_list
    ALL_SCORES = ALL_SCORES + Score_list
    ALL_OVR = ALL_OVR + OVR_list
    ALL_SALARIES = ALL_SALARIES + Salaries_list
    imported_P_Tab()


# Main Code
def main():
    global SPD
    global SHOOT, PASS, DEFEN, DRIBB, PHYS, date, ID
    program_counter = 3
    while program_counter > 0:
        ID = ID_check("\nEnter Player ID to start or 'End' to exit: ")
        if ID != "end":
            # Capture new Data.
            First_Name = Name_Check("Enter the player's Name: ")
            First_Name = First_Name.lower()
            (date, age) = date_validate()
            SPD = R_CHK("Enter speed rating: ")
            SHOOT = R_CHK("Enter shooting rating: ")
            PASS = R_CHK("Enter passing rating: ")
            DEFEN = R_CHK("Enter defending rating: ")
            DRIBB = R_CHK("Enter dribbling rating: ")
            PHYS = R_CHK("Enter physicality rating: ")
            ALL_AGES.append(age)
            ALL_DOB.append(date)
            ALL_PID.append(ID)
            ALL_PFN.append(First_Name)
            ALL_PSR.append(SPD)
            ALL_PSHR.append(SHOOT)
            ALL_PPASR.append(PASS)
            ALL_PDR.append(DEFEN)
            ALL_PDBBR.append(DRIBB)
            ALL_PPHYR.append(PHYS)
            # Get Calculations for table
            Player_Score = calculate_rating(SPD, SHOOT, PASS,
                                            DEFEN, DRIBB, PHYS)
            Overall_Rate = Overall_Rate_Calculator(Player_Score)
            Player_Salary = calculate_salary(Overall_Rate)
            ALL_SCORES.append(Player_Score)
            ALL_OVR.append(Overall_Rate)
            ALL_SALARIES.append(Player_Salary)
            print("The player's score is ", Player_Score)
            print("The overall rate is", int(Overall_Rate))
            print("The player's salary is", Player_Salary)
            P_Tab()
            program_counter -= 1
        else:
            program_counter = 0
    # End Loop
    print("\nAlright, bye! See you after your coffee break!\n")
    P_Tab()


if __name__ == '__main__':
    main()
