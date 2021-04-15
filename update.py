import requests
Token = input('Enter Your Token Bot')
API_URL = 'https://api.telegram.org/bot'+Token+'/'
def getupdate(offset):
  update = requests.get(API_URL+'getupdates?offset='+str(offset)+'&limit=1')
  return update.json()['result'][0]
def run(update):
 print(update)
update_id = 0
while True:
  try:
	  update = getupdate(update_id+1)
	  run(update)
	  update_id = int(update['update_id'])
  except:
    continue

