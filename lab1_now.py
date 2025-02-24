import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

#url = 'http://python.org/'  # προσδιορισμός του url

#with requests.get(url) as response:  # το αντικείμενο response
#    html = response.text
#    more(html)

# Ερώτημα 1ο
url = input("Give url:\t")

http_start = "https://"
if not url.startswith("https://"):
    url = "https://" + url

print(url)

# Ερώτημα 2ο
with requests.get(url) as response:
    print(response.text)
