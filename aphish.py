import requests, time
dirs = ['/usernames.txt', '/ip.txt', '/saved.usernames.txt', '/saved.ip.txt', '/victim_ip.txt', '/login_info.txt', '/save.txt', '/log.txt', '/data.txt', '/data.log', '/login.txt']
tr = 0
print("""
 _______            _ ______  _     _      _
(_______)       _  (_|_____ \| |   (_)    | |
 _______ ____ _| |_ _ _____) ) |__  _  ___| |__
|  ___  |  _ (_   _) |  ____/|  _ \| |/___)  _ \.
| |   | | | | || |_| | |     | | | | |___ | | | |
|_|   |_|_| |_| \__)_|_|     |_| |_|_(___/|_| |_|
Termux-Lab             |           t.me/termuxlab
""")
urls = input("afish[url]> ")
print("Поиск...")
if urls == '':
    print("0")
else:
    for i in range(len(dirs)-1):
        r = requests.get(urls+dirs[i])
        if r.status_code  == 200:
            print(r.text)
            tr+=1
        time.sleep(1)
print('\n\n')
if tr == 0:
    print("Не удалось ничего найти \n1/Если ссыка не от ngrok, то попробуйте утилиту Weber\n-- https://github.com/termux-lab/weber --\n\n2/Сообщите нам в Telegram @termuxlab")
else:
    print("найдено результатов", tr)
