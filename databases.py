import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='localhost',
                             user='root',
                             password='12345678',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

conn.cursor().execute('drop database if exists django_hms')

conn.cursor().execute('create database django_hms')

conn.select_db("django_hms")

# conn.cursor().execute('''create table django_hms.data_hms (
#     id      int     not null,
#     nama    varchar(200)    not null,
#     tgl_lahir   varchar(200),
#     alamat varchar(1000),
#     height  int,
#     weight  int,
#     gender varchar(100),
#     tgl_masuk varchar(200),
#     diagnosis varchar(1000),
#     bed     int,
#     primary key (id)
# ) engine = innodb;''')