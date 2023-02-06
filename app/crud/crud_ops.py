from pymongo import MongoClient
from decouple import config
from app.resp_models.model import UserInDB, User
from app.auth.authorization import get_password_hash, verify_password

MONGO_ADMIN = config("mongo_admin")
MONGO_PW = config("mongo_pw")

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def conn_db():
    
    uri = f"mongodb://{MONGO_ADMIN}:{MONGO_PW}@localhost:27017"
    client = MongoClient(uri)

    return client

def insert_user(user : UserInDB):
    client = conn_db()
    db = client.users
    coll = db.users
    cursor_user = coll.find({"$or" : [{"username" : f"{user.username}"}, {"email" : f"{user.email}"}]})
    for p in cursor_user:
        if p:
            return {"message" : "User already created"}
    user.id = coll.count_documents({})
    user.hashed_password = get_password_hash(user.hashed_password) #the password should be encrypted in the front-end
    user_dict = user.dict()
    result = coll.insert_one(user_dict)

    return User(**user_dict)

def get_user(username : str):
    client = conn_db()
    db = client.users
    coll = db.users
    cursor_user = coll.find({"username" : f"{username}"})
    for user in cursor_user:
        if user:
            return UserInDB(**user)
    
