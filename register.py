#!C:/python/python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>welcome to mypage</h1>")


Form=cgi.FieldStorage()
FName=Form.getvalue("name")
FPassword=Form.getvalue("password")


#print("<h1>",FName,FPassword,"</h1>")

print("Record stored... Thank you for register Mr/Ms",FName,FPassword);

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="amazon"
    )
mycursor=mydb.cursor();
sql="INSERT INTO users(Name,Password)VALUES(%s,%s)";
val=(FName,FPassword);
mycursor.execute(sql,val)
mydb.commit()
print("</body>")
print("</html>")
