# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 
# Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video of what 
# Brandon usually does to calculate his Rental Property ROI.

# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate 
# the Return on Investment(ROI) for a rental property. And now that we know a thing or two about making our 
# programs run more efficiently, try utilizing some of the strategies we talked about this week for optimization!

# Your Program should have the following (this is not an exhaustive list but just base functionality):

# -  There should be some sort of Driver code for users to choose what to do next 

# -  There should be a way to store multiple users and for users to be able to have multiple different properties 
# (This might be done by creating a User Class & a Property class similarly to how we did it with the Codeflix program)

# -  Properties should be able to store multiple different types of expenses (i.e. taxes, mortgage, insurance, etc) 
# and multiple different types of incomes (i.e. rent, laundry, parking, etc)

# -  The ROI needs to be calculated & displayed to the user and should also be stored for that specific property.

# This project will be completed individually, though you can feel free to share ideas with your fellow students.

# Once completed, commit the project to github and submit the link to this assignment.

# BUT WAIT THERES MORE!
# This is not a requirement but if you're feeling extra saucy, check out the list of API's below and see if 
# there is anything you can incorporate with this project. You can use the tvmaze api and pokeapi class projects 
# for reference.


class User:
    __id_counter = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password[::-2]
        self.id = User.__id_counter
        User.__id_counter += 1
        self.rental_properties = {}


    def __str__(self):
        formatted_user = f"{self.id} - {self.username.title()}\n" + f"Password: {self.password}"
        return formatted_user
    
    
    def __repr__(self):
        return f"<User {self.id} | {self.username}"
    
    
    def check_password(self, pw_guess):
        return self.password == pw_guess[::-2]
    

class Rental():

    def __init__(self):
        self.users = set()
        self.current_user = None


    def add_user(self):
        username = input("Please enter a username: ").title()
        if username in {i.username for i in self.users}:
            print("Username already exists.  Please use another.")

        else:
            password = input("Please enter a password: ")
            user = User(username, password)
            self.users.add(user)
            print(f"{user}\nAccount has been created.\n")

        self.login_user()


    def login_user(self):
        username = input("What is your username? ").title()
        password = input("What is your password? ")

        for user in self.users:
            if user.username == username and user.check_password(password):
                self.current_user = user
                print(f"{user}\nYou are now logged in.")
                break

        else:
            print("Username and/or password is incorrect.")

    
    def logout(self):
        self.current_user = None
        print("You are now logged out.")


    def update_user(self):
        if self.current_user:
            print(self.current_user)
            choice_update = input("Which do you want to update? Username or Password: ")
            if choice_update.lower() == "username":
                new_user = input("Please enter your new username: ").title()
                self.current_user.username = new_user
                print(f"{self.current_user.username} is the new username.")
            elif choice_update.lower() == "password":
                new_pw = input("Please enter your new password: ")
                self.current_user.password = new_pw

            print(f"{self.current_user.username}'s info has been updated.")

        else:
            print("Please login to update information.")
            self.login_user()


    # Creating new property info to account
    def add_to_properties(self):
        
        # Adding address 
        print("\nAdding new property info")
        address = input("What is the property's address?: ").title()
        self.current_user.rental_properties[address] = {}
        
        # Adding Income Information
        while True:
            try:
                print("\nAdding MONTHLY Income information")
                print("Enter only whole numbers with no commas (ex: 15000)")
                self.current_user.rental_properties[address]["Income"] = {}
                rental_income = int(input("What is the monthly rental income?: "))
                self.current_user.rental_properties[address]["Income"]["Rental Income"] = rental_income
                laundry = int(input("Any monthly laundry income? Enter 0 if there is none: "))
                self.current_user.rental_properties[address]["Income"]["Laundry"] = laundry
                storage = int(input("Any monthly storage income? Enter 0 if there is none: "))
                self.current_user.rental_properties[address]["Income"]["Storage"] = storage
                misc_income = int(input("Any other monthly miscellaneous income? Enter 0 if there is none: "))
                self.current_user.rental_properties[address]["Income"]["Misc Income"] = misc_income
        
                total_monthly_income = rental_income + laundry + storage + misc_income

        # Adding Expense Information
                print("\nAdding MONTHLY Expense information")
                print("Enter only whole numbers with no commas (ex: 15000)")
                self.current_user.rental_properties[address]["Expenses"] = {}
                mortgage = int(input("How much is the monthly mortgage?: "))
                self.current_user.rental_properties[address]["Expenses"]["Mortgage"] = mortgage
                tax = int(input("What is the monthly property tax of this property?: "))
                self.current_user.rental_properties[address]["Expenses"]["Tax"] = tax
                insurance = int(input("How much is the monthly insurance fee?: "))
                self.current_user.rental_properties[address]["Expenses"]["Insurance"] = insurance
                hoa = int(input("Any monthly HOA fees? Enter 0 if there is none: "))
                self.current_user.rental_properties[address]["Expenses"]["HOA Fee"] = hoa
                lawn = int(input("Any monthly lawn/snow fees? Enter 0 if there is none: "))
                self.current_user.rental_properties[address]["Expenses"]["Lawn/Snow Care Fee"] = lawn
                vacancy = int(input("How much is your monthly vacancy estimate? (Usually 5% of your rental income): "))
                self.current_user.rental_properties[address]["Expenses"]["Vacancy"] = vacancy
                repair = int(input("How much would you want to save aside monthly for any surprise repair fees (ex: carpet cleaning, fixing a hole in the wall, etc.)?: "))
                self.current_user.rental_properties[address]["Expenses"]["Repair Savings"] = repair
                capital_expenditures = int(input("How much would you want to save aside monthly for bigger surprise repairs (ex: new roof, new water heater, etc.): ? "))
                self.current_user.rental_properties[address]["Expenses"]["Capital Expenditures"] = capital_expenditures
                management = int(input("Any monthly rental management fees? Enter 0 if there is none: "))
                self.current_user.rental_properties[address]["Expenses"]["Rental Management"] = management
                print("\nAdding MONTHLY Utility expenses")
                self.current_user.rental_properties[address]["Expenses"]["Utility"] = {}
                electricity = int(input("How much is the monthly elecricity bill? Enter 0 if none or tenant pays for it: "))
                self.current_user.rental_properties[address]["Expenses"]["Utility"]["Electricity"] = electricity
                water = int(input("How much is the monthly water bill? Enter 0 if none or tenant pays for it: "))
                self.current_user.rental_properties[address]["Expenses"]["Utility"]["Water"] = water
                sewer = int(input("How much for monthly sewer bill? Enter 0 if none or tenant pays for it: "))
                self.current_user.rental_properties[address]["Expenses"]["Utility"]["Sewer"] = sewer
                garbage = int(input("How much for monthly garbage fees? Enter 0 if none or tenant pays for it: "))
                self.current_user.rental_properties[address]["Expenses"]["Utility"]["Garbage"] = garbage
                gas = int(input("How much for is the monthly gas bill? Enter 0 if none or tenant pays for it: "))
                self.current_user.rental_properties[address]["Expenses"]["Utility"]["Gas"] = gas
        
                total_monthly_expense = mortgage + tax + insurance + hoa + lawn + vacancy + repair + capital_expenditures + \
                            management + electricity + water + sewer + garbage + gas
        
        # Calculating monthly cashflow
                total_monthly_cashflow = total_monthly_income - total_monthly_expense
                self.current_user.rental_properties[address]["Cashflow"] = total_monthly_cashflow

        # Adding Investment information
                print("\nAdding Investment information for the property")
                print("Enter only whole numbers with no commas (ex: 15000)")
                self.current_user.rental_properties[address]["Investments"] = {}
                downpayment = int(input("How much was your downpayment for the property?: "))
                self.current_user.rental_properties[address]["Investments"]["Downpayment"] = downpayment
                closing_cost = int(input("How much was the closing cost?: "))
                self.current_user.rental_properties[address]["Investments"]["Closing Cost"] = closing_cost
                rehab = int(input("Any rehab/renovations done to the property?: Enter 0 if none was done: "))
                self.current_user.rental_properties[address]["Investments"]["Rehab Budget"] = rehab
                misc_investment = int(input("Any other miscellaneous investments done for the property? Enter 0 if none was done: "))
                self.current_user.rental_properties[address]["Investments"]["Misc Investments"] = misc_investment

                total_investments = downpayment + closing_cost + rehab + misc_investment

        # Totals added to list
                self.current_user.rental_properties[address]["Total Monthly Income"] = total_monthly_income
                self.current_user.rental_properties[address]["Total Monthly Expenses"] = total_monthly_expense
                self.current_user.rental_properties[address]["Total Investments"] = total_investments

        # Calculating ROI
                annual_cashflow = total_monthly_cashflow * 12
                roi = round(float(annual_cashflow / total_investments) * 100, 3)
                self.current_user.rental_properties[address]["ROI"] = roi
                print("\n===========================================")
                print(f"Your ROI for {address} is:  {roi}%\n")
                print(f"{address}'s info: \n")
                print(self.current_user.rental_properties[address])
                break

            except ValueError:
                print("\nInvalid input!  Starting over... Please enter a whole number with no commas.  Example: 1000")


    def view_properties(self):
        if self.current_user.rental_properties == {}:
            print("You dont have any properties in your list.")
        else:
            for i in self.current_user.rental_properties:
                print(i)
                print(self.current_user.rental_properties[i])
                print("\n")

       
    def remove_property(self):
        if self.current_user.rental_properties == {}:
            print("You dont have any properties in your list.")
        else:
            print("\nYour current list of properties: ")
            self.view_properties()

            choice = input("Which property would you like to remove from your list? ").title()
            for i in self.current_user.rental_properties:
                if i.title() == choice:
                    del self.current_user.rental_properties[i]
                    print(f"{choice.title()} has been removed from your properties list.")
                    break

    
    def update_property(self):

        if self.current_user.rental_properties == {}:
            print("You dont have any properties in your list.")
            
        else: 
            print("\nYour current list of properties: ")
            self.view_properties()

            choice = input("Which property would you like to update? ").title()
            for i in self.current_user.rental_properties:
                if i.title() == choice:
                    update = input("What would you like to update? Income/Expenses/Investments ").lower().strip()

                    # updating icome portion only
                    if update == "income":
                        print("\nEnter only whole numbers with no commas (ex: 15000)")
                        while True:                          
                            try:    
                                rental_income = int(input("What is the monthly rental income?: "))
                                self.current_user.rental_properties[i]["Income"]["Rental Income"] = rental_income
                                laundry = int(input("Any monthly laundry income? Enter 0 if there is none: "))
                                self.current_user.rental_properties[i]["Income"]["Laundry"] = laundry
                                storage = int(input("Any monthly storage income? Enter 0 if there is none: "))
                                self.current_user.rental_properties[i]["Income"]["Storage"] = storage
                                misc_income = int(input("Any other monthly miscellaneous income? Enter 0 if there is none: "))
                                self.current_user.rental_properties[i]["Income"]["Misc Income"] = misc_income
                                total_monthly_income = rental_income + laundry + storage + misc_income
                                self.current_user.rental_properties[i]["Total Monthly Income"] = total_monthly_income
                                self.current_user.rental_properties[i]["Cashflow"] = total_monthly_income - self.current_user.rental_properties[i]["Total Monthly Expenses"]
                                roi = round(float(self.current_user.rental_properties[i]["Cashflow"] * 12 / self.current_user.rental_properties[i]["Total Investments"]) * 100, 3)
                                self.current_user.rental_properties[i]["ROI"] = roi
                                print("Your Income information has been updated.\n")
                                print(i)
                                print(self.current_user.rental_properties[i])
                                break

                            except ValueError:
                                print("\nInvalid input!  Starting over... Please enter a whole number with no commas.  Example: 1000\n")
                            
                    # updating expenses portion only
                    elif update == "expenses":
                        print("\nEnter only whole numbers with no commas (ex: 15000)")
                        while True:
                            try:
                                mortgage = int(input("How much is the monthly mortgage?: "))
                                self.current_user.rental_properties[i]["Expenses"]["Mortgage"] = mortgage
                                tax = int(input("What is the monthly property tax of this property?: "))
                                self.current_user.rental_properties[i]["Expenses"]["Tax"] = tax
                                insurance = int(input("How much is the monthly insurance fee?: "))
                                self.current_user.rental_properties[i]["Expenses"]["Insurance"] = insurance
                                hoa = int(input("Any monthly HOA fees? Enter 0 if there is none: "))
                                self.current_user.rental_properties[i]["Expenses"]["HOA Fee"] = hoa
                                lawn = int(input("Any monthly lawn/snow fees? Enter 0 if there is none: "))
                                self.current_user.rental_properties[i]["Expenses"]["Lawn/Snow Care Fee"] = lawn
                                vacancy = int(input("How much is your monthly vacancy estimate? (Usually 5% of your rental income): "))
                                self.current_user.rental_properties[i]["Expenses"]["Vacancy"] = vacancy
                                repair = int(input("How much would you want to save aside monthly for any surprise repair fees (ex: carpet cleaning, fixing a hole in the wall, etc.)?: "))
                                self.current_user.rental_properties[i]["Expenses"]["Repair Savings"] = repair
                                capital_expenditures = int(input("How much would you want to save aside monthly for bigger surprise repairs (ex: new roof, new water heater, etc.): ? "))
                                self.current_user.rental_properties[i]["Expenses"]["Capital Expenditures"] = capital_expenditures
                                management = int(input("Any monthly rental management fees? Enter 0 if there is none: "))
                                self.current_user.rental_properties[i]["Expenses"]["Rental Management"] = management
                                print("Adding MONTHLY Utility expenses")
                                self.current_user.rental_properties[i]["Expenses"]["Utility"] = {}
                                electricity = int(input("How much is the monthly elecricity bill? Enter 0 if none or tenant pays for it: "))
                                self.current_user.rental_properties[i]["Expenses"]["Utility"]["Electricity"] = electricity
                                water = int(input("How much is the monthly water bill? Enter 0 if none or tenant pays for it: "))
                                self.current_user.rental_properties[i]["Expenses"]["Utility"]["Water"] = water
                                sewer = int(input("How much for monthly sewer bill? Enter 0 if none or tenant pays for it: "))
                                self.current_user.rental_properties[i]["Expenses"]["Utility"]["Sewer"] = sewer
                                garbage = int(input("How much for monthly garbage fees? Enter 0 if none or tenant pays for it: "))
                                self.current_user.rental_properties[i]["Expenses"]["Utility"]["Garbage"] = garbage
                                gas = int(input("How much for is the monthly gas bill? Enter 0 if none or tenant pays for it: "))
                                self.current_user.rental_properties[i]["Expenses"]["Utility"]["Gas"] = gas
                                total_monthly_expense = mortgage + tax + insurance + hoa + lawn + vacancy + repair + capital_expenditures + \
                                        management + electricity + water + sewer + garbage + gas
                                self.current_user.rental_properties[i]["Total Monthly Expenses"] = total_monthly_expense
                                self.current_user.rental_properties[i]["Cashflow"] = self.current_user.rental_properties[i]["Total Monthly Income"] - total_monthly_expense
                                roi = round(float(self.current_user.rental_properties[i]["Cashflow"] * 12 / self.current_user.rental_properties[i]["Total Investments"]) * 100, 3)
                                self.current_user.rental_properties[i]["ROI"] = roi
                                print("Your Expenses information has been updated.\n")
                                print(i)
                                print(self.current_user.rental_properties[i])
                                break

                            except ValueError:
                                print("\nInvalid input!  Starting over... Please enter a whole number with no commas.  Example: 1000\n")

                    # updating investments portion only
                    elif update == "investments":
                        print("\nEnter only whole numbers with no commas (ex: 15000)")
                        while True:
                            try:
                                downpayment = int(input("How much was your downpayment for the property?: "))
                                self.current_user.rental_properties[i]["Investments"]["Downpayment"] = downpayment
                                closing_cost = int(input("How much was the closing cost?: "))
                                self.current_user.rental_properties[i]["Investments"]["Closing Cost"] = closing_cost
                                rehab = int(input("Any rehab/renovations done to the property?: Enter 0 if none was done: "))
                                self.current_user.rental_properties[i]["Investments"]["Rehab Budget"] = rehab
                                misc_investment = int(input("Any other miscellaneous investments done for the property? Enter 0 if none was done: "))
                                self.current_user.rental_properties[i]["Investments"]["Misc Investments"] = misc_investment
                                total_investments = downpayment + closing_cost + rehab + misc_investment
                                self.current_user.rental_properties[i]["Total Investments"] = total_investments
                                roi = round(float(self.current_user.rental_properties[i]["Cashflow"] * 12 / total_investments) * 100, 3)
                                self.current_user.rental_properties[i]["ROI"] = roi
                                print("Your Investment information has been updated.\n")
                                print(i)
                                print(self.current_user.rental_properties[i])
                                break

                            except ValueError:
                                print("\nInvalid input!  Starting over... Please enter a whole number with no commas.  Example: 1000\n")
            
                else: 
                    print("Did not find this property in your list.  Please check spelling and try again.")

        

    
    def run(self):
        print("=====Rental Property Calculator=====")

        if self.users:
            self.login_user()
        else:
            self.add_user()

        while True:
            pick = input("\nWhat would you like to do? Add User / Update User / Login / Logout / Add Property / Remove Property / Update Property / View Properties / Quit: ")

            if pick.lower() == "add user":
                self.add_user()
            elif pick.lower() == "update user":
                self.update_user()
            elif pick.lower() == "login":
                self.login_user()
            elif pick.lower() == "logout":
                self.logout()
                response = input("What would you like to do next? Login / Add User / Quit ")
                if response.lower() == "login":
                    self.login_user()
                elif response.lower() == "add user":
                    self.add_user()
                elif response.lower() == "quit":
                    print("=====Thanks for using Rental Property Calculator!=====")
                    break

            elif pick.lower() == "add property":
                self.add_to_properties()
            elif pick.lower() == "remove property":
                self.remove_property()
            elif pick.lower() == "update property":
                self.update_property()
            elif pick.lower() == "view properties":
                self.view_properties()
            elif pick.lower() == "quit":
                print("=====Thanks for using Rental Property Calculator!=====")
                break
            else:
                print("Invalid input.  Please enter from the list given.")



calculator = Rental()
calculator.run()
