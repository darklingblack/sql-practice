import pyodbc

# Path where you want to create the new database
db_path = r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPytonTraining\Programming for Biologists\assignment2_yourname.accdb'

# Create a connection to the Access database engine

conn_str = r'Driver={ODBC Driver 17 for SQL Server}';DBQ={db_path};CREATE_DBV2=1;'

try:
    conn = pyodbc.connect(conn_str) # Connect to the database (this will create a new one if it doesn't exist)
    conn.close() # Close the connection
    print(f"MS Access database '{db_path}' created successfully.")
except pyodbc.Error as e:
    print(f"Error creating MS Access database: {e}")

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor() # Create a cursor object to execute SQL queries
    create_table_sql = '''
        CREATE TABLE SurveysByHand (
            ID AUTOINCREMENT PRIMARY KEY,
            SampleID TEXT,
            Plot INTEGER,
            Year INTEGER,
            Species TEXT,
            Mass INTEGER,
            HindFoot INTEGER,
            Tag TEXT
        )
        '''

    cursor.execute(create_table_sql)
    conn.commit()

    print("Table 'SurveysByHand' created successfully.")
except pyodbc.Error as e:
    print(f"Error creating table 'SurveysByHand': {e}")
finally:
    if conn: # Close the connection
        conn.close()

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    data = [
        ('21012', 4, 1993, 'DM', 42, 36, '1EA0F9'),
        ('22012', 4, 1995, 'DM', 31, 37, '0D373C'),
        ('23012', 17, 1996, 'DM', 25, 37, '64C6CC'),
        ('24012', 21, 1996, 'PP', 26, 22, '1F511A'),
        ('25012', 22, 1997, 'DM', 53, 35, '2624')


    insert_sql = '''
        INSERT INTO SurveysByHand (SampleID, Plot, Year, Species, Mass, HindFoot, Tag)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    '''

    for row in data:
        cursor.execute(insert_data_sql, row)

    conn.commit()
    print("Data inserted successfully into table 'SurveysByHand'.")
except pyodbc.Error as e:
    print(f"Error inserting data into table 'SurveysByHand': {e}")
finally:
    # Close the connection
    if conn:
        conn.close()