import sqlite3
import os
import random
import sys
import hashlib


def manipulate_file(data, keys_0, keys_1, keys_2):
    for i in range(len(data)):
        data[i] = data[i] ^ ((keys_1 ^ keys_0 ^ keys_2) >> 24 & 0xFF)
        keys_0 = (0x343fd * keys_0 + 0x269ec3) & 0xFFFFFFFF
        keys_1 = (0x343fd * keys_1 + 0x269ec3) & 0xFFFFFFFF
        keys_2 = (0x343fd * keys_2 + 0x269ec3) & 0xFFFFFFFF

def generate_unique_background_id(cursor):
    while True:
        new_id = random.randint(0, 999999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_custom_background WHERE id = ?;", (new_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id
                        
def background_path_randomhash(cursor):
    while True:
        new_hash2 = format(random.randint(0, 0xFFFFFFFF), 'x')
        cursor.execute("SELECT COUNT(*) FROM main.texture WHERE asset_path = ?;", (new_hash2,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_hash2
            

# Get user inputs
background_file = "assets/data/" + input("Enter background file: ")
if background_file == "assets/data/":
    print("No file selected")
    sys.exit(1)
background_name = input("Enter background name: ")
input("is everything correct?, Press Enter to add")


# Extract filename and filesize from background_file
background_filename = os.path.splitext(background_file.split("/")[-1])[0]
# Replace with actual method to get filesize
background_size = os.path.getsize(background_file)

encrypted_background = "static/2d61e7b4e89961c7/" + os.path.splitext(background_file.split("/")[-1])[0]

# encrypting asset first

with open(background_file, "rb") as file:
    data = bytearray(file.read())

    key_0 = 12345
    key_1 = 0
    key_2 = 0
    manipulate_file(data, key_0, key_1, key_2)

    with open(encrypted_background, "wb") as file:
        file.write(data)

print("asset encrypted")
with sqlite3.connect('assets/db/gl/asset_a_en.db') as conn:
    cursor = conn.cursor()
    
    background_path = background_path_randomhash(cursor)
    
    # (light download auto delete fix)
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (background_filename,))
    
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (background_path, background_filename, background_size))
                                 
# Connect to masterdata.db and perform INSERT
with sqlite3.connect('assets/db/gl/masterdata.db') as conn:
    cursor = conn.cursor()
    
    donot_insertbg = None
    background_id_masterdata = generate_unique_background_id(cursor)
    background_dictionary = "bg" + str(background_id_masterdata)
    background_dictionary_masterdata = "inline_image." + background_dictionary
    
    cursor.execute("SELECT MAX(display_order) FROM main.m_custom_background;")
    result = cursor.fetchone()
    max_display_order = result[0] if result[0] is not None else 0

    display_order_new = max_display_order + 1

    # Insert the new record with the updated display_order
    cursor.execute("INSERT INTO main.m_custom_background (id, background_id, name, thumbnail_asset_path, release_route, release_value, display_order) VALUES (?, ?, ?, ?, '2', '0', ?);",
                   (background_id_masterdata, background_id_masterdata, background_dictionary_masterdata, background_path, display_order_new)) # using bg as thumbnail
    cursor.execute("INSERT INTO main.m_background (id, prefab_asset_path, background_asset_path) VALUES (?, ?, ?);", (background_id_masterdata, donot_insertbg, background_path))
                   
with sqlite3.connect('assets/db/gl/dictionary_en_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (background_dictionary, background_name))

# experimental add cdn asset to db    
with sqlite3.connect('assets/db/gl/asset_a_en.db') as conn:
    cursor = conn.cursor()
    
    donot_insert = None
    package_key_thumbnail = "main"
    category_background = '8'
    fresh_version_main = hashlib.sha1(str(random.random()).encode()).hexdigest()
    
    cursor.execute("SELECT COUNT(*) FROM main.m_asset_package_mapping WHERE package_key = 'main';")
    get_main_asset = cursor.fetchone()[0]
    update_main_asset = get_main_asset + 1
    
    cursor.execute("INSERT INTO main.m_asset_package_mapping (package_key, pack_name, file_size, metapack_name, metapack_offset, category) VALUES (?, ?, ?, ?, '0', ?);",
                   (package_key_thumbnail, background_filename, background_size, donot_insert, category_background))
    cursor.execute("REPLACE INTO main.m_asset_package (package_key, version, pack_num) VALUES ('main', ?, ?);",
                   (fresh_version_main, update_main_asset))
                       
print("background added to database")