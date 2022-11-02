import bcrypt
import mysql.connector
from generate_key import get_hwid, get_secret_key, hashed_password

user_db = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'users',
    'raise_on_warnings': True
}


# USER_DB
def username_check(userName):
    select_command = f"SELECT * FROM userdata WHERE userName = '{userName}'"

    cnx = mysql.connector.connect(**user_db)
    cursor = cnx.cursor()

    cursor.execute(select_command)

    for user_name in cursor:
        print(user_name[1])
        if user_name[1] == userName:
            cursor.close()
            cnx.close()
            return True
    cursor.close()
    cnx.close()
    return False


def get_secret_key_for_user(username):
    select_command = f"SELECT * FROM userdata WHERE userName = '{username}'"
    cnx = mysql.connector.connect(**user_db)
    cursor = cnx.cursor()

    cursor.execute(select_command)
    for user in cursor:
        if username in user:
            user_secret = user[4]
            return user_secret
    return None


def register(userName, userPassword):
    can_use = username_check(userName)
    if can_use:
        print("Use a different username!")
        return
    else:
        insert_command = f"INSERT INTO userdata (userName, userPassword, userHwid, userSecret, authorization) VALUES (%s, %s, %s, %s, %s)"

        cnx = mysql.connector.connect(**user_db)
        cursor = cnx.cursor()

        userHwid = get_hwid()
        userSecret = get_secret_key()
        hashedPassword = hashed_password(userPassword, userSecret)
        values = (userName, str(hashedPassword.decode("utf-8")), userHwid, userSecret, "Member")

        cursor.execute(insert_command, values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return True


def login_check(username, password):
    select_command = f"SELECT * from userdata WHERE userName = '{username}';"
    cnx = mysql.connector.connect(**user_db)
    cursor = cnx.cursor()
    cursor.execute(select_command)

    for user in cursor:
        if username in user:
            password = str.encode(password)
            user_passwd = user[2]

            user_hwid = user[3]
            comp_hwid = get_hwid()

            user_passwd = user_passwd.encode("utf-8")

            if bcrypt.checkpw(password, user_passwd):
                if user_hwid == comp_hwid:
                    print("login success")
                    return user
                else:
                    print("you cannot login another pc")
                    return False
            else:
                print("Id or Password is wrong!")
                return False
    print("Id Or Password is wrong!")
    return False


def delete_all():
    delete_command = f"TRUNCATE TABLE userdata"
    cnx = mysql.connector.connect(**user_db)
    cursor = cnx.cursor()

    cursor.execute(delete_command)
    cursor.close()
    cnx.close()


# KEY_DB
key_db = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'serial_keys',
    'raise_on_warnings': True
}


def add_key(userName, userKey, createDate, expDate):
    can_use = username_check(userName)
    if not can_use:
        print("User is doesn't exist")
        return False
    else:
        insert_command = f"INSERT INTO keydata (userName, userKey, createDate, expDate) VALUES (%s, %s, %s, %s)"

        cnx = mysql.connector.connect(**key_db)
        cursor = cnx.cursor()
        print(userName, userKey, createDate, expDate)
        values = (userName, userKey, createDate, expDate)

        cursor.execute(insert_command, values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return True


def get_all_key_data():
    select_command = "SELECT * FROM keydata"

    cnx = mysql.connector.connect(**key_db)
    cursor = cnx.cursor()

    cursor.execute(select_command)

    result = cursor.fetchall()

    return result
