
from flask import Flask
import pyodbc

app = Flask(__name__)

server = '<your_server_name>.database.windows.net'
database = '<your_database_name>'
username = '<your_username>'
password = '<your_password>'
driver = '{ODBC Driver 17 for SQL Server}'

@app.route('/')
def index():
    try:
        with pyodbc.connect(
            f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
        ) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT @@VERSION")
            row = cursor.fetchone()
        return f"Hello from Azure SQL!<br><br>{row[0]}"
    except Exception as e:
        return f"Connection failed: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
