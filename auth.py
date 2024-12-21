import bcrypt
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb+srv://tintin:tintin@cluster0.qot4y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["health_bot_db"]
users_collection = db["users"]


def hash_password(password):
    """Hash a password for storing."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def check_password(hashed_password, plain_password):
    """Check if a plain password matches the hashed password."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)


def signup_user(username, password):
    """Sign up a new user."""
    if users_collection.find_one({"username": username}):
        return False, "Username already exists!"

    hashed_password = hash_password(password)
    users_collection.insert_one({"username": username, "password": hashed_password})
    return True, "User registered successfully!"


def login_user(username, password):
    """Log in a user."""
    user = users_collection.find_one({"username": username})
    if user and check_password(user["password"], password):
        return True, "Login successful!"
    return False, "Invalid username or password!"
