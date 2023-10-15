import sqlite3
import hashlib
import random
import os
import tkinter as tk
from tkinter import filedialog
import sys

# User inputs
costume_file = filedialog.askopenfilename(title="Locate New Costume File")
if costume_file:
    print(f"Selected costume: {costume_file}")
else:
    print("No file selected")
    sys.exit(1)
thumbnail_file = filedialog.askopenfilename(title="Locate New Thumbnail File")
if thumbnail_file:
    print(f"Selected thumbnail: {thumbnail_file}")
else:
    print("No file selected")
    sys.exit(1)
package_key_new = "suit:" + input("Enter costume id: ") #EDIT DIFFERENT

# Generate a random SHA-256 version
new_version = hashlib.sha256(str(random.random()).encode()).hexdigest()

# Extract filename and filesize from costume_file
costume_filename = costume_file.split("/")[-1]
# Replace with actual method to get filesize
costume_filesize = os.path.getsize(costume_file)

# Extract filename and filesize from thumbnail_file
thumbnail_costume_filename = thumbnail_file.split("/")[-1]
# Replace with actual method to get filesize
thumbnail_costume_size = os.path.getsize(thumbnail_file)

# Open the SQLite database
conn = sqlite3.connect("jp/asset_a_ja.db")
cursor = conn.cursor()

# Check if package_key_new exists in m_asset_package
cursor.execute("SELECT COUNT(*) FROM m_asset_package WHERE package_key = ?", (package_key_new,))
result = cursor.fetchone()
if result[0] > 0:
    # Update the existing record
    cursor.execute("UPDATE m_asset_package SET version = ? WHERE package_key = ?", (new_version, package_key_new))
    cursor.execute("UPDATE m_asset_package_mapping SET pack_name = ? WHERE package_key = ? AND category = '3", (costume_filename, package_key_new))
    cursor.execute("UPDATE m_asset_package_mapping SET file_size = ? WHERE package_key = ? AND category = '3'", (costume_filesize, package_key_new))
    cursor.execute("UPDATE m_asset_package_mapping SET pack_name = ? WHERE package_key = ? AND category = '8", (thumbnail_costume_filename, package_key_new))
    cursor.execute("UPDATE m_asset_package_mapping SET file_size = ? WHERE package_key = ? AND category = '8'", (thumbnail_costume_size, package_key_new))
    conn.commit()
else:
    # Handle the case when no package key is found
    print("No package key found.")

# Close the database connection
conn.close()
