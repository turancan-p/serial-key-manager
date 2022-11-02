import subprocess
import bcrypt


def get_hwid():
    user_hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    return user_hwid


def get_secret_key():
    secret_key = bcrypt.gensalt()
    return secret_key


def public_key(key, salt):
    public_key = bcrypt.hashpw(key, salt)
    return public_key


def hashed_password(password, secret_key):
    hashed_pass = bcrypt.hashpw(password, secret_key)
    return hashed_pass
