import mysql.connector
config={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"order"
}
con=mysql.connector.connect(**config)
username="1 OR 1=1"
password="1 OR 1=1"
sql="SELECT COUNT(*) FROM jd_order WHERE amount=%s " \
    "AND AES_DECRYPT(UNHEX(create_user),'HelloWorld')=%s";
cursor=con.cursor()
cursor.execute(sql,(username,password))
print(cursor.fetchone()[0])
con.close()




