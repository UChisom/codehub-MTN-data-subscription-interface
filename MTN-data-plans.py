# MTN data plans program

prompt = "Welcome to the MTN Data Plans list \nCarrier info:"
print(prompt)
daily_plans = {'N50' : '40 MB', 'N100': '100MB', 'N100': '350MB(IG & TIKTOK ONLY)', 'N200':'250MB(2 DAYS)', 'N300': '1GB', 'N500': '2GB(2 DAYS)'}
weekly_plans = {'200': '1GB(IG&TIKTOK ONLY)', '300': '350MB', '500': '750MB(2-Week plan)', '500': '750MB+N500 Talktime (Val/ 14 days)','1500': '6GB'}
monthly_plans = {'1000': '1.5GB', '1200': '2GB', '1500': '3GB', '2000': '4.5GB', '2500': '6GB', '3500': '12GB', '1000': '1.5GB+N1000'}
bundle_prompt = "Would you like to bundle? \nEnter 'yes' or 'no' \n"
success_prompt = "You have bundled successfully"
cancel_prompt = "Subscription cancelled"

def print_menu():
    '''displays the main menu of the MTN data plans on dialing *131#'''
    all_products = {1: 'Data Plans', 2: 'XtraValue(Data+Voice)', 3: 'Social Bundles', 4: 'Balance Check', 5: "Roaming/Int'l", 6: 'Borrow Credit/ Recharge', 7: 'Gift Data', 8: "Video Packs", 9: 'Hot Deals', 99: 'Next'}
    for key, values in all_products.items():
        print(key,'. ', values)
def selection():
    selecta = input("Please select a number for the plan you want...\n")
    while selecta != '1':
        selecta = input("Sorry, this service is not available at this time. Try another:\n")
    return selecta

def data_plans_list(select):
    '''displays data plans list, that is the first option'''
    Data_Plans = {1: 'Daily', 2: 'weekly', 3: 'Monthly', 4: '2-3 months ', 5: 'Always On Plans', 6: "MIFI Plans", 7: 'Family Packs', 8: 'Hot deals', 9: "Free Youtube", 10: 'Manage Data'}
    if select == '1':
        for key, values in Data_Plans.items():
            print(key, '. ', values)
        dt_plan = input("ENTER YOUR OPTION HERE: \n")
        while int(dt_plan) > 3:
            dt_plan = input("sorry we do not have that plan yet. Please try another \n")
        return dt_plan

def daily(dat_plan):
    if dat_plan == '1':
        print('Your Dialy Plans are:')
        for i, (key, values) in enumerate(daily_plans.items()):
            num = i+1 
            print(num, '. ', key, ' for ', values)
        dl_plan = input('ENTER OPTION HERE: \n')
        while int(dl_plan) > len(list(daily_plans.keys())):
            dl_plan = input("Please make a valid selection: \n")
        index = int(dl_plan)-1
        price = list(daily_plans.keys())[index]
        amount = list(daily_plans.values())[index]
        message = f"You will be charged {price} for the purchase of {amount} Daily Plan."
        print(message)
        last_prompt = input(bundle_prompt)
        while last_prompt not in ['yes', 'no']:
            last_prompt = input('Please make a valid selection: \n')
        if last_prompt.lower() =='yes':
            print(success_prompt)
        else:
            print(cancel_prompt)
    else:
        pass

def weekly(dat_plan):
    if dat_plan == '2':
        print('Your Weekly Plans are:')
        for i, (key, values) in enumerate(weekly_plans.items()):
            num = i+1 
            print(num, '. N', key, ' for ', values)
        wk_plan = input('ENTER OPTION HERE: \n')
        index = int(wk_plan)-1
        price = list(weekly_plans.keys())[index]
        amount = list(weekly_plans.values())[index]
        message = f"You will be charged N{price} for the purchase of {amount} Weekly Plan."
        print(message)
        last_prompt = input(bundle_prompt)
        while last_prompt not in ['yes', 'no']:
            last_prompt = input('Please make a valid selection: \n')
        if last_prompt.lower() =='yes':
            print(success_prompt)
        else:
            print(cancel_prompt)
    else:
        pass
    
def monthly(dat_plan):
    if dat_plan == '3':
        print('Your Monthly Plans are:')
        for i, (key, values) in enumerate(monthly_plans.items()):
            num = i+1 
            print(num, '. N', key, ' for ', values)
        mt_plan = input('ENTER OPTION HERE: \n')
        index = int(mt_plan)-1
        price = list(monthly_plans.keys())[index]
        amount = list(monthly_plans.values())[index]
        message = f"You will be charged N{price} for the purchase of {amount} Monthly Plan. "
        print(message)
        last_prompt = input(bundle_prompt)
        while last_prompt not in ['yes', 'no']:
            last_prompt = input('Please make a valid selection: \n')
        if last_prompt.lower() =='yes':
            print(success_prompt)
        else:
            print(cancel_prompt)
    else:
        pass

def other_data_plans(dat_plan):
    if int(dat_plan) > 4:
        print("Sorry, this service is not currently available thank you.")
    
def main():
    while True:
        print_menu()
        select = selection()
        dat_plan = data_plans_list(select)
        daily(dat_plan)
        weekly(dat_plan)
        monthly(dat_plan)
        other_data_plans(dat_plan)

        restart = input("Would you like to restart? \n\t'yes' or 'no' \n")
        if restart.lower() != 'yes':
            break
    
    
if __name__ == '__main__':
    main()
    

