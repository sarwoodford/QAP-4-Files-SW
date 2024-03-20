# Description: process insurance policies for the One Stop Insurance Company 
# Author     : Sara Woodford
# Date(s)    : March 17, 2024 - March 19, 2024

# import required libraries

import datetime
from datetime import timedelta 
import sys
import time

# define default values 

POLICY_NUM = 1948
BASIC_PREM = 869.00
ADD_CAR_DISC_RATE = 0.25
EX_LIABILITY_COV = 130.00
GLASS_COV = 86.00
LOAN_CAR_COV = 58.00
HST_RATE = 0.15
MON_PROCESS_FEE = 39.99

# # main program
# #gather user inputs 
# #validate required inputs

while True:
    print("")
    print("")
    print("ONE STOP INSURANCE COMPANY - INSURANCE POLICY PROGRAM")
    print("")
    print("")
    print("CUSTOMER INFORMATION")
    print("")
    while True: 
        first_name =  input("Enter customer first name            : ").title()
        if first_name == "":
            print("DATA ENTRY ERROR - first name cannot be blank")
        else:
            break

    while True:
        last_name =   input("Enter customer last name             : ").title()
        if last_name == "":
            print("DATA ENTRY ERROR - last name cannot be blank")
        else:
            break

    while True:
        street_add =  input("Enter customer street address        : ").title()
        if street_add == "":
            print("DATA ENTRY ERROR - street address cannot be blank")
        else:
            break

    while True: 
        city =        input("Enter customer city                  : ").title()
        if city == "":
            print("DATA ENTRY ERROR - city cannot be blank")
        else:
            break



    #validate using a list
    ProvinceLst = ["NL", "PE", "NS", "NB", "MB", "AB", "SK", "QC", "ON", "BC", "YT", "NU", "NT"]
    while True:
        province =    input("Enter the customer province (XX)     : ").upper()
        province = province.replace(".","")
        if province == "":
            print("DATA ENTRY ERROR - province cannot be blank.")
        elif len(province) != 2:
            print("DATA ENTRY ERROR - province must be 2 characters only.")
        elif province not in ProvinceLst:
            print("DATA ENTRY ERROR - invalid province entered")
        else:
            break

    while True:
        postal_code = input("Enter customer postal code (A0A0A0)  : ").upper()
        postal_code = postal_code.replace(" ","")
        postal_code = postal_code.replace("-","")
        if postal_code == "":
            print("DATA ENTRY ERROR - postal code cannot be blank")
        elif len(postal_code) != 6:
            print("DATA ENTRY ERROR - postal code must be 6 characters only")
        else:
            break


    while True: 
        phone_num =   input("Enter customer phone number (9999999): ")
        phone_num = phone_num.replace(" ", "") 
        phone_num = phone_num.replace("-", "")
        phone_num = phone_num.replace("/", "")
        phone_num = phone_num.replace(",","")
        if len(phone_num) != 7:
            print("DATA ENTRY ERROR - please enter phone number in provided format. ")
        elif phone_num == "":
            print("DATA ENTRY ERROR - phone number cannot be blank")
        elif (phone_num).isdigit == False:
            print('DATA ENTRY ERROR - phone number must be entered using numbers only')
        else:
            break

    print("")
    print("POLICY INFORMATION")
    print("")
    while True: 
        num_cars_insured = input("Enter the number of cars being insured                                                               : ")
        try:
            num_cars_insured = int(num_cars_insured)
        except:
            print("DATA ENTRY ERROR - number of cars insured must be a numeric value")
        else:
            if num_cars_insured == "":
                print("DATA ENTRY ERROR - number of cars cannot be blank")
            elif num_cars_insured < 1:
                print("DATA ENTRY ERROR - number of cars insured must be 1 or greater")
            elif num_cars_insured > 7692:
                print("DATA ENTRY ERROR - number of cars insured cannot exceed 7692")
            else:
                break
        
        #^^ because extra liability cannot exceed $1,000,000 and its easier to control that here where number of cars is already an integer rather than in the optional liability loop because that is a yes/no option. (1,000,000 / 130 = 7692) - unrealistic number i know (LOL) but possible considering large companies like transportation insuruing many lots worth of trucks and cars


    num_cars_insured = int(num_cars_insured)

    while True: 
        opt_extra_liab =  input("Would you like to apply optional extra liability (Y/N)?                                              : ").upper()
        if opt_extra_liab != "Y" and opt_extra_liab != "N":
            print("DATA ENTRY ERROR - extra liability answer must be 'Y or 'N'")
        elif opt_extra_liab == "":
            print('DATA ENTRY ERROR - extra liability option cannot be blank')
        else:
            break 


    while True: 
        opt_glass_cov =  input("Would you like to apply optional glass coverage(Y/N)?                                                : ").upper()
        if opt_glass_cov != "Y" and opt_glass_cov != "N":
            print("DATA ENTRY ERROR - glass coverage must be 'Y' or 'N'")
        elif opt_glass_cov == "":
            print('DATA ENTRY ERROR - glass coverage option cannot be blank')
        else:
            break 


    while True: 
        opt_loan_car =  input("Would you like to apply optional loan cars(Y/N)?                                                     : ").upper()
        if opt_loan_car != "Y" and opt_loan_car != "N":
            print("DATA ENTRY ERROR - loan car must be 'Y' or 'N'")
        elif opt_loan_car == "":
            print('DATA ENTRY ERROR - loan car option cannot be blank')
        else:
            break 

    #validate using a list
    PayOptionsLst = ["F","M","D"]
    while True:
        pay_opt =      input("How is the customer paying? Enter 'F' for in full, 'M' for monthly payments and 'D' for down payment : ").upper()
        if pay_opt not in PayOptionsLst:
            print("DATA ENTRY ERROR - pay option must be 'F','M' or 'D'")
        elif pay_opt == "":
            print('DATA ENTRY ERROR - pay option cannot be blank')
        else: 
            break


    discounted_amt = (BASIC_PREM / (1+ADD_CAR_DISC_RATE)) 

    ins_prem = BASIC_PREM + ((num_cars_insured - 1) * discounted_amt)

    #function #1 - calculates total extra costs using the optional add ons and whether the user wanted them or not 
    def CalcExCost(num_cars_insured, opt_glass_cov, opt_extra_liab, opt_loan_car):
        global glass_cov_amt
        global ex_liab_amt
        global loan_amt
        global total_extra_cost


        if opt_glass_cov == 'Y':
            glass_cov_amt = GLASS_COV * num_cars_insured
        else:
            glass_cov_amt = 0

        if opt_extra_liab == 'Y':
            ex_liab_amt = EX_LIABILITY_COV * num_cars_insured
        else:
            ex_liab_amt = 0

        if opt_loan_car == 'Y':
            loan_amt = LOAN_CAR_COV * num_cars_insured
        else:
            loan_amt = 0 

        total_extra_cost = glass_cov_amt + ex_liab_amt + loan_amt


        return glass_cov_amt, ex_liab_amt, loan_amt, total_extra_cost

    glass_cov_amt, ex_liab_amt, loan_amt, total_extra_cost = CalcExCost(num_cars_insured, opt_glass_cov, opt_extra_liab, opt_loan_car)


    total_ins_prem = ins_prem + total_extra_cost

    hst = total_ins_prem * HST_RATE

    total_cost = total_ins_prem + hst


    #function #2 - calculates monthly paymet based on what payment option the user choose. also offers a prompt to enter down payment amount if user picked to enter one 
    def CalcMonthlyPayment():
        global monthly_payment
        global down_payment

        if pay_opt == 'D':
            down_payment = input("Enter the down payment amount                                                                        : ")
            try:
                down_payment = float(down_payment)
                monthly_payment = ((total_cost - down_payment) + MON_PROCESS_FEE) / 8
            except:
                print("DATA ENTRY ERROR - down payment must be a numeric value")
        elif pay_opt == 'M':
            down_payment = "N/A"
            monthly_payment = (total_cost + MON_PROCESS_FEE) / 8
        else:
            down_payment = "N/A"
            monthly_payment = 0
        
        return monthly_payment, down_payment

    monthly_payment, down_payment = CalcMonthlyPayment()

    if pay_opt == "D":
        down_dsp = "${:,.2f}".format(down_payment)
    else:
        down_dsp = "N/A"

    if monthly_payment == "F":
        monthly_pay_dsp = "Paid in Full - No Payments Due"
    else:
        monthly_pay_dsp = "${:,.2f}".format(monthly_payment)

    #function #3 - validates user entered date in the right format
    def ValidateDateFormat(date_str, format_str):
        try:
            datetime.datetime.strptime(date_str, format_str)
            return True
        except:
            return False 
        

    PrevClaimsLst=[]

    print("")
    print("PREVIOUS CLAIM INFORMATION")
    print("")

    while True: 
            while True: 
                claim_num =   input("Enter customer claim number (99999)                              : ")
                if claim_num == "":
                    print('DATA ENTRY ERROR - claim number cannot be blank')
                elif len(claim_num) != 5:
                    print("DATA ENTRY ERROR - claim number must be 5 digits only")
                else:
                    break
            while True: 
                claim_date =  input ("Enter claim date (YYYY-MM-DD)                                    : ")
                if claim_date == "":
                    print("DATA ENTRY ERROR - claim date cannot be blank")
                # elif ValidateDateFormat(claim_date, "%Y-%m-%d") == False:
                #     print("DATA ENTRY ERROR - please enter claim date in provided format")
                else:
                    break
            while True: 
                claim_amt =   input("Enter the total of previous claim for current customer           : ")
                
                claim_amt = claim_amt.replace("$","")
                claim_amt = claim_amt.replace(",","")
                claim_amt = claim_amt.replace(".","")
                claim_amt = float(claim_amt)
                if claim_amt == "":
                    print("DATA ENTRY ERROR - amount of previous claims cannot be blank")
                else:
                    break 
            
            PrevClaimsLst.append((claim_num, claim_date, claim_amt))

            
            while True:
                continue_opt =input("Would you like to process another claim for customer? Enter Y / N: ").upper()
                if continue_opt == "":
                    print("DATA ENTRY ERROR - continue option cannot be blank")
                elif continue_opt !="Y" and continue_opt != "N":
                    print("DATA ENTRY ERROR - continue option must be 'Y' or 'N'")
                else:
                    break

            if continue_opt == "N":
                break 






    #function #4 - to calculate the first month pay date using datetime.now to get invoice date 
    def CalcMonthPayDate():
        global inv_date
        global first_month_pay_date

        inv_date = datetime.datetime.now()

        first_month_pay_date = (inv_date.replace(day=1) + timedelta (days=32)).replace(day=1)

        return first_month_pay_date, inv_date

    first_month_pay_date, inv_date = CalcMonthPayDate()

    first_month_pay_form = first_month_pay_date.strftime('%Y-%b-%d')
    inv_date_form = inv_date.strftime('%Y-%b-%d')


    # display results to user in the form of a receipt 
    print(f"")
    print(f"")
    print(f"")
    print(f"--------------------------------------------------------------------------------")
    print(f"                                                                                ")
    print(f"                          ONE STOP INSURANCE COMPANY                            ")
    print(f"                      Customer Insurance Policy Receipt                         ")
    print(f"{POLICY_NUM}                                                  Invoice Date: {inv_date_form}")
    print(f"--------------------------------------------------------------------------------")
    print(f" Customer Name  : {first_name:<} {last_name:<}                            Phone Number: {phone_num:<7s} ")
    print(f" Customer Adress: {street_add:<}, {city:<}                                      ")
    print(f"                  {postal_code:<}, {province:<}                                 ")
    print(f"--------------------------------------------------------------------------------")
    print(f"                              POLICY INFORMATION                                ")
    print(f"               -------------------------------------------------                ")
    print(f"               Number of Cars on Policy:                   {num_cars_insured:>4d}")
    ex_liab_dsp = "${:,.2f}".format(ex_liab_amt)
    print(f"               Optional Extra Liability:          {ex_liab_dsp:>13s}")
    glass_cov_dsp = "${:,.2f}".format(glass_cov_amt)
    print(f"               Optional Glass Coverage :          {glass_cov_dsp:>13s} ")
    loan_dsp = "${:,.2f}".format(loan_amt)
    print(f"               Optional Loan Car       :          {loan_dsp:>13s} ")
    ex_cost_dsp = "${:,.2f}".format(total_extra_cost)
    print(f"")
    print(f"               TOTAL EXTRA COST:                  {ex_cost_dsp:>13s}")
    print(f"               -------------------------------------------------                ")
    print(f"                                PRICE BREAKDOWN                                 ")
    print(f"--------------------------------------------------------------------------------")
    basic_prem_dsp = "${:,.2f}".format(BASIC_PREM)
    print(f" Inital Price for First Car                   : {basic_prem_dsp:>10s}            ")
    #^ not a calculated value but i thought it made sense to include with the discounted price 
    disc_dsp ="${:,.2f}".format(discounted_amt)
    print(f" Discounted Price for Additonal Cars on Policy: {disc_dsp:>10s}                  ")
    ins_prem_dsp = "${:,.2f}".format(ins_prem)
    print(f" Insurance Premium - Before Extra Costs       : {ins_prem_dsp:>10s}              ")
    total_prem_dsp = "${:,.2f}".format(total_ins_prem)
    print(f" Total Insurance Premium                      : {total_prem_dsp:>10s}            ")
    hst_dsp = "${:,.2f}".format(hst)
    total_cost_dsp = "${:,.2f}".format(total_cost)
    print(f"               -------------------------------------------------                ")
    print(f"               HST: {hst_dsp:>10s}         Total Cost: {total_cost_dsp:>13s}        ")
    print(f"               -------------------------------------------------                ")
    print(f" Payment Option :  {pay_opt}                 Down Payment  : {down_dsp:<9s}")
    print(f" Monthly Payment:  {monthly_pay_dsp:<10s}        First Pay Date: {first_month_pay_form}")
    print(f"--------------------------------------------------------------------------------")
    print(f"                           PREVIOUS CLAIM INFORMATION                           ")
    print(f"               -------------------------------------------------                ")
    print(f"                Claim #            Claim Date            Amount                 ")
    print(f"               -------------------------------------------------                ")

    for claim_num, claim_date, claim_amt in PrevClaimsLst:

        print(f"                {claim_num:<7}            {claim_date:<12}         ${claim_amt:>.2f}")
    print(f" ")
    print(f" ")

# save data to text file and 

    print("your claim is being processed and saved. please wait...")

    for _ in range(3):
        print("")
        print('saving claim data ...', end='\r')
        time.sleep(1)  
        sys.stdout.write('\033[2K\r')

    f = open("InsClaim.txt", "a")

    f.write("{}, ".format(str(POLICY_NUM))) 
    cust_name = first_name + " " + last_name
    f.write("{}, ".format(cust_name)) 
    cust_add = street_add + " " + city + " " + postal_code + " " + province
    f.write("{}, ".format(cust_add)) 
    f.write("{}, ".format(phone_num)) 
    f.write("{}, ".format(num_cars_insured)) 
    f.write("{}, ".format(opt_extra_liab)) 
    f.write("{}, ".format(opt_glass_cov)) 
    f.write("{}, ".format(opt_loan_car))
    f.write("{}, ".format(pay_opt))
    f.write("{}\n, ".format(str(total_ins_prem)))


# increase policy number by 1 each time a new policy is entered 
    POLICY_NUM += 1

    
    f.close()

    print("")
    print("claim data has been successfuly saved. ")
    time.sleep(1)  
    sys.stdout.write('\033[2K\r')

# house keeping
    
    while True:
        print("")
        end_opt =input("Would you like to process another claim for customer? Enter Y / N: ").upper()
        if end_opt == "":
            print("DATA ENTRY ERROR - continue option cannot be blank")
        elif end_opt !="Y" and end_opt != "N":
            print("DATA ENTRY ERROR - continue option must be 'Y' or 'N'")
        else:
            break

    if end_opt == "N":
        print("")
        print("Thank you for using One Stop Insurance Company's Program!")
        print("")
        break 


