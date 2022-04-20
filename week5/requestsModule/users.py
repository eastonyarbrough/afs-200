import requests

class User:
    def __init__(self, firstName, lastName, email, userName, password, userId, homeNum, cellNum, imgLarge, imgSmall):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.userName = userName
        self.password = password
        self.userId = userId
        self.homeNum = homeNum
        self.cellNum = cellNum
        self.imgLarge = imgLarge
        self.imgSmall = imgSmall

    def setName(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def setEmail(self, email):
        self.email = email

    def setUsername(self, userName):
        self.userName = userName

    def setPassword(self, password):
        self.password = password

    def setUserID(self, userID):
        self.userId = userID

    def setNumbers(self, homeNum, cellNum):
        self.homeNum = homeNum
        self.cellNum = cellNum

    def setImages(self, imgLarge, imgSmall):
        self.imgLarge = imgLarge
        self.imgSmall = imgSmall

    def getName(self):
        return f'{self.firstName} {self.lastName}'

    def getEmail(self):
        return self.email

    def getUsername(self):
        return self.userName

    def getPassword(self):
        return self.password

    def getUserID(self):
        return self.userId

    def getNumbers(self):
        return f'Home#: {self.homeNum}, Cell#: {self.cellNum}'

    def getImages(self):
        return f'ImgLarge: {self.imgLarge}, ImgSmall: {self.imgSmall}'

    def __str__(self):
        retStr = f'{self.firstName} {self.lastName}'
        retStr += f' ({self.email})' 
        return retStr

class AuthorizedUsers():
    def __init__(self):
        self.users = []

    def addUser(self, user):
        self.users.append(user)

    def showAuthUsers(self):
        for user in self.users:
            print(user)

def getUserData():
    URL = 'https://randomuser.me/api/?nat=us&results=10'

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

AuthUsers = AuthorizedUsers()
newUsers = getUserData()

for currentUser in newUsers['results']:
    first = currentUser['name']['first']
    last = currentUser['name']['last']
    email = currentUser['email']
    username = currentUser['login']['username']
    password = currentUser['login']['password']
    userid = currentUser['login']['uuid']
    homenum = currentUser['phone']
    cellnum = currentUser['cell']
    imglg = currentUser['picture']['large']
    imgsm = currentUser['picture']['thumbnail']

    newUser = User(first, last, email, username, password, userid, homenum, cellnum, imglg, imgsm)
    AuthUsers.addUser(newUser)

AuthUsers.showAuthUsers()