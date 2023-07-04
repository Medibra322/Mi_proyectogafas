import mysql.connector

def connectdb():
    try:
        conn = mysql.connector.connect(
            host='containers-us-west-151.railway.app',
            port=6066,
            user='root',
            password='AjmT0AtsX6cBIvrqxnIC',
            database='railway'
    )
        print('Connecting to railway')

    except Exception as e:
        print(f'Error connecting to railway: {e}')

    return conn

connectdb()