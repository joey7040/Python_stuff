# import boto3
# import os
# import json
# import sys
# import secret_maker
# from json import load, dump
# import subprocess

# def get_data():
#     with open('./directorys/location/', 'r') as fin:
#         data = load(fin)
#     return data


# def insert_db_seed():
  
#     obj = get_data()
#     parameter = obj["secretFromSecretManager"]
#     data = secret_maker.get_secret(parameter)
#     uname = data['username']
#     endpoint = data['host']
#     pwd = data['password']

#     Cmd = "mysql -h"+endpoint+" -u "+uname+" -D DatabaseName"+" -p\"{pwd}\"".format(pwd=pwd)+" < /location/of/your/file."
#     print("Inserting Database.")
#     subprocess.call(Cmd, shell=True)


# insert_db_seed()

