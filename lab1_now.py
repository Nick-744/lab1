import requests # Εισαγωγή της βιβλιοθήκης
from datetime import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

    return;

'''
- Example:

url = 'http://python.org/' # προσδιορισμός του url
with requests.get(url) as response: # το αντικείμενο response
    html = response.text
    more(html)
'''

# Ερώτημα 1ο - Ζητάει από τον χρήστη ένα URL:
url = input("- Give url: ")
http_start = "https://"
if not url.startswith(http_start):
    url = http_start + url
print(url)

# Ερώτημα 2ο - Πραγματοποιεί ένα αίτημα HTTP σε αυτό το URL:
with requests.get(url) as response:
    # Ερώτημα 3ο - Τυπώνει τις κεφαλίδες (headers) της απόκρισης HTTP:
    print(f"\n- Κεφαλίδες της απόκρισης HTTP:")
    for key in response.headers:
        print(f"Name: {key}, Value: {response.headers[key]}")
    
    # Ερώτημα 4ο - Τροποποιήστε τον κώδικα ώστε να απαντάει για το
    #              URL που έδωσε ο χρήστης με τις εξής πληροφορίες:
    '''
    α) Ποιο είναι το λογισμικό που χρησιμοποιεί ο εξυπηρετητής (ο web server)
       για να απαντήσει στο αίτημα;
    '''
    print(f"\nServer: {response.headers.get('Server')}")

    '''
    β) Αν η σελίδα χρησιμοποιεί cookies, και αν ναι:
    '''
    print(f"\nHas cookies: {'Set-Cookie' in response.headers}")

    '''
    γ) Το όνομα κάθε cookie και για πόσο διάστημα θα είναι έγκυρο:
    '''
    print("\nMore info about cookies:")
    for cookie in response.cookies:
        print(f"Name: {cookie.name}, Expires: {datetime.fromtimestamp(cookie.expires)}")