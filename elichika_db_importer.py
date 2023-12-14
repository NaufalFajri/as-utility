import sqlite3
import os

import shutil

def create_backup(source_files, backup_files):
    for source_file, backup_file in zip(source_files, backup_files):
        if os.path.exists(backup_file):
            print(f"Backup file '{backup_file}' already exists. Skipping.")
        else:
            try:
                shutil.copy2(source_file, backup_file)
                print(f"Backup created successfully: {backup_file}")
            except Exception as e:
                print(f"Error creating backup for '{source_file}': {e}")

# Example usage:
source_files = ['assets/db/gl/asset_a_en.db', 'assets/db/gl/asset_i_en.db', 'assets/db/gl/asset_a_ko.db', 'assets/db/gl/asset_i_ko.db', 'assets/db/gl/asset_a_zh.db', 'assets/db/gl/asset_i_zh.db', 'assets/db/gl/masterdata.db', 'assets/db/gl/dictionary_en_inline_image.db', 'assets/db/gl/dictionary_ko_inline_image.db', 'assets/db/gl/dictionary_zh_inline_image.db']
backup_files = ['assets/db/gl/backup/asset_a_en.db', 'assets/db/gl/backup/asset_i_en.db', 'assets/db/gl/backup/asset_a_ko.db', 'assets/db/gl/backup/asset_i_ko.db', 'assets/db/gl/backup/asset_a_zh.db', 'assets/db/gl/backup/asset_i_zh.db', 'assets/db/gl/backup/masterdata.db', 'assets/db/gl/backup/dictionary_en_inline_image.db', 'assets/db/gl/backup/dictionary_ko_inline_image.db', 'assets/db/gl/backup/dictionary_zh_inline_image.db']


def import_to_multiple_dbs(source_sql_file, target_db_list):
    # Split SQL statements into individual queries
    with open(source_sql_file, 'r') as sql_file:
        sql_statements = sql_file.read()
    queries = sql_statements.split(';')

    for target_db in target_db_list:
        target_conn = sqlite3.connect(target_db)
        target_cursor = target_conn.cursor()

        try:
            # Execute each query in the target database
            for query in queries:
                if query.strip():  # Skip empty queries
                    try:
                        target_cursor.execute(query)
                    except sqlite3.OperationalError as e:
                        if "no such table" not in str(e):
                            raise
                        #print(f"Skipping query in {target_db}: {e}")

            target_conn.commit()
            print(f"Data successfully imported to {target_db}.")

        except sqlite3.Error as e:
            print(f"SQLite error in {target_db}: {e}")

        finally:
            # Close the target database connection
            target_conn.close()

# Example usage:
source_sql_file_input = "assets/data/" + input("Enter SQL filename: ") + ".sql"
if source_db_input == "assets/data/":
    print("No file selected")
    sys.exit(1)

# encrypting asset first
bekupfolder_folder = "assets/db/gl/backup/"

if not os.path.exists(bekupfolder_folder):
    os.makedirs(bekupfolder_folder)

target_dbs = [
    'assets/db/gl/asset_a_en.db',
    'assets/db/gl/asset_i_en.db',
    'assets/db/gl/asset_a_ko.db',
    'assets/db/gl/asset_i_ko.db',
    'assets/db/gl/asset_a_zh.db',
    'assets/db/gl/asset_i_zh.db',
    'assets/db/gl/masterdata.db',
    'assets/db/gl/dictionary_en_inline_image.db',
    'assets/db/gl/dictionary_ko_inline_image.db',
    'assets/db/gl/dictionary_zh_inline_image.db'
]
create_backup(source_files, backup_files)
import_to_multiple_dbs(source_sql_file_input, target_dbs)
