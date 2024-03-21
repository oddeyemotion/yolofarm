import pyodbc

try:
    conn = pyodbc.connect(
    '''
    DRIVER={ODBC Driver 17 for SQL Server};
    SERVER=DESKTOP-7CB1RAA;
    DATABASE=yolofarm;
    Trusted_Connection=yes;
    '''
    )

    cursor = conn.cursor()

    cursor.execute("SELECT 1 AS test_value")
    result = cursor.fetchone()

    if result[0] == 1:
        print("Connection successful!")
    else:
        print("Unexpected query result.")

except pyodbc.Error as ex:
    print("Error connecting to database:", ex)

finally:
    # Close the connection if opened
    if conn:
        conn.close()

    