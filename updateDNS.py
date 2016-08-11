from godaddypy import Client, Account
import ipgetter
import config


PUBLIC_KEY = config.PUBLIC_KEY
SECRET_KEY = config.SECRET_KEY

my_acct = Account(api_key=PUBLIC_KEY, api_secret=SECRET_KEY)
client = Client(my_acct)

x = client.get_domains()
print client.get_records(x[0], record_type='A', name='@')

ext_ip = ipgetter.myip()

print ext_ip
