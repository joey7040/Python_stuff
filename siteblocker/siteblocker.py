import time
from datetime import datetime as dt 

hosts_temp='hosts'

hosts_path='C:\Windows\System32\drivers\etc\hosts
redirect = '127.0.0.1'
sites_that_kill_time = ['www.facebook.com', 'facebook.com', 'www.twitter.com', 'twitter.com']

print(dt.now())
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,16) < dt(dt.now().year, dt.now.month, dt.now().day,17):
        print('working hours: ')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in sites_that_kill_time:
                if site in content:
                    pass
                else:
                    file.write(redirect+' '+site+'\n')
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites_that_kill_time):
                    file.write(line)
            file.truncate()
        print('time to play!!!')
    time.sleep(600)

