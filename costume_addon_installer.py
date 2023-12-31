import sqlite3
import os
import zipfile
import io
import platform
import random
import sys
import shutil
import hashlib

modding_elichika_path = "assets/data/"

if not os.path.exists(modding_elichika_path):
    os.makedirs(modding_elichika_path)

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

source_files = ['assets/db/gl/asset_a_en.db', 'assets/db/gl/asset_i_en.db', 'assets/db/gl/asset_a_ko.db', 'assets/db/gl/asset_i_ko.db', 'assets/db/gl/asset_a_zh.db', 'assets/db/gl/asset_i_zh.db', 'assets/db/gl/masterdata.db', 'assets/db/gl/dictionary_en_inline_image.db', 'assets/db/gl/dictionary_ko_inline_image.db', 'assets/db/gl/dictionary_zh_inline_image.db', 'assets/db/jp/asset_a_ja.db', 'assets/db/jp/asset_i_ja.db', 'assets/db/jp/dictionary_ja_inline_image.db', 'assets/db/jp/masterdata.db']
backup_files = ['assets/db/gl/backup/asset_a_en.db', 'assets/db/gl/backup/asset_i_en.db', 'assets/db/gl/backup/asset_a_ko.db', 'assets/db/gl/backup/asset_i_ko.db', 'assets/db/gl/backup/asset_a_zh.db', 'assets/db/gl/backup/asset_i_zh.db', 'assets/db/gl/backup/masterdata.db', 'assets/db/gl/backup/dictionary_en_inline_image.db', 'assets/db/gl/backup/dictionary_ko_inline_image.db', 'assets/db/gl/backup/dictionary_zh_inline_image.db', 'assets/db/jp/backup/asset_a_ja.db', 'assets/db/jp/backup/asset_i_ja.db', 'assets/db/jp/backup/dictionary_ja_inline_image.db', 'assets/db/jp/backup/masterdata.db']

def create_backup_elichika_new(source_file_elichika_new, backup_file_elichika_new):
    if os.path.exists(backup_file_elichika_new):
        print("Backup file already exists. Stopping.")
        return
    
    try:
        shutil.copy2(source_file_elichika_new, backup_file_elichika_new)
        print(f"Backup created successfully: {backup_file_elichika_new}")
        print("do not transfer account with added item, this may don't work on JP client")
    except Exception as e:
        print(f"Error creating backup: {e}")

# Example usage:
source_file_elichika_new = "userdata.db"
backup_file_elichika_new = "backup_new/userdata.db"

def create_backup_elichika_new1(source_file_elichika_new1, backup_file_elichika_new1):
    if os.path.exists(backup_file_elichika_new1):
        print("Backup file already exists. Stopping.")
        return
    
    try:
        shutil.copy2(source_file_elichika_new1, backup_file_elichika_new1)
        print(f"Backup created successfully: {backup_file_elichika_new1}")
    except Exception as e:
        print(f"Error creating backup: {e}")

# Example usage:
source_file_elichika_new1 = "serverdata.db"
backup_file_elichika_new1 = "backup_new/serverdata.db"

def create_backup_elichika_old(source_file_elichika_old, backup_file_elichika_old):
    if os.path.exists(backup_file_elichika_old):
        print("Backup file already exists. Stopping.")
        return
    
    try:
        shutil.copy2(source_file_elichika_old, backup_file_elichika_old)
        print(f"Backup created successfully: {backup_file_elichika_old}")
    except Exception as e:
        print(f"Error creating backup: {e}")

# Example usage:
source_file_elichika_old = "assets/db/serverdata.db"
backup_file_elichika_old = "assets/db/backup_old/serverdata.db"

def clear_terminal():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux' or system == 'Darwin':
        os.system('clear')

def manipulate_file(data, keys_0, keys_1, keys_2):
    for i in range(len(data)):
        data[i] = data[i] ^ ((keys_1 ^ keys_0 ^ keys_2) >> 24 & 0xFF)
        keys_0 = (0x343fd * keys_0 + 0x269ec3) & 0xFFFFFFFF
        keys_1 = (0x343fd * keys_1 + 0x269ec3) & 0xFFFFFFFF
        keys_2 = (0x343fd * keys_2 + 0x269ec3) & 0xFFFFFFFF

# Function to generate a unique costume_id_masterdata
def generate_unique_costume_id(cursor):
    while True:
        new_id = random.randint(0, 999999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_suit WHERE id = ?;", (new_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id
            
def generate_unique_trade_id(cursor):
    while True:
        new_id333 = random.randint(0, 999999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_trade_product WHERE id = ?;", (new_id333,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id333
            
def generate_unique_trade_content_id(cursor):
    while True:
        new_id3334 = random.randint(0, 20000000000)
        cursor.execute("SELECT COUNT(*) FROM main.m_trade_product_content WHERE id = ?;", (new_id3334,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id3334
            
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
            
def rinaunmask_path_randomhash(cursor):
    while True:
        new_hash3 = format(random.randint(0, 0xFFFFFFFF), 'x')
        cursor.execute("SELECT COUNT(*) FROM main.texture WHERE asset_path = ?;", (new_hash3,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_hash3

# explorer code
clear_terminal()
temp_directory = "assets/data/temp/"
shutil.rmtree(temp_directory, ignore_errors=True)
directory_path_sifas = "assets/data/"

# List all files in the directory with a ".zip" extension
zip_files = [file for file in os.listdir(directory_path_sifas) if file.endswith(".zip")]

# Display the available zip files with corresponding numbers
print("Available .zip files:")
for i, zip_file in enumerate(zip_files, start=1):
    print(f"{i}. {zip_file}")

# User input to choose a zip file by entering a number
try:
    chosen_number = int(input("Enter the number corresponding to the .zip file you want to choose: "))
    
    # Check if the chosen number is valid
    if 1 <= chosen_number <= len(zip_files):
        chosen_zip_file = zip_files[chosen_number - 1]
        zip_file_path = os.path.join(directory_path_sifas, chosen_zip_file)
        print(f"You chose: {zip_file_path}")
        # Now you can work with the chosen zip file as needed
    else:
        print("Invalid number. Please enter a valid number.")
        sys.exit(1)
except ValueError:
    print("Invalid input. Please enter a number.")
    sys.exit(1)
    
os.makedirs(temp_directory, exist_ok=True)
with open(zip_file_path, 'rb') as zip_file:
    zip_data = zip_file.read()
    
zip_buffer = io.BytesIO(zip_data)

    # Create a ZipFile object
with zipfile.ZipFile(zip_buffer, 'r') as zip_ref:
        # Extract all files to the temp directory
    zip_ref.extractall(temp_directory)

        # Iterate through the contents of the ZIP file
    for file_info in zip_ref.infolist():
            # Check if the file has a .txt extension
        if file_info.filename.endswith('.txt'):
                # Open and process the .txt file
            txt_file_path = os.path.join(temp_directory, file_info.filename)
            with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
                    # Read and process each line in the extracted file
                for line in txt_file:
                    exec(line)




# Get user inputs
if chara_id == 212:
    chara_id = 211
elif chara_id == 211:
    chara_id = 212

if 1 <= chara_id <= 9:
    chara_id_group = 13
elif 101 <= chara_id <= 109:
    chara_id_group = 14
elif 201 <= chara_id <= 212:
    chara_id_group = 15

clear_terminal()
print('Name: ' + costume_name)
if chara_id == 1:
    print('Chara: Honoka Kousaka')
elif chara_id == 2:
    print('Chara: Eli Ayase')
elif chara_id == 3:
    print('Chara: Kotori Minami')
elif chara_id == 4:
    print('Chara: Umi Sonoda')
elif chara_id == 5:
    print('Chara: Rin Hoshizora')
elif chara_id == 6:
    print('Chara: Maki Nishikino')
elif chara_id == 7:
    print('Chara: Nozomi Tojo')
elif chara_id == 8:
    print('Chara: Hanayo Koizumi')
elif chara_id == 9:
    print('Chara: Nico Yazawa')
elif chara_id == 101:
    print('Chara: Chika Takami')
elif chara_id == 102:
    print('Chara: Riko Sakurauchi')
elif chara_id == 103:
    print('Chara: Kanan Matsuura')
elif chara_id == 104:
    print('Chara: Dia Kurosawa')
elif chara_id == 105:
    print('Chara: You Watanabe')
elif chara_id == 106:
    print('Chara: Yoshiko Tsushima')
elif chara_id == 107:
    print('Chara: Hanamaru Kunikida')
elif chara_id == 108:
    print('Chara: Mari Ohara')
elif chara_id == 109:
    print('Chara: Ruby Kurosawa')
elif chara_id == 201:
    print('Chara: Ayumu Uehara')
elif chara_id == 202:
    print('Chara: Kasumi Nakasu')
elif chara_id == 203:
    print('Chara: Shizuku Osaka')
elif chara_id == 204:
    print('Chara: Karin Asaka')
elif chara_id == 205:
    print('Chara: Ai Miyashita')
elif chara_id == 206:
    print('Chara: Kanata Konoe')
elif chara_id == 207:
    print('Chara: Setsuna Yuki')
elif chara_id == 208:
    print('Chara: Emma Verde')
elif chara_id == 209:
    print('Chara: Rina Tennoji')
elif chara_id == 210:
    print('Chara: Shioriko Mifune')
elif chara_id == 212:
    print('Chara: Lanzhu Zhong')
elif chara_id == 211:
    print('Chara: Mia Taylor')
    
if chara_id_group == 13:
    print('Group: Myuzu')
elif chara_id_group == 14:
    print('Group: Aqours')
elif chara_id_group == 15:
    print('Group: Nijigasaki')
print('Description: ' + costume_description)
do_you_think_want_add_this = input("do you want add this? (y/n): ")

if do_you_think_want_add_this == "y" :
    clear_terminal()
else :
    clear_terminal()
    shutil.rmtree(temp_directory, ignore_errors=True)
    sys.exit(1)

# Extract filename and filesize from costume_file
costume_filename = "0_" + os.path.splitext(costume_file.split("/")[-1])[0]
# Replace with actual method to get filesize
costume_filesize = os.path.getsize(costume_file)

# Extract filename and filesize from thumbnail_file
thumbnail_costume_filename = "0_" + os.path.splitext(thumbnail_file.split("/")[-1])[0]
# Replace with actual method to get filesize
thumbnail_costume_size = os.path.getsize(thumbnail_file)

encrypted_costume = "encrypted_data/files/files/pkg0/0_" + os.path.splitext(costume_file.split("/")[-1])[0]
encrypted_thumbnail = "encrypted_data/files/files/pkg0/0_" + os.path.splitext(thumbnail_file.split("/")[-1])[0]

if chara_id == 209:
    rina_unmask_costume_filename = "0_" + os.path.splitext(rina_unmask_costume_file.split("/")[-1])[0]
    rina_unmask_costume_filesize = os.path.getsize(rina_unmask_costume_file)

if chara_id == 209:
    encrypted_rina_unmask = "encrypted_data/files/files/pkg0/0_" + os.path.splitext(rina_unmask_costume_file.split("/")[-1])[0]

# encrypting asset first
encrypted_folder = "encrypted_data/files/files/pkg0/"

if not os.path.exists(encrypted_folder):
    os.makedirs(encrypted_folder)

# encrypting asset first
bekupfolder_folder = "assets/db/gl/backup/"

if not os.path.exists(bekupfolder_folder):
    os.makedirs(bekupfolder_folder)
    
bekupfolder_folder_japan = "assets/db/jp/backup/"

if not os.path.exists(bekupfolder_folder_japan):
    os.makedirs(bekupfolder_folder_japan)

create_backup(source_files, backup_files)

with open(costume_file, "rb") as file:
    data = bytearray(file.read())

    key_0 = 12345
    key_1 = 0
    key_2 = 0
    print("encrypting costume")
    manipulate_file(data, key_0, key_1, key_2)

    with open(encrypted_costume, "wb") as file:
        file.write(data)
    
with open(thumbnail_file, "rb") as file:
    data = bytearray(file.read())

    key_0 = 12345
    key_1 = 0
    key_2 = 0
    print("encrypting thumbnail")
    manipulate_file(data, key_0, key_1, key_2)

    with open(encrypted_thumbnail, "wb") as file:
        file.write(data)

if chara_id == 209:
    with open(rina_unmask_costume_file, "rb") as file:
        data = bytearray(file.read())

        key_0 = 12345
        key_1 = 0
        key_2 = 0
        print("encrypting rina unmask costume")
        manipulate_file(data, key_0, key_1, key_2)

        with open(encrypted_rina_unmask, "wb") as file:
            file.write(data)

print("assets encrypted")
with sqlite3.connect('assets/db/jp/asset_a_ja.db') as conn:
    cursor = conn.cursor()
    
    costume_path = costume_path_randomhash(cursor)
    thumbnail_costume_path = thumbnail_path_randomhash(cursor)
    
    # (light download auto delete fix)
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (costume_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_costume_filename,))
    if chara_id == 209:
        cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (rina_unmask_costume_filename,))
        
    cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (costume_path, costume_filename, costume_filesize))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (thumbnail_costume_path, thumbnail_costume_filename, thumbnail_costume_size))
                                 
    if chara_id == 209:
        rina_unmask_costume_path = rinaunmask_path_randomhash(cursor)
        cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (rina_unmask_costume_path, rina_unmask_costume_filename, rina_unmask_costume_filesize))     
 
    if chara_id == 1:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '{#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Q9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'aE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 2:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8C');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'k?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 3:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g4');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'T1');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 4:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M!');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 5:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '!{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 6:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'YS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '~Y');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 7:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'J9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'L_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '}x');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 8:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'BX');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '[*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 9:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'C{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#s');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 101:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '5]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '85');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'MS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 102:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Bz');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'F$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 103:
        fix_kanan_dep = "'x"
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kanan_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't~');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 104:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Iu');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'x=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 105:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'iy');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'jo');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'lR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 106:
        fix_yoshiko_dep = "Z'"
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Wm');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_yoshiko_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'di');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 107:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '2*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';L');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Tv');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 108:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'B*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^5');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 109:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'p2');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'U}');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 201:
        fix_ayumu_dep = ".'"
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ayumu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'f%');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sq');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 202:
        fix_kasukasu_dep = '"{'
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kasukasu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_K');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'uK');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 203:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^g');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'bS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#M');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 204:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '7,');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Aa');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'io');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 205:
        fix_ai_dep = '("'
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ai_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 206:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ')#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'LB');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Si');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 207:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8m');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'fl');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 208:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '28');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 209:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'ID');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'wS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z$');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'xU');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';k');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (rina_unmask_costume_path,))
    elif chara_id == 210:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^/)');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '$EZ');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sgs');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 212:
        fix_mia_dep = 'w";'
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_mia_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0W=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Qp?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 211:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '4fS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?l=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'oq0');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))

# REST CODE TO GL CLIENT & IOS PLATFORM

with sqlite3.connect('assets/db/jp/asset_i_ja.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (costume_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_costume_filename,))
    if chara_id == 209:
        cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (rina_unmask_costume_filename,))
        
    cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (costume_path, costume_filename, costume_filesize))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (thumbnail_costume_path, thumbnail_costume_filename, thumbnail_costume_size))
                                 
    if chara_id == 209:
        cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (rina_unmask_costume_path, rina_unmask_costume_filename, rina_unmask_costume_filesize))     
 
    if chara_id == 1:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '{#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Q9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'aE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 2:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8C');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'k?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 3:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g4');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'T1');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 4:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M!');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 5:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '!{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 6:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'YS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '~Y');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 7:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'J9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'L_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '}x');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 8:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'BX');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '[*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 9:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'C{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#s');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 101:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '5]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '85');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'MS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 102:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Bz');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'F$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 103:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kanan_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't~');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 104:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Iu');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'x=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 105:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'iy');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'jo');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'lR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 106:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Wm');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_yoshiko_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'di');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 107:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '2*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';L');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Tv');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 108:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'B*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^5');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 109:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'p2');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'U}');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 201:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ayumu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'f%');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sq');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 202:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kasukasu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_K');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'uK');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 203:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^g');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'bS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#M');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 204:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '7,');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Aa');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'io');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 205:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ai_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 206:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ')#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'LB');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Si');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 207:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8m');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'fl');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 208:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '28');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 209:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'ID');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'wS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z$');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'xU');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';k');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (rina_unmask_costume_path,))
    elif chara_id == 210:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^/)');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '$EZ');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sgs');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 212:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_mia_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0W=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Qp?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 211:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '4fS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?l=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'oq0');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))

with sqlite3.connect('assets/db/gl/asset_a_en.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (costume_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_costume_filename,))
    if chara_id == 209:
        cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (rina_unmask_costume_filename,))
        
    cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (costume_path, costume_filename, costume_filesize))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (thumbnail_costume_path, thumbnail_costume_filename, thumbnail_costume_size))
                                 
    if chara_id == 209:
        cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (rina_unmask_costume_path, rina_unmask_costume_filename, rina_unmask_costume_filesize))     
 
    if chara_id == 1:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '{#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Q9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'aE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 2:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8C');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'k?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 3:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g4');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'T1');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 4:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M!');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 5:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '!{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 6:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'YS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '~Y');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 7:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'J9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'L_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '}x');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 8:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'BX');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '[*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 9:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'C{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#s');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 101:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '5]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '85');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'MS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 102:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Bz');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'F$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 103:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kanan_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't~');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 104:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Iu');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'x=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 105:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'iy');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'jo');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'lR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 106:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Wm');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_yoshiko_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'di');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 107:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '2*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';L');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Tv');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 108:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'B*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^5');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 109:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'p2');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'U}');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 201:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ayumu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'f%');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sq');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 202:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kasukasu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_K');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'uK');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 203:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^g');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'bS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#M');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 204:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '7,');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Aa');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'io');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 205:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ai_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 206:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ')#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'LB');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Si');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 207:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8m');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'fl');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 208:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '28');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 209:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'ID');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'wS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z$');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'xU');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';k');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (rina_unmask_costume_path,))
    elif chara_id == 210:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^/)');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '$EZ');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sgs');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 212:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_mia_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0W=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Qp?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 211:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '4fS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?l=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'oq0');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))

with sqlite3.connect('assets/db/gl/asset_i_en.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (costume_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_costume_filename,))
    if chara_id == 209:
        cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (rina_unmask_costume_filename,))
        
    cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (costume_path, costume_filename, costume_filesize))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (thumbnail_costume_path, thumbnail_costume_filename, thumbnail_costume_size))
                                 
    if chara_id == 209:
        cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (rina_unmask_costume_path, rina_unmask_costume_filename, rina_unmask_costume_filesize))     
 
    if chara_id == 1:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '{#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Q9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'aE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 2:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8C');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'k?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 3:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g4');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'T1');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 4:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M!');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 5:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '!{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 6:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'YS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '~Y');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 7:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'J9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'L_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '}x');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 8:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'BX');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '[*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 9:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'C{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#s');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 101:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '5]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '85');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'MS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 102:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Bz');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'F$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 103:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kanan_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't~');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 104:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Iu');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'x=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 105:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'iy');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'jo');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'lR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 106:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Wm');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_yoshiko_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'di');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 107:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '2*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';L');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Tv');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 108:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'B*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^5');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 109:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'p2');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'U}');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 201:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ayumu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'f%');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sq');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 202:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kasukasu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_K');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'uK');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 203:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^g');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'bS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#M');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 204:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '7,');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Aa');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'io');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 205:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ai_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 206:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ')#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'LB');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Si');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 207:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8m');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'fl');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 208:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '28');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 209:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'ID');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'wS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z$');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'xU');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';k');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (rina_unmask_costume_path,))
    elif chara_id == 210:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^/)');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '$EZ');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sgs');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 212:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_mia_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0W=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Qp?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 211:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '4fS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?l=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'oq0');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))

with sqlite3.connect('assets/db/gl/asset_a_ko.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (costume_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_costume_filename,))
    if chara_id == 209:
        cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (rina_unmask_costume_filename,))
        
    cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (costume_path, costume_filename, costume_filesize))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (thumbnail_costume_path, thumbnail_costume_filename, thumbnail_costume_size))
                                 
    if chara_id == 209:
        cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (rina_unmask_costume_path, rina_unmask_costume_filename, rina_unmask_costume_filesize))     
                   
    if chara_id == 1:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '{#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Q9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'aE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 2:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8C');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'k?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 3:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g4');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'T1');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 4:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M!');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 5:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '!{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 6:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'YS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '~Y');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 7:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'J9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'L_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '}x');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 8:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'BX');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '[*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 9:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'C{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#s');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 101:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '5]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '85');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'MS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 102:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Bz');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'F$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 103:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kanan_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't~');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 104:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Iu');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'x=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 105:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'iy');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'jo');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'lR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 106:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Wm');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_yoshiko_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'di');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 107:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '2*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';L');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Tv');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 108:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'B*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^5');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 109:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'p2');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'U}');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 201:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ayumu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'f%');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sq');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 202:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kasukasu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_K');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'uK');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 203:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^g');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'bS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#M');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 204:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '7,');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Aa');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'io');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 205:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ai_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 206:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ')#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'LB');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Si');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 207:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8m');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'fl');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 208:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '28');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 209:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'ID');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'wS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z$');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'xU');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';k');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (rina_unmask_costume_path,))
    elif chara_id == 210:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^/)');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '$EZ');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sgs');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 212:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_mia_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0W=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Qp?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 211:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '4fS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?l=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'oq0');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))

with sqlite3.connect('assets/db/gl/asset_i_ko.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (costume_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_costume_filename,))
    if chara_id == 209:
        cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (rina_unmask_costume_filename,))
        
    cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (costume_path, costume_filename, costume_filesize))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (thumbnail_costume_path, thumbnail_costume_filename, thumbnail_costume_size))
                                 
    if chara_id == 209:
        cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (rina_unmask_costume_path, rina_unmask_costume_filename, rina_unmask_costume_filesize))     
 
    if chara_id == 1:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '{#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Q9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'aE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 2:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8C');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'k?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 3:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g4');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'T1');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 4:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M!');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 5:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '!{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 6:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'YS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '~Y');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 7:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'J9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'L_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '}x');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 8:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'BX');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '[*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 9:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'C{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#s');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 101:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '5]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '85');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'MS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 102:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Bz');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'F$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 103:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kanan_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't~');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 104:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Iu');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'x=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 105:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'iy');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'jo');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'lR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 106:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Wm');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_yoshiko_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'di');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 107:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '2*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';L');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Tv');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 108:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'B*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^5');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 109:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'p2');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'U}');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 201:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ayumu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'f%');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sq');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 202:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kasukasu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_K');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'uK');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 203:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^g');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'bS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#M');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 204:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '7,');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Aa');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'io');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 205:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ai_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 206:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ')#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'LB');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Si');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 207:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8m');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'fl');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 208:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '28');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 209:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'ID');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'wS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z$');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'xU');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';k');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (rina_unmask_costume_path,))
    elif chara_id == 210:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^/)');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '$EZ');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sgs');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 212:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_mia_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0W=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Qp?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 211:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '4fS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?l=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'oq0');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))

with sqlite3.connect('assets/db/gl/asset_a_zh.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (costume_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_costume_filename,))
    if chara_id == 209:
        cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (rina_unmask_costume_filename,))
        
    cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (costume_path, costume_filename, costume_filesize))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (thumbnail_costume_path, thumbnail_costume_filename, thumbnail_costume_size))
                                 
    if chara_id == 209:
        cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (rina_unmask_costume_path, rina_unmask_costume_filename, rina_unmask_costume_filesize))     
 
    if chara_id == 1:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '{#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Q9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'aE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 2:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8C');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'k?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 3:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g4');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'T1');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 4:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M!');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 5:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '!{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 6:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'YS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '~Y');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 7:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'J9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'L_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '}x');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 8:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'BX');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '[*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 9:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'C{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#s');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 101:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '5]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '85');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'MS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 102:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Bz');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'F$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 103:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kanan_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't~');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 104:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Iu');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'x=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 105:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'iy');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'jo');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'lR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 106:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Wm');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_yoshiko_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'di');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 107:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '2*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';L');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Tv');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 108:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'B*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^5');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 109:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'p2');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'U}');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 201:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ayumu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'f%');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sq');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 202:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kasukasu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_K');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'uK');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 203:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^g');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'bS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#M');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 204:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '7,');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Aa');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'io');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 205:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ai_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 206:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ')#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'LB');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Si');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 207:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8m');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'fl');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 208:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '28');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 209:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'ID');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'wS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z$');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'xU');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';k');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (rina_unmask_costume_path,))
    elif chara_id == 210:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^/)');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '$EZ');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sgs');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 212:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_mia_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0W=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Qp?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 211:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '4fS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?l=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'oq0');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))

with sqlite3.connect('assets/db/gl/asset_i_zh.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (costume_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_costume_filename,))
    if chara_id == 209:
        cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (rina_unmask_costume_filename,))
        
    cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (costume_path, costume_filename, costume_filesize))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (thumbnail_costume_path, thumbnail_costume_filename, thumbnail_costume_size))
                                 
    if chara_id == 209:
        cursor.execute("INSERT INTO main.member_model (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (rina_unmask_costume_path, rina_unmask_costume_filename, rina_unmask_costume_filesize))     
 
    if chara_id == 1:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '{#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Q9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'aE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 2:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8C');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'k?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 3:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g4');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'T1');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 4:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M!');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 5:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '!{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'M_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 6:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'YS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '~Y');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 7:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'J9');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'L_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '}x');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 8:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'BX');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '[*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 9:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'C{');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#s');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 101:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '5]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '85');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'MS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 102:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Bz');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'F$');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 103:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kanan_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(A');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 't~');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 104:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '.q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Iu');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'x=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 105:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'iy');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'jo');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'lR');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 106:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Wm');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_yoshiko_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'di');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 107:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '2*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';L');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Tv');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 108:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'B*');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^5');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_v');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 109:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'p2');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'U}');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 201:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ayumu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'f%');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sq');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 202:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_kasukasu_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '_K');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'uK');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 203:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^g');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'bS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '#M');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 204:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '7,');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Aa');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'io');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 205:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_ai_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '1]');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'a+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 206:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ')#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'LB');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Si');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
    elif chara_id == 207:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '8m');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'fl');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '(Q');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 208:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'g_');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'dE');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '28');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 209:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'ID');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'wS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Z$');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'xU');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ';k');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§?D#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§j^');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (rina_unmask_costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (rina_unmask_costume_path,))
    elif chara_id == 210:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '^/)');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '$EZ');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'sgs');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 212:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, ?);", (costume_path, fix_mia_dep))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '0W=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'Qp?');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
    elif chara_id == 211:
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '4fS');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '?l=');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, 'oq0');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§M|');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§Vr');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§n8#');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§y7');", (costume_path,))
        cursor.execute("INSERT INTO main.member_model_dependency (asset_path, dependency) VALUES (?, '§~+');", (costume_path,))

# Connect to masterdata.db and perform INSERT
with sqlite3.connect('assets/db/jp/masterdata.db') as conn:
    cursor = conn.cursor()

    # Generate a unique costume_id_masterdata
    costume_id_masterdata = generate_unique_costume_id(cursor)
    costume_dictionary = "suit_name_" + str(costume_id_masterdata)
    costume_dictionary_masterdata = "inline_image." + costume_dictionary
    donot_insert = None 
    
    # Find the minimum display_order for the given chara_id
    cursor.execute("SELECT MIN(display_order) FROM main.m_suit WHERE member_m_id = ?;", (chara_id,))
    result = cursor.fetchone()
    min_display_order_ja = result[0] if result[0] is not None else 0

    # Calculate the new display_order (decrease by 1)
    display_order_new_ja = min_display_order_ja - 1

    # Insert the new record with the updated display_order
    cursor.execute("INSERT INTO main.m_suit (id, member_m_id, name, thumbnail_image_asset_path, suit_release_route, suit_release_value, model_asset_path, display_order) VALUES (?, ?, ?, ?, '2', '0', ?, ?);",
                   (costume_id_masterdata, chara_id, costume_dictionary_masterdata, thumbnail_costume_path, costume_path, display_order_new_ja))
   
    if chara_id == 209:
        cursor.execute("INSERT INTO main.m_suit_view (suit_master_id, view_status, model_asset_path) VALUES (?, '2', ?);", (costume_id_masterdata, rina_unmask_costume_path))

with sqlite3.connect('assets/db/gl/masterdata.db') as conn:
    cursor = conn.cursor()
    
    # Find the minimum display_order for the given chara_id
    cursor.execute("SELECT MIN(display_order) FROM main.m_suit WHERE member_m_id = ?;", (chara_id,))
    result = cursor.fetchone()
    min_display_order_gl = result[0] if result[0] is not None else 0

    # Calculate the new display_order (decrease by 1)
    display_order_new_gl = min_display_order_gl - 1

    # Insert the new record with the updated display_order
    cursor.execute("INSERT INTO main.m_suit (id, member_m_id, name, thumbnail_image_asset_path, suit_release_route, suit_release_value, model_asset_path, display_order) VALUES (?, ?, ?, ?, '2', '0', ?, ?);",
                   (costume_id_masterdata, chara_id, costume_dictionary_masterdata, thumbnail_costume_path, costume_path, display_order_new_gl))
   
    if chara_id == 209:
        cursor.execute("INSERT INTO main.m_suit_view (suit_master_id, view_status, model_asset_path) VALUES (?, '2', ?);", (costume_id_masterdata, rina_unmask_costume_path))


with sqlite3.connect('assets/db/jp/dictionary_ja_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (costume_dictionary, costume_name))

with sqlite3.connect('assets/db/gl/dictionary_en_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (costume_dictionary, costume_name))
    
with sqlite3.connect('assets/db/gl/dictionary_ko_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (costume_dictionary, costume_name))
    
with sqlite3.connect('assets/db/gl/dictionary_zh_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (costume_dictionary, costume_name))
            
file_path_trade_stuff = 'userdata.db'
file_path_oldelichika_stuff = 'serverdata.db'

# Check if the file exists
if os.path.exists(file_path_trade_stuff):
    # File exists, proceed with reading and modifying
    print("elichika new version detected, adding to gold exchange shop")
    backup_trade_path = "backup_new"

    if not os.path.exists(backup_trade_path):
        os.makedirs(backup_trade_path)
        
    create_backup_elichika_new(source_file_elichika_new, backup_file_elichika_new)
    create_backup_elichika_new1(source_file_elichika_new1, backup_file_elichika_new1)
    
    # experimental add trade
    with sqlite3.connect('assets/db/gl/masterdata.db') as conn:
        cursor = conn.cursor()
        trade_content_into_json = generate_unique_trade_content_id(cursor)
        trade_id_into_json = generate_unique_trade_id(cursor)
        
        cursor.execute("INSERT INTO main.m_trade_product (id, trade_master_id, source_amount_color_on, label, display_order) VALUES (?, '1200', '0', ?, '1');", (trade_id_into_json, donot_insert))
        cursor.execute("INSERT INTO main.m_trade_product_content (id, trade_product_master_id, content_display_order) VALUES (?, ?, '1');", (trade_content_into_json, trade_id_into_json))
        cursor.execute("INSERT INTO main.m_trade_product_content_category (trade_category_master_pattern_id, trade_category_master_id, content_type, content_id) VALUES (0, ?, '7', ?);", (chara_id_group, costume_id_masterdata))
        
    with sqlite3.connect('serverdata.db') as conn:
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO main.s_trade_product (product_id, trade_id, source_amount, stock_amount, content_type, content_id, content_amount) VALUES (?, '1200', '1', ?, '7', ?, 1);", (trade_id_into_json, donot_insert, costume_id_masterdata))
    
    print("deleting temp folder")
    shutil.rmtree(temp_directory, ignore_errors=True)
    print("FINISHED")
    print("go to ~/elichika/encrypted_data/ & copy files folder to android/data/com.klab.lovelive.allstars.global(jp version path is similar) to something else")
    sys.exit(1)
    
elif os.path.exists(file_path_oldelichika_stuff):
    # File doesn't exist, rest of the code
    print("elichika old version detected, adding to serverdata")
    
    backup_usedata_path = "assets/db/backup_old/"

    if not os.path.exists(backup_usedata_path):
        os.makedirs(backup_usedata_path)
        
    create_backup_elichika_old(source_file_elichika_old, backup_file_elichika_old)
    
    with sqlite3.connect('assets/db/serverdata.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO main.s_user_suit (user_id, suit_master_id, is_new) VALUES ('588296696', ?, '1');", (costume_id_masterdata,))    
            
    print("deleting temp folder")
    shutil.rmtree(temp_directory, ignore_errors=True)
    print("FINISHED")
    print("go to ~/elichika/encrypted_data/ & copy files folder to android/data/com.klab.lovelive.allstars.global(jp version path is similar) to something else")
    sys.exit(1)
    
else:
    print("no elichika installed, ignoring import to userdata / serverdata")
    print("deleting temp folder")
    shutil.rmtree(temp_directory, ignore_errors=True)
    print("FINISHED")
    print("go to ~/elichika/encrypted_data/ & copy files folder to android/data/com.klab.lovelive.allstars.global(jp version path is similar) to something else")
    sys.exit(1)

