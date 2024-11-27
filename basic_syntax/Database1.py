import msaccessdb
import pyodbc

# Path and filename for the new Access database
db_path = r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPytonTraining\Programming for Biologists\assignment_database4.accdb'
msaccessdb.create(db_path)# Create a new empty Access database file

# Connection string for the Access database
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_path};'
)

# Data to be inserted into the table
data = [
    (21012, 4, 1993, 'DM', 42, 36, '1EA0F9'),
    (22012, 4, 1995, 'DM', 31, 37, '0D373C'),
    (23012, 17, 1996, 'DM', 25, 37, '64C6CC'),
    (24012, 21, 1996, 'PP', 26, 22, '1F511A'),
    (25012, 22, 1997, 'DM', 53, 35, '2624')
]

try:
    conn = pyodbc.connect(conn_str)# Establish connection to the Access database
    cursor = conn.cursor()# Create a cursor
    cursor.execute('''
        CREATE TABLE SurveysByHandz (
            SampleID INT PRIMARY KEY,
            Plot INT,
            Year INT,
            Species TEXT,
            Mass INT,
            HindFoot INT,
            Tag TEXT
        )
    ''')# Create the SurveysByHand table
    cursor.executemany('''
        INSERT INTO SurveysByHandz (SampleID, Plot, Year, Species, Mass, HindFoot, Tag)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()# Commit the transaction
    print(f"Access database '{db_path}' created successfully with table 'SurveysByHandz' and data inserted.")
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close() # Close connection
