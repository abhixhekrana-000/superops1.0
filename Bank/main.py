
import json
import random
import string
from pathlib import Path

class bank:
    database='data.json'
    data=[]
    try:
      if Path(database).exists():

       with open(database) as fs:
        data=json.load(fs.read())
      else:
        print("no such file exists")
    except Exception as err:
       print(f"exception error as {err}")

    @staticmethod
    def updateaccount():
      with open(bank.database,'w') as fs:
        fs.write(json.dumps(bank.data))



        
    def createaccount(self):
      info={
        "name":input("tell your name:"),
        "age":int(input("tell your age:")),
        "email":input("tell your email:"),
        "pin":int(input("tell your pin:")),
        "accountNo":1234,
        "balance":0
      }
       
      if info['age']<18 or len(str(info['pin']))!=4:
        print("Sorry you can't create your account")
      else:
        print('account has been created succesfully')
        for i in info:
          print(f"{i}:{info[i]}")
        print("please notedown your account number:")
        bank.data.append(info)
        bank.update()
        
          

user=bank()

print("-----WELCOME TO OUR BANK SIR-------")

print("press 1 for creating a account")
print("press 2 for deposing the money in the  bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for  deleting your account")

check=int(input("please enter your response:"))

if check==1:
    user.createaccount()
