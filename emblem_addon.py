import sqlite3
import os
import random
import tkinter as tk
from tkinter import filedialog
import sys
import hashlib

root = tk.Tk()
root.withdraw()  # Hide the main window

def manipulate_file(data, keys_0, keys_1, keys_2):
    for i in range(len(data)):
        data[i] = data[i] ^ ((keys_1 ^ keys_0 ^ keys_2) >> 24 & 0xFF)
        keys_0 = (0x343fd * keys_0 + 0x269ec3) & 0xFFFFFFFF
        keys_1 = (0x343fd * keys_1 + 0x269ec3) & 0xFFFFFFFF
        keys_2 = (0x343fd * keys_2 + 0x269ec3) & 0xFFFFFFFF

def generate_unique_emblem_id(cursor):
    while True:
        new_id = random.randint(0, 999999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_emblem WHERE id = ?;", (new_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id
                        
def emblem_path_randomhash(cursor):
    while True:
        new_hash2 = format(random.randint(0, 0xFFFFFFFF), 'x')
        cursor.execute("SELECT COUNT(*) FROM main.texture WHERE asset_path = ?;", (new_hash2,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_hash2
            

# Get user inputs
emblem_file = filedialog.askopenfilename(title="Locate Emblem File")
if emblem_file:
    print(f"Selected Emblem: {emblem_file}")
else:
    print("No file selected")
    sys.exit(1)
emblem_name = input("Enter Emblem name: ")
emblem_description = input("Enter Emblem description: ")
input("is everything correct?, Press Enter to add")


# Extract filename and filesize from emblem_file
emblem_filename = os.path.splitext(emblem_file.split("/")[-1])[0]
# Replace with actual method to get filesize
emblem_size = os.path.getsize(emblem_file)

encrypted_emblem = "static/2d61e7b4e89961c7/" + os.path.splitext(emblem_file.split("/")[-1])[0]

# encrypting asset first

with open(emblem_file, "rb") as file:
    data = bytearray(file.read())

    key_0 = 12345
    key_1 = 0
    key_2 = 0
    manipulate_file(data, key_0, key_1, key_2)

    with open(encrypted_emblem, "wb") as file:
        file.write(data)

print("asset encrypted")
with sqlite3.connect('assets/db/gl/asset_a_en.db') as conn:
    cursor = conn.cursor()
    
    emblem_path = emblem_path_randomhash(cursor)
    
    # (light download auto delete fix)
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (emblem_filename,))
    
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (emblem_path, emblem_filename, emblem_size))
                                 
# Connect to masterdata.db and perform INSERT
with sqlite3.connect('assets/db/gl/masterdata.db') as conn:
    cursor = conn.cursor()
    
    donot_insertem = None
    emblem_id_masterdata = generate_unique_emblem_id(cursor)
    emblem_dictionary = "m_dic_emblem_name_" + str(emblem_id_masterdata)
    emblem_dictionary_description = "m_dic_emblem_description_" + str(emblem_id_masterdata)
    emblem_dictionary_masterdata = "inline_image." + emblem_dictionary
    emblem_dictionary_description_masterdata = "inline_image." + emblem_dictionary_description
    
    cursor.execute("SELECT MAX(display_order) FROM main.m_emblem;")
    result = cursor.fetchone()
    max_display_order = result[0] if result[0] is not None else 0

    display_order_new = max_display_order + 1

    # Insert the new record with the updated display_order
    cursor.execute("INSERT INTO main.m_emblem (id, name, description, emblem_type, grade, emblem_asset_path, emblem_sub_asset_path, emblem_clear_condition_type, emblem_clear_condition_param, is_emblem_secret_condition, is_event_emblem, released_at, display_order) VALUES (?, ?, ?, '2', ?, ?, ?, '1', ?, '0', '0', '0', ?);",
                   (emblem_id_masterdata, emblem_dictionary_masterdata, emblem_dictionary_description_masterdata, donot_insertem, emblem_path, donot_insertem, donot_insertem, display_order_new)) 
                 
with sqlite3.connect('assets/db/gl/dictionary_en_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (emblem_dictionary, emblem_name))
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (emblem_dictionary_description, emblem_description))

# experimental add cdn asset to db    
with sqlite3.connect('assets/db/gl/asset_a_en.db') as conn:
    cursor = conn.cursor()
    
    donot_insert = None
    package_key_thumbnail = "main"
    category_emblem = '8'
    fresh_version_main = hashlib.sha1(str(random.random()).encode()).hexdigest()
    
    cursor.execute("SELECT COUNT(*) FROM main.m_asset_package_mapping WHERE package_key = 'main';")
    get_main_asset = cursor.fetchone()[0]
    update_main_asset = get_main_asset + 1
    
    cursor.execute("INSERT INTO main.m_asset_package_mapping (package_key, pack_name, file_size, metapack_name, metapack_offset, category) VALUES (?, ?, ?, ?, '0', ?);",
                   (package_key_thumbnail, emblem_filename, emblem_size, donot_insert, category_emblem))
    cursor.execute("REPLACE INTO main.m_asset_package (package_key, version, pack_num) VALUES ('main', ?, ?);",
                   (fresh_version_main, update_main_asset))
                       
print("emblem added to database")