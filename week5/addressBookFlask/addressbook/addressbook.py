class Contact():
    def __init__(self, firstname, lastname, email, phone, photo):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.photo = photo
    
    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone

    def getPhoto(self):
        return self.photo

    def __str__(self):
        magStr = f'{self.firstname} {self.lastname}'
        magStr += f' ({self.email})'
        return magStr

    def __repr__(self):
        magStr = f'{self.firstname} {self.lastname}'
        magStr += f' ({self.email})'
        return magStr
        
class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            
            if address.getFirstname().lower().startswith(searchStr.lower()) or address.getLastname().lower().startswith(searchStr.lower()):
                results.append(address)
                
        return results