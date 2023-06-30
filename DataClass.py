import json
import os
import random
from abc import ABC, abstractmethod


class DataHandler:

    def __addData(self, file_name: str, table: str, details: dict)->str:

        if self.isAnExistingUser(details["Username"]):
            return False
        
        with open(file_name, "r+") as file:         
            data = json.load(file)
            data[table].append(details)
            file.seek(0)
            json.dump(data, file, indent=4)
            return True
            
    
    def addSavingAccountUser(self, full_name: str, username: str, password: str, email: str, phone:str\
        , account_id: str, balance: float, amount: float):
        
        data : dict = { 
                        "Name": full_name,
                        "Username": username,
                        "Password": password,
                        "Email": email,
                        "Phone": phone,
                        "AccountID": account_id,
                        "Balance": balance,
                        "Amount": amount
                        }
        return self.__addData("Users.json", "SavingAccountUser", data)
        
      
    def addCheckingAccountUser(self, full_name: str, username: str, password: str, email: str, phone:str\
        , account_id: str, balance: float, credit_limit: float, repayment_deadline: str):
        
        data : dict = { 
                        "Name": full_name,
                        "Username": username,
                        "Password": password,
                        "Email": email,
                        "Phone": phone,
                        "AccountID": account_id,
                        "Balance": balance,
                        "CreditLimit": credit_limit,
                        "RepaymentDeadline": repayment_deadline
                        }
        return self.__addData("Users.json", "CheckingAccountUser", data)
             
    
    def addLoanAccountUser(self, full_name: str, username: str, password: str, email: str, phone:str\
        , account_id: str, loan_taken: float, amount_repayed: float, repayment_deadline: str):
        
        data : dict = { 
                        "Name": full_name,
                        "Username": username,
                        "Password": password,
                        "Email": email,
                        "Phone": phone,
                        "AccountID": account_id,
                        "LoanTaken": loan_taken,
                        "RepaymentDeadline": amount_repayed,
                        "AmountRepayed": repayment_deadline
                        }
        return self.__addData("Users.json", "LoanAccountUser", data)

    
    def __dataChecker(self, file_name: str, table: str, key: str, value: str) -> tuple:
        with open(file_name, "r") as file:
            database = json.load(file)
            results: list
            for data in database[table]:
                if value.upper() in data.get(key).upper():
                    results.append(data)
                    
            return results
        
        
    def isAnExistingUser(self, username: str) -> bool:
        if self.__dataChecker("User", "Username", username):
            return True
        else:
            return False
            
                             
    def getUsersData(self, username: str):
        return self.__dataChecker("Username", username)



    def updateUsersData(self, new_data: dict):
        with open(self.file_name, "r+") as file:
            database = json.load(file)
            for user in database["Users"]:
                if new_data.get("Username") == user.get("Username"):
                    updated_data = user
                    del user
                    
            for change in new_data:
                updated_data[change] = new_data[change]
                
            database["Users"].append([updated_data])
            json.dump(database, indent=4)
            
            return "Field Successfully Changed."
                   
    def getUsersTransactionHistory(self, username: str):
        return self.__dataChecker("Transactions", "SenderName", username)        


d = DataHandler()
