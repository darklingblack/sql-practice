import pyodbc

import msaccessdb
msaccessdb.create(r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPytonTraining\Programming for Biologists\assignment_database_1-2.accdb')

db_path = [] 
conn_str = []
create_table_sql = []

db_path = r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPytonTraining\Programming for Biologists\assignment_database_1-2.accdb' # Path to the existing Access database file
conn_str = (r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" rf"DBQ=C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPytonTraining\Programming for Biologists\assignment_database_1-2.accdb;")
create_table_sql = """
CREATE TABLE SurveysByHand2 (
    ID INT PRIMARY KEY,
    Plot INT,
    Year INT,
    Species TEXT,
    Mass INT,
    HindFoot INT,
    Tag TEXT
);
"""

data_points = [
    (21012, 4, 1993, 'DM', 42, 36, '1EA0F9'),
    (22012, 4, 1995, 'DM', 31, 37, '0D373C'),
    (23012, 17, 1996, 'DM', 25, 37, '64C6CC'),
    (24012, 21, 1996, 'PP', 26, 22, '1F511A'),
    (25012, 22, 1997, 'DM', 53, 35, '2624')
]

try:
    conn = pyodbc.connect(conn_str) # Connect to the Access database
    cursor = conn.cursor()
    insert_sql = """
    INSERT INTO SurveysByHand2 (SampleID, Plot, Year, Species, Mass, HindFoot, Tag)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(create_table_sql)
    cursor.execute("""
    CREATE TABLE SurveysByHand2 (
        SampleID INT PRIMARY KEY,
        Plot INT,
        Year INT,
        Species TEXT,
        Mass INT,
        HindFoot INT,
        Tag TEXT
    )
    """)   
    for data in data_points:
        cursor.execute(insert_sql, data)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created successfully!")    
except pyodbc.Error as e:
    print(f"Error connecting to MS Access database: {e}")
