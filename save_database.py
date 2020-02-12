import struct,socket
import sqlite3 as lite
from sqlite3 import Error
UDP_IP = "169.254.9.218"
UDP_PORT = 4123
def packet_from_UDP(ip,port):
    try:
        data_output = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data_output.bind((ip, port))
        packet, addr = data_output.recvfrom(64)
        data_str= struct.Struct('i3ffff3f3f3i')
        data = data_str.unpack(packet)
        return data
    except:
        print("Cannot recv data from UDP")
def create_connetion(db_file):
    conn = None
    try:
        conn = lite.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
def create_table(conn,create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
        conn.commit()
        return 1
    except Error as e:
        print(e)
def insert_data(conn,func_ins_sql,data):
    try:
        cur = conn.cursor()
        cur.execute(func_ins_sql,data)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
# delete old data
database = r"C:\Users\CuongBui\PycharmProjects\dulieuNFS\LFS.db"
conn = create_connetion(database)
try:
    cur = conn.cursor()
    cur.execute(" DROP TABLE datas;")
    conn.commit()
except:
    print("tables not found")
# create new tables
create_sql_database_lfs = """ CREATE TABLE IF NOT EXISTS datas (
                            id INTEGER PRIMARY KEY,
                            time INTEGER NOT NULL,
                            Angvel_X REAL NOT NULL,
                            AngVel_Y REAL NOT NULL,
                            AngVel_Z REAL NOT NULL,
                            Heading REAL NOT NULL,
                            Pitch REAL NOT NULL,
                            Roll REAL NOT NULL,
                            Accel_X REAL NOT NULL,
                            Accel_Y REAL NOT NULL,
                            Accel_Z REAL NOT NULL,
                            Vel_X REAL NOT NULL,
                            Vel_Y REAL NOT NULL,
                            Vel_Z REAL NOT NULL,
                            Pos_X REAl NOT NULL,
                            Pos_Y REAL NOT NULL,
                            Pos_Z REAL NOT NULL
                            );"""
create_table(conn, create_sql_database_lfs)
insert_sql = "INSERT INTO datas (time, Angvel_X,Angvel_Y,AngVel_Z,Heading,Pitch,Roll,Accel_X,Accel_Y,Accel_Z,Vel_X,Vel_Y,Vel_Z,Pos_X,Pos_Y,Pos_Z)" \
             "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
while True:
    data = packet_from_UDP(UDP_IP,UDP_PORT)
    insert_data(conn, insert_sql, data)
