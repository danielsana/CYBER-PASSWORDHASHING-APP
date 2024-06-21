# import hashlib
import hashlib

def hash_password(password):
    # create an object for md5
    hasher = hashlib.md5()
    # hash the password
    hasher.update(password.encode('utf-8'))
    # create a hexadecimal representation
    hashed_password =hasher.hexdigest()
    return hashed_password


# def hash_password_salt(password):
    