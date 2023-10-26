import smtplib
import random
import pymongo
import certifi


temp = "mongodb+srv://gather:gather@cluster0.vo1"
connection = temp + "mev8.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection, tlsCAFile=certifi.where())
db = client["illinigather"]
collection = db["verification"]
col = db["verified"]


def sendVerification(email):
    code = random.randint(11111111, 99999999)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login('illinigather@gmail.com', 'eidmjubametrxhdm')
        server.sendmail('illinigather@gmail.com', email, str(code))
        post = {'email': email, "code": code}
        collection.insert_one(post)
        return True
    except Exception:
        return False


def verify(email, entered_code):
    try:
        code = collection.find_one({"email": email})["code"]
        if int(code) == int(entered_code):
            return True
        else:
            return False
    except Exception:
        return False


def expireCode(email):
    collection.delete_one({"email": email})


def verified(email):
    try:
        verified_email = col.find_one({"email": email})["email"]
        if email == verified_email:
            return True
        else:
            return False
    except Exception:
        return False


def addToVerified(email):
    try:
        post = {'email': email}
        col.insert_one(post)
        return True
    except Exception:
        return False
