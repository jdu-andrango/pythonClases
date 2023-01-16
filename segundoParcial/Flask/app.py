from flask import Flask
from psycopg2 import connect


app= Flask(__name__)

host='localhost'
port=5432
database= 'pruebaConexion'
user='postgres'
password='david'


def getConnection():
    conn = connect(host=host,port=port,database=database,user=user, password=password)
    return conn

@app.get('/')
def home():
    conn=getConnection()
    cur=conn.cursor()

    cur.execute("SELECT 1+1 ")
    result=cur.fetchone()
    print(result)


    return '<h1>hola mundo</h1>'

if __name__ == '__main__':
    app.run(debug=True)    