from flask import Flask, request, render_template
import requests
import addressbook
app = Flask(__name__)

def getContacts():
    URL = 'https://randomuser.me/api/?nat=us&results=25'

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

myAddressBook = addressbook.AddressBook()
newContacts = getContacts()

for contact in newContacts['results']:
    first = contact['name']['first']
    last = contact['name']['last']
    email = contact['email']
    phone = contact['phone']
    photo = contact['picture']['thumbnail']

    newContact = addressbook.Contact(first, last, email, phone, photo)
    myAddressBook.addAddress(newContact)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html', contacts=myAddressBook.addresses)

@app.route("/search", methods=['POST'])
def search():
    searchField = request.form.get('search')
    results = myAddressBook.findAllMatching(searchField)
    return render_template('index.html', contacts=results)

if __name__ == "__main__":
    app.run()