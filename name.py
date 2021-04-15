import requests
Token = input('Enter Your Token Bot')
API_URL = 'https://api.telegram.org/bot'+Token+'/'
def getupdate(offset):
  update = requests.get(API_URL+'getupdates?offset='+str(offset)+'&limit=1')
  return update.json()['result'][0]
def sendmessage(chat_id,text):
	url = requests.get(API_URL+'sendmessage?chat_id='+chat_id+'&text'+text)
	return url.json()
def run(update):
 print(update)
 message = update['message']
 text = message['text']
 chat_id = message['chat']['id']
 name = message['from']['first_name']
 if text == '/start':
 	sendmessage(chat_id,'''
 🙋🏻‍♂┇ أهلا بك عزيزي '''+name+''' في بوت معاني الاسماء 👬💓

🔱┇ البوت فريد من نوعه ✨😌

🤗┇ ارسل اسمك وانتظر ثانية 😎💞
''')
 else:
 	get = requests.get('https://dev-yhya.tk/api/name/index.php?Name='+text)
	 if get.json()['ok'] == False:
		sendmessage(chat_id,'عذرا عزيزي الاسم الذي أدخلته خاطئ')
	else:
		sendmessage(chat_id,get.json()['meaning'])
update_id = 0
while True:
  try:
	  update = getupdate(update_id+1)
	  run(update)
	  update_id = int(update['update_id'])
  except:
    continue

