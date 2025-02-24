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

# Ερώτημα 1ο - Ζητάει από τον χρήστη ένα URL
url = input("- Give url:\t")

http_start = "https://"
if not url.startswith("https://"):
    url = "https://" + url

print(url)

# Ερώτημα 2ο - Πραγματοποιεί ένα αίτημα HTTP σε αυτό το URL
with requests.get(url) as response:
    # Ερώτημα 3ο - Τυπώνει τις κεφαλίδες (headers) της απόκρισης HTTP
    #print(f"\n- Κεφαλίδες της απόκρισης HTTP:")
    #for key in response.headers:
    #    print(f"Name: {key}, Value: {response.headers[key]}")
    
    # Ερώτημα 4ο - Τροποποιήστε τον κώδικα ώστε να απαντάει για το
    #              URL που έδωσε ο χρήστης με τις εξής πληροφορίες:

    # - Ποιο είναι το λογισμικό που χρησιμοποιεί ο εξυπηρετητής (ο web server)
    # για να απαντήσει στο αίτημα;
    print(f"\nServer: {response.headers.get('Server')}")

    # - Αν η σελίδα χρησιμοποιεί cookies, και αν ναι
    print(f"\nHas cookies: {'Set-Cookie' in response.headers}")

    # - Το όνομα κάθε cookie και για πόσο διάστημα θα είναι έγκυρο.
    print(" ") # Καλύτερη αισθητική
    for cookie in response.cookies:
        print(f"Name: {cookie.name}, Expires:")