from dbm import _Database
import getpass
database = {"doe.john": "123456", "doe.john": "654321"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Username : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Please enter password again : ")
        break
print("verified")