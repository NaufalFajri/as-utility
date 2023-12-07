import sqlite3
import os

def import_to_multiple_dbs(source_sql_file, target_db1, target_db2, target_db3):
    # Connect to the target databases
    target_conn1 = sqlite3.connect(target_db1)
    target_cursor1 = target_conn1.cursor()

    target_conn2 = sqlite3.connect(target_db2)
    target_cursor2 = target_conn2.cursor()

    target_conn3 = sqlite3.connect(target_db3)
    target_cursor3 = target_conn3.cursor()

    try:
        # Read the SQL statements from the source SQL file
        with open(source_sql_file, 'r') as sql_file:
            sql_statements = sql_file.read()

        # Split SQL statements into individual queries
        queries = sql_statements.split(';')

        # Execute each query in the first target database
        for query in queries:
            if query.strip():  # Skip empty queries
                try:
                    target_cursor1.execute(query)
                except sqlite3.OperationalError as e:
                    if "no such table" not in str(e):
                        raise  # Raise the exception if it's not a "no such table" error
                    print(f"Skipping query in target_db1: {e}")
        target_conn1.commit()

        # Execute each query in the second target database
        for query in queries:
            if query.strip():
                try:
                    target_cursor2.execute(query)
                except sqlite3.OperationalError as e:
                    if "no such table" not in str(e):
                        raise
                    print(f"Skipping query in target_db2: {e}")
        target_conn2.commit()

        # Execute each query in the third target database
        for query in queries:
            if query.strip():
                try:
                    target_cursor3.execute(query)
                except sqlite3.OperationalError as e:
                    if "no such table" not in str(e):
                        raise
                    print(f"Skipping query in target_db3: {e}")
        target_conn3.commit()

        print("Data successfully imported to all target databases.")

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        # Close all database connections
        target_conn1.close()
        target_conn2.close()
        target_conn3.close()

# Example usage:
source_db_input = "assets/data/" + input("Enter the source database file path: ") + ".sql"
if source_db_input == "assets/data/":
    print("No file selected")
    sys.exit(1)
import_to_multiple_dbs(source_db_input, "assets/db/gl/asset_a_en.db", "assets/db/gl/masterdata.db", "assets/db/gl/dictionary_en_k.db")
