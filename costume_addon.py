import sqlite3
import os
import random

print("Eternal Live Addon Costume Database (JP)")
print("\n")
print("Note :")
print("Asset encryption key1 & key2 must be 0 value")
print("rina mask not tested yet")
print("missing chara dependencies")
print("\n")
print("--Chara ID--")
print("1 - Honoka")
print("2 - Eli")
print("3 - Kotori")
print("4 - Umi")
print("5 - Rin")
print("6 - Maki")
print("7 - Nozomi")
print("8 - Hanayo")
print("9 - Nico")
print("\n")
print("101 - Chika")
print("102 - Riko")
print("103 - Kanan")
print("104 - Dia")
print("105 - You")
print("106 - Yoshiko")
print("107 - Hanamaru")
print("108 - Mari")
print("109 - Ruby")
print("\n")
print("201 - Ayumu")
print("202 - Kasumi")
print("203 - Shizuku")
print("204 - Karin")
print("205 - Ai")
print("206 - Kanata")
print("207 - Setsuna")
print("208 - Emma")
print("209 - Rina")
print("210 - Shioriko")
print("211 - Lanzhu")
print("212 - Mia")


# Create a set to store existing costume IDs
# existing_costume_ids = set()

# Function to generate a unique costume_id_masterdata
def generate_unique_costume_id(cursor):
    while True:
        new_id = random.randint(0, 999999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_suit WHERE id = ?;", (new_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id
            
def costume_path_randomhash(cursor):
    while True:
        new_hash1 = format(random.randint(0, 0xFFFFFFFF), 'x')
        cursor.execute("SELECT COUNT(*) FROM main.member_model WHERE asset_path = ?;", (new_hash1,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_hash1
            
def thumbnail_path_randomhash(cursor):
    while True:
        new_hash2 = format(random.randint(0, 0xFFFFFFFF), 'x')
        cursor.execute("SELECT COUNT(*) FROM main.texture WHERE asset_path = ?;", (new_hash2,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_hash2


# Get user inputs
costume_file = input("Enter costume file: ")
thumbnail_file = input("Enter thumbnail file: ")
chara_dep = input("Enter chara ID dependencies: ")
chara_id = input("Enter chara ID to add: ")
if chara_id == "209":
    rina_unmask_costume_file = input("Enter rina unmasked costume file: ")
    print("input whatever you want")
    rina_unmask_costume_path = input("Enter rina unmasked costume path: ")
costume_name = input("Enter costume name: ")
elichika_add = input("do you want add to elichika serverdata? (y/n): ")
input("is everything correct?, Press Enter to add")


# Extract filename and filesize from costume_file
costume_filename = costume_file.split("/")[-1]
# Replace with actual method to get filesize
costume_filesize = os.path.getsize(costume_file)

# Extract filename and filesize from thumbnail_file
thumbnail_costume_filename = thumbnail_file.split("/")[-1]
# Replace with actual method to get filesize
thumbnail_costume_size = os.path.getsize(thumbnail_file)

if chara_id == "209":
    rina_unmask_costume_filename = rina_unmask_costume_file.split("/")[-1]
    rina_unmask_costume_filesize = os.path.getsize(rina_unmask_costume_file)

with sqlite3.connect('jp/asset_a_ja.db') as conn:
    cursor = conn.cursor()
    
    costume_path = costume_path_randomhash(cursor)
    thumbnail_costume_path = thumbnail_path_randomhash(cursor)
    
    cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (costume_path, costume_filename, costume_filesize))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (thumbnail_costume_path, thumbnail_costume_filename, thumbnail_costume_size))
                 
    if chara_id == "209":
        cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (rina_unmask_costume_path, rina_unmask_costume_filename, rina_unmask_costume_filesize))
                   
    if chara_dep == "101":
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '5]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'MS');", (costume_path,))          
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '85');", (costume_path,))          
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))          
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))          
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))          
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))          
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))          
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))          
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))                       
    elif chara_dep == "103":
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't~');", (costume_path,))
        kanan_fix_dep = "'x"
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, kanan_fix_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_dep == "105":
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'jo');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'lR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'iy');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))

# Connect to masterdata.db and perform INSERT
with sqlite3.connect('jp/masterdata.db') as conn:
    cursor = conn.cursor()

    # Generate a unique costume_id_masterdata
    costume_id_masterdata = generate_unique_costume_id(cursor)
    costume_dictionary = "suit_name_" + str(costume_id_masterdata)
    costume_dictionary_masterdata = "inline_image." + costume_dictionary
    
    # Find the minimum display_order for the given chara_id
    cursor.execute("SELECT MIN(display_order) FROM main.m_suit WHERE member_m_id = ?;", (chara_id,))
    result = cursor.fetchone()
    min_display_order = result[0] if result[0] is not None else 0

    # Calculate the new display_order (decrease by 1)
    display_order_new = min_display_order - 1

    # Insert the new record with the updated display_order
    cursor.execute("INSERT INTO main.m_suit (id, member_m_id, name, thumbnail_image_asset_path, suit_release_route, suit_release_value, model_asset_path, display_order) VALUES (?, ?, ?, ?, '2', '0', ?, ?);",
                   (costume_id_masterdata, chara_id, costume_dictionary_masterdata, thumbnail_costume_path, costume_path, display_order_new))
                   
    if chara_id == "209":
        cursor.execute("INSERT INTO main.member_model_dependency (suit_master_id, view_status, model_asset_path) VALUES (?, '2', ?);", (costume_id_masterdata, rina_unmask_costume_path))

    if elichika_add == "y":
        with sqlite3.connect('serverdata.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO main.s_user_suit (user_id, suit_master_id, is_new) VALUES ('588296696', ?, '1');", (costume_id_masterdata,))

with sqlite3.connect('jp/dictionary_ja_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (costume_dictionary, costume_name))
        
print("costume added to database")