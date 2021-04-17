import requests
Token = input('Enter Your Token Bot:')
API_URL = 'https://api.telegram.org/bot'+Token+'/'
def getupdate(offset):
  update = requests.get(API_URL+'getupdates?offset='+str(offset)+'&limit=1')
  return update.json()['result'][0]
def sendmessage(chat_id,text):
	url = requests.get(API_URL+'sendmessage?chat_id='+str(chat_id)+'&text='+str(text))
	return url.json()
update_id = 0
while True:
 try:
   update = getupdate(update_id+1)
   print(update)
   update_id = int(update['update_id'])
 except:
  continue
