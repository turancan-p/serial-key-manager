import subprocess
import bcrypt


def get_id():
    customer_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    return customer_id


def create_private():
    private_key = bcrypt.gensalt()
    return private_key