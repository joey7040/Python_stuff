import boto3
import json
from json import load, dump
import sys
sess = boto3.session.Session()
cog_client = sess.client('cognito-idp','us-east-1')
rds_client = sess.client('rds','us-east-1')
cfn_client = sess.client('cloudformation','us-east-1')
secret_client = sess.client('secretsmanager','us-east-1')






def get_original():
    with open('/home/jrivera/PycharmProjects/Development/ironsaferestapi/ironsafe/settings/OriginalConfig.json', 'r') as fin:
        og = load(fin)
    return og

pool = sys.argv[1]
secretname = sys.argv[2]


def get_poolid():
    pool_dict = cog_client.list_user_pools(MaxResults=20)
    print('pool id = ' , pool_dict['UserPools'][1]['Id'])
    return "".join(pool_dict['UserPools'][1]['Id'])


def get_clientid(pool):
    client_dict = cog_client.list_user_pool_clients(UserPoolId=pool)
    print('got client id', client_dict['UserPoolClients'][0]['ClientId'])
    return "".join(client_dict['UserPoolClients'][0]['ClientId'])


def get_domain(pool):
    client_dict = cog_client.describe_user_pool(UserPoolId=pool)
    print('got domain')
    return "".join(client_dict['UserPool']['Domain'])


def get_callbackurl(pool, client_id):
    call_url_dict = cog_client.describe_user_pool_client(UserPoolId=pool, ClientId=client_id)
    print('got callback url')
    return"".join(call_url_dict['UserPoolClient']['CallbackURLs'])




def make_new(og):
    cid = get_clientid(pool)
    og['userpool_id'] = pool
    og['secret'] = secretname
    client_id = get_clientid(pool)
    og['app_client_id'] = client_id
    og['domain'] = get_domain(pool)
    og['cb_url'] = get_callbackurl(pool, client_id)
    with open('/home/jrivera/PycharmProjects/Development/ironsaferestapi/ironsafe/settings/newConfig.json', 'w+') as fout:
        json.dump(og ,fout)
    return og



og = get_original()
make_new(og)



""" 
Appends the orginal config dictionary with credit union specific configurations.
it creates a new config and uses that for the configurations. 
fullconfig.json is created if it dosen't exist at run time and that is what is used for ironsafe.
"""
