import mysql.connector
con=mysql.connector.connect(
    host="localhost",port="3306",
    user="root",password="123456",
    database="order"
)
cursor=con.cursor()
sql="SELECT amount,status,create_time FROM jd_order;"
cursor.execute(sql)
for one in cursor:
    print(one[0],one[1],one[2])
con.close()