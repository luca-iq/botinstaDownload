import requests
import telebot
from user_agent import generate_user_agent
import secrets

username = ''
password = ''

cookie = secrets.token_hex(8) * 2
url = 'https://www.instagram.com/accounts/login/ajax/'
head = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate,br',
    'Accept-Language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '325',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '8ddbbd59d8414ad78ddbbd59d8414ad7',
    'Host': 'www.instagram.com',
    'Origin': 'https://www.instagram.com',
    'Referer': 'https://www.instagram.com/',
    'sec-ch-ua': '"Chromium";v="94","MicrosoftEdge";v="94",";NotABrand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': generate_user_agent(),
    'X-ASBD-ID': '198387',
    'X-CSRFToken': '0aVmGdk3XzL4b0yeXnlFXedsBdwrPDw2',
    'X-IG-App-ID': '936619743392459',
    'X-IG-WWW-Claim': '0',
    'X-Instagram-AJAX': '1f85c4f74473',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' + password,
    'username': username,
    'queryParams': '{}',
    'optIntoOneTap': 'false',
    'stopDeletionNonce': '',
    'trustedDeviceRecords': '{}',
}

re = requests.Session()
x = re.post(url, headers=head, data=data)
print(x.text)
try:

    bot = telebot.TeleBot("1404843672:AAE8fg2AGPmZYdX9-o0PD8x7RYWxIG68jjE")


    @bot.message_handler(commands='start')
    def welcome(message):
        bot.reply_to(message, 'welcome\nماذا تريد التحميل\n/vidoe')


    @bot.message_handler(commands='vidoe')
    def send_link(message):
        bot.reply_to(message, 'ارسل رابط الفيديو')

        @bot.message_handler(func=lambda m: True)
        def send_vido(message):
            if 'https://' in message.text:
                me = message.text
                o = str(me).split('?')[0]
                if '"status":"ok"' in x.text:
                    urlw = o + '?__a=1'
                    print(urlw)
                    vi = re.get(url=urlw)
                    try:

                        url_video = \
                        vi.json()["graphql"]["shortcode_media"]["edge_sidecar_to_children"]["edges"][0]["node"][
                            "video_url"]

                        try:
                            bot.send_video(message.chat.id, url_video)

                        except:
                            bot.messages(message.chat.id, url_video)
                            pass
                    except:

                        try:
                            uu = vi.json()["graphql"]["shortcode_media"]["video_url"]
                            bot.send_video(message.chat.id, uu)
                        except:
                            pass
except:
    pass

bot.polling()
