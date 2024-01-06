import sqlite3
import os
import zipfile
import io
import json
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

source_files = ['assets/db/gl/asset_a_en.db', 'assets/db/gl/asset_i_en.db', 'assets/db/gl/asset_a_ko.db', 'assets/db/gl/asset_i_ko.db', 'assets/db/gl/asset_a_zh.db', 'assets/db/gl/asset_i_zh.db', 'assets/db/gl/masterdata.db', 'assets/db/gl/dictionary_en_inline_image.db', 'assets/db/gl/dictionary_ko_inline_image.db', 'assets/db/gl/dictionary_zh_inline_image.db']
backup_files = ['assets/db/gl/backup/asset_a_en.db', 'assets/db/gl/backup/asset_i_en.db', 'assets/db/gl/backup/asset_a_ko.db', 'assets/db/gl/backup/asset_i_ko.db', 'assets/db/gl/backup/asset_a_zh.db', 'assets/db/gl/backup/asset_i_zh.db', 'assets/db/gl/backup/masterdata.db', 'assets/db/gl/backup/dictionary_en_inline_image.db', 'assets/db/gl/backup/dictionary_ko_inline_image.db', 'assets/db/gl/backup/dictionary_zh_inline_image.db']



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

# Function to generate a unique live_id_masterdata
def generate_unique_live_id(cursor):
    while True:
        new_id = random.randint(0, 99999)
        cursor.execute("SELECT COUNT(*) FROM main.m_live WHERE live_id = ?;", (new_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id
       


def generate_unique_music_id1(cursor):
    while True:
        new_id42a = random.randint(0, 99999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_live_difficulty WHERE live_id = ?;", (new_id42a,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id42a

def generate_unique_liveconst1_id(cursor):
    while True:
        new_id42a311 = random.randint(0, 99999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_live_difficulty_const WHERE id = ?;", (new_id42a311,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id42a311              
            
def generate_unique_liveconst2_id(cursor):
    while True:
        new_id42a322 = random.randint(0, 99999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_live_difficulty_const WHERE id = ?;", (new_id42a322,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id42a322   
            
def generate_unique_liveconst3_id(cursor):
    while True:
        new_id42a333 = random.randint(0, 99999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_live_difficulty_const WHERE id = ?;", (new_id42a333,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id42a333     

def generate_unique_music_id2(cursor):
    while True:
        new_id42b = random.randint(0, 99999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_live_difficulty WHERE live_id = ?;", (new_id42b,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id42b
            
def generate_unique_music_id2a(cursor):
    while True:
        new_id42b11 = random.randint(0, 9999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_live_difficulty_gimmick WHERE id = ?;", (new_id42b11,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id42b11
          
def generate_unique_music_id2b(cursor):
    while True:
        new_id42b22 = random.randint(0, 9999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_live_difficulty_gimmick WHERE id = ?;", (new_id42b22,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id42b22
            
def generate_unique_music_id2c(cursor):
    while True:
        new_id42b33 = random.randint(0, 9999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_live_difficulty_gimmick WHERE id = ?;", (new_id42b33,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id42b33
            
def generate_unique_music_id3(cursor):
    while True:
        new_id42c = random.randint(0, 99999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_live_difficulty WHERE live_id = ?;", (new_id42c,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id42c  
            
def generate_unique_music_id(cursor):
    while True:
        new_id42 = random.randint(1000, 9999)
        cursor.execute("SELECT COUNT(*) FROM main.m_live WHERE music_id = ?;", (new_id42,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id42    
                        
def thumbnail_path_randomhash(cursor):
    while True:
        new_hash2 = format(random.randint(0, 0xFFFFFFFF), 'x')
        cursor.execute("SELECT COUNT(*) FROM main.texture WHERE asset_path = ?;", (new_hash2,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_hash2
            
def movie_path_randomhash(cursor):
    while True:
        new_hash2mov = format(random.randint(0, 0xFFFFFFFF), 'x')
        cursor.execute("SELECT COUNT(*) FROM main.m_movie WHERE pavement = ?;", (new_hash2mov,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_hash2mov
            
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





clear_terminal()
print('Name: ' + music_name)
print('Copyright: ' + music_copyright_name)
if member_group_live == 1:
    print('Group: Myuzu')
elif member_group_live == 2:
    print('Group: Aqours')
elif member_group_live == 3:
    print('Group: Nijigasaki')
elif member_group_live == 4:
    print('Group: Liella')
else:
    print('Please enter correct member_group_live value')
    sys.exit(1)    
    
    
if attribute_live == 1:
    print('Attribute: Smile')
elif attribute_live == 2:
    print('Attribute: Pure')
elif attribute_live == 3:
    print('Attribute: Cool')
elif attribute_live == 4:
    print('Attribute: Active')
elif attribute_live == 5:
    print('Attribute: Natural')
elif attribute_live == 6:
    print('Attribute: Elegant')
elif attribute_live == 9:
    print('Attribute: Untyped / Unknown')
else:
    print('Please enter correct attribute value')
    sys.exit(1)
    
if 'videoprime_file' in globals() or 'videoprime_file' in locals():
    print('MV Video: yes')
else:
    print('MV Video: no')
print('Description: ' + music_description)
do_you_think_want_add_this = input("do you want add this? (y/n): ")

if do_you_think_want_add_this == "y" :
    clear_terminal()
else :
    clear_terminal()
    shutil.rmtree(temp_directory, ignore_errors=True)
    sys.exit(1)

# Extract filename and filesize from costume_file
music_filename = "0_" + os.path.splitext(music_file.split("/")[-1])[0]
music_sabi_filename = "0_" + os.path.splitext(music_sabi_file.split("/")[-1])[0]

# Extract filename and filesize from thumbnail_file
thumbnail_music_filename = "0_" + os.path.splitext(thumbnail_file.split("/")[-1])[0]

# Replace with actual method to get filesize
thumbnail_music_size = os.path.getsize(thumbnail_file)

encrypted_thumbnail = "encrypted_data/files/files/pkg0/0_" + os.path.splitext(thumbnail_file.split("/")[-1])[0]
music_filename_saved = "encrypted_data/files/files/pkg0/0_" + os.path.splitext(music_file.split("/")[-1])[0]
music_sabi_filename_saved = "encrypted_data/files/files/pkg0/0_" + os.path.splitext(music_sabi_file.split("/")[-1])[0]
movie_filename_saved = "encrypted_data/files/files/pkg0/0_" + os.path.splitext(videoprime_file.split("/")[-1])[0]

# encrypting asset first
encrypted_folder = "encrypted_data/files/files/pkg0/"

if not os.path.exists(encrypted_folder):
    os.makedirs(encrypted_folder)

# encrypting asset first
bekupfolder_folder = "assets/db/gl/backup/"

if not os.path.exists(bekupfolder_folder):
    os.makedirs(bekupfolder_folder)

create_backup(source_files, backup_files)
    
def read_file_and_select_text(music_file):
    with open(music_file, 'rb') as file:
        # Seek to the decimal offset 1438
        file.seek(1438)

        selected_text_deretote = b''  # Use bytes for binary reading

        while True:
            # Read one byte
            byte = file.read(1)

            # Check if the byte is the hex value 00
            if byte == b'\x00':
                break  # Stop reading if hex 00 is found

            selected_text_deretote += byte

        # Print the selected text
        return selected_text_deretote.decode('utf-8')
        
def read_file_and_select_text1(music_sabi_file):
    with open(music_sabi_file, 'rb') as file:
        # Seek to the decimal offset 1438
        file.seek(1438)

        selected_text_deretote = b''  # Use bytes for binary reading

        while True:
            # Read one byte
            byte = file.read(1)

            # Check if the byte is the hex value 00
            if byte == b'\x00':
                break  # Stop reading if hex 00 is found

            selected_text_deretote += byte

        # Print the selected text
        return selected_text_deretote.decode('utf-8')
    
with open(thumbnail_file, "rb") as file:
    data = bytearray(file.read())

    key_0 = 12345
    key_1 = 0
    key_2 = 0
    print("encrypting jacket")
    manipulate_file(data, key_0, key_1, key_2)

    with open(encrypted_thumbnail, "wb") as file:
        file.write(data)

print("assets encrypted")
shutil.copy(music_file, music_filename_saved)
shutil.copy(music_sabi_file, music_sabi_filename_saved)

with sqlite3.connect('assets/db/gl/asset_a_en.db') as conn:
    cursor = conn.cursor()
    
    thumbnail_music_path = thumbnail_path_randomhash(cursor)
    sheet_name_file = read_file_and_select_text(music_file)
    sheet_name_file1 = read_file_and_select_text1(music_sabi_file)
    donot_insert = None
    if 'videoprime_file' in globals() or 'videoprime_file' in locals():
        print("videoprime_file detected. adding MV Video to database")
        movie_genpath = movie_path_randomhash(cursor)
        movie_filename = "0_" + os.path.splitext(videoprime_file.split("/")[-1])[0]
        cursor.execute("INSERT INTO main.m_movie (pavement, pack_name) VALUES (?, ?);", (movie_genpath, movie_filename))
        shutil.copy(videoprime_file, movie_filename_saved)
    else:
        print("videoprime_file not detected. ignoring MV Video")
     
    # (light download auto delete fix)
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_sabi_filename,))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file, music_filename, donot_insert))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file1, music_sabi_filename, donot_insert))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');", (thumbnail_music_path, thumbnail_music_filename, thumbnail_music_size))
    
# REST CODE TO CN ZH LANGUAGE & IOS PLATFORM
with sqlite3.connect('assets/db/gl/asset_i_en.db') as conn:
    cursor = conn.cursor()   

    if 'videoprime_file' in globals() or 'videoprime_file' in locals():
        cursor.execute("INSERT INTO main.m_movie (pavement, pack_name) VALUES (?, ?);", (movie_genpath, movie_filename))

    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_sabi_filename,))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file, music_filename, donot_insert))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file1, music_sabi_filename, donot_insert))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');", (thumbnail_music_path, thumbnail_music_filename, thumbnail_music_size))

with sqlite3.connect('assets/db/gl/asset_a_ko.db') as conn:
    cursor = conn.cursor()

    if 'videoprime_file' in globals() or 'videoprime_file' in locals():
        cursor.execute("INSERT INTO main.m_movie (pavement, pack_name) VALUES (?, ?);", (movie_genpath, movie_filename))

    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_sabi_filename,))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file, music_filename, donot_insert))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file1, music_sabi_filename, donot_insert))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');", (thumbnail_music_path, thumbnail_music_filename, thumbnail_music_size))

with sqlite3.connect('assets/db/gl/asset_i_ko.db') as conn:
    cursor = conn.cursor()

    if 'videoprime_file' in globals() or 'videoprime_file' in locals():
        cursor.execute("INSERT INTO main.m_movie (pavement, pack_name) VALUES (?, ?);", (movie_genpath, movie_filename))

    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_sabi_filename,))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file, music_filename, donot_insert))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file1, music_sabi_filename, donot_insert))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');", (thumbnail_music_path, thumbnail_music_filename, thumbnail_music_size))

with sqlite3.connect('assets/db/gl/asset_a_zh.db') as conn:
    cursor = conn.cursor()

    if 'videoprime_file' in globals() or 'videoprime_file' in locals():
        cursor.execute("INSERT INTO main.m_movie (pavement, pack_name) VALUES (?, ?);", (movie_genpath, movie_filename))
        
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_sabi_filename,))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file, music_filename, donot_insert))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file1, music_sabi_filename, donot_insert))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');", (thumbnail_music_path, thumbnail_music_filename, thumbnail_music_size))

with sqlite3.connect('assets/db/gl/asset_i_zh.db') as conn:
    cursor = conn.cursor()

    if 'videoprime_file' in globals() or 'videoprime_file' in locals():
        cursor.execute("INSERT INTO main.m_movie (pavement, pack_name) VALUES (?, ?);", (movie_genpath, movie_filename))  
   
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (thumbnail_music_filename,))
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (music_sabi_filename,))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file, music_filename, donot_insert))
    cursor.execute("INSERT INTO main.m_asset_sound (sheet_name, acb_pack_name, awb_pack_name) VALUES (?, ?, ?);", (sheet_name_file1, music_sabi_filename, donot_insert))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');", (thumbnail_music_path, thumbnail_music_filename, thumbnail_music_size))   

# Connect to masterdata.db and perform INSERT
with sqlite3.connect('assets/db/gl/masterdata.db') as conn:
    cursor = conn.cursor()

    # Generate a unique live_id_masterdata
    live_id_masterdata = generate_unique_live_id(cursor)
    music_id_masterdata = generate_unique_music_id(cursor)
    music_diff1_masterdata = generate_unique_music_id1(cursor)
    music_diff2_masterdata = generate_unique_music_id2(cursor)
    music_diff3_masterdata = generate_unique_music_id3(cursor)
    music_diff1g_masterdata = generate_unique_music_id2a(cursor)
    music_diff2g_masterdata = generate_unique_music_id2b(cursor)
    music_diff3g_masterdata = generate_unique_music_id2c(cursor)
    music_name_dictionary_masterdata = "inline_image.song_name_so" + str(music_id_masterdata)
    music_id_copyright_masterdata = "inline_image.song_copyright_so" + str(music_id_masterdata)
    music_name_dictionary_dic = "song_name_so" + str(music_id_masterdata)
    music_id_copyright_dic = "song_copyright_so" + str(music_id_masterdata)
    
    live_constaddon_easy = generate_unique_liveconst1_id(cursor)
    live_constaddon_normal = generate_unique_liveconst2_id(cursor)
    live_constaddon_hard = generate_unique_liveconst3_id(cursor)
    
    # Find the minimum display_order for the given chara_id
    cursor.execute("SELECT MAX(display_order) FROM main.m_live WHERE member_group=?;", (member_group_live,))
    result = cursor.fetchone()
    min_display_order = result[0] if result[0] is not None else 0

    # Calculate the new display_order (decrease by 1)
    display_order_new = min_display_order + 1

    # Insert the new record with the updated display_order
    # there no Liella & Union chibi so i will reuse myuzu
    if member_group_live == 1:
        member_mapping_live = 10001
        if attribute_live == 1:
            drop_live_item1_easy = 104100110
            drop_live_item1_normal = 104100120
            drop_live_item1_hard = 104100130
            drop_live_item2_easy = 100100110
            drop_live_item2_normal = 100100120
            drop_live_item2_hard = 100100130
            drop_live_item3_easy = 101100110
            drop_live_item3_normal = 101100120
            drop_live_item3_hard = 101100130
            drop_live_item4_easy = 102100110
            drop_live_item4_normal = 102100120
            drop_live_item4_hard = 102100130
            drop_live_item5_easy = 103100110
            drop_live_item5_normal = 103100120
            drop_live_item5_hard = 103100130
        elif attribute_live == 2:
            drop_live_item1_easy = 104200110
            drop_live_item1_normal = 104200120
            drop_live_item1_hard = 104200130
            drop_live_item2_easy = 100200110
            drop_live_item2_normal = 100200120
            drop_live_item2_hard = 100200130
            drop_live_item3_easy = 101200110
            drop_live_item3_normal = 101200120
            drop_live_item3_hard = 101200130
            drop_live_item4_easy = 102200110
            drop_live_item4_normal = 102200120
            drop_live_item4_hard = 102200130
            drop_live_item5_easy = 103200110
            drop_live_item5_normal = 103200120
            drop_live_item5_hard = 103200130
        elif attribute_live == 3:
            drop_live_item1_easy = 104300110
            drop_live_item1_normal = 104300120
            drop_live_item1_hard = 104300130
            drop_live_item2_easy = 100300110
            drop_live_item2_normal = 100300120
            drop_live_item2_hard = 100300130
            drop_live_item3_easy = 101300110
            drop_live_item3_normal = 101300120
            drop_live_item3_hard = 101300130
            drop_live_item4_easy = 102300110
            drop_live_item4_normal = 102300120
            drop_live_item4_hard = 102300130
            drop_live_item5_easy = 103300110
            drop_live_item5_normal = 103300120
            drop_live_item5_hard = 103300130
        elif attribute_live == 4:
            drop_live_item1_easy = 104400110
            drop_live_item1_normal = 104400120
            drop_live_item1_hard = 104400130
            drop_live_item2_easy = 100400110
            drop_live_item2_normal = 100400120
            drop_live_item2_hard = 100400130
            drop_live_item3_easy = 101400110
            drop_live_item3_normal = 101400120
            drop_live_item3_hard = 101400130
            drop_live_item4_easy = 102400110
            drop_live_item4_normal = 102400120
            drop_live_item4_hard = 102400130
            drop_live_item5_easy = 103400110
            drop_live_item5_normal = 103400120
            drop_live_item5_hard = 103400130
        elif attribute_live == 5:
            drop_live_item1_easy = 104500110
            drop_live_item1_normal = 104500120
            drop_live_item1_hard = 104500130
            drop_live_item2_easy = 100500110
            drop_live_item2_normal = 100500120
            drop_live_item2_hard = 100500130
            drop_live_item3_easy = 101500110
            drop_live_item3_normal = 101500120
            drop_live_item3_hard = 101500130
            drop_live_item4_easy = 102500110
            drop_live_item4_normal = 102500120
            drop_live_item4_hard = 102500130
            drop_live_item5_easy = 103500110
            drop_live_item5_normal = 103500120
            drop_live_item5_hard = 103500130
        elif attribute_live == 6:
            drop_live_item1_easy = 104600110
            drop_live_item1_normal = 104600120
            drop_live_item1_hard = 104600130
            drop_live_item2_easy = 100600110
            drop_live_item2_normal = 100600120
            drop_live_item2_hard = 100600130
            drop_live_item3_easy = 101600110
            drop_live_item3_normal = 101600120
            drop_live_item3_hard = 101600130
            drop_live_item4_easy = 102600110
            drop_live_item4_normal = 102600120
            drop_live_item4_hard = 102600130
            drop_live_item5_easy = 103600110
            drop_live_item5_normal = 103600120
            drop_live_item5_hard = 103600130
        else:
            drop_live_item1_easy = 0
            drop_live_item1_normal = 0
            drop_live_item1_hard = 0
            drop_live_item2_easy = 0
            drop_live_item2_normal = 0
            drop_live_item2_hard = 0
            drop_live_item3_easy = 0
            drop_live_item3_normal = 0
            drop_live_item3_hard = 0
            drop_live_item4_easy = 0
            drop_live_item4_normal = 0
            drop_live_item4_hard = 0
            drop_live_item5_easy = 0
            drop_live_item5_normal = 0
            drop_live_item5_hard = 0
    elif member_group_live == 2:
        member_mapping_live = 11001
        if attribute_live == 1:
            drop_live_item1_easy = 104100210
            drop_live_item1_normal = 104100220
            drop_live_item1_hard = 104100230
            drop_live_item2_easy = 100100210
            drop_live_item2_normal = 100100220
            drop_live_item2_hard = 100100230
            drop_live_item3_easy = 101100210
            drop_live_item3_normal = 101100220
            drop_live_item3_hard = 101100230
            drop_live_item4_easy = 102100210
            drop_live_item4_normal = 102100220
            drop_live_item4_hard = 102100230
            drop_live_item5_easy = 103100210
            drop_live_item5_normal = 103100220
            drop_live_item5_hard = 103100230
        elif attribute_live == 2:
            drop_live_item1_easy = 104200210
            drop_live_item1_normal = 104200220
            drop_live_item1_hard = 104200230
            drop_live_item2_easy = 100200210
            drop_live_item2_normal = 100200220
            drop_live_item2_hard = 100200230
            drop_live_item3_easy = 101200210
            drop_live_item3_normal = 101200220
            drop_live_item3_hard = 101200230
            drop_live_item4_easy = 102200210
            drop_live_item4_normal = 102200220
            drop_live_item4_hard = 102200230
            drop_live_item5_easy = 103200210
            drop_live_item5_normal = 103200220
            drop_live_item5_hard = 103200230
        elif attribute_live == 3:
            drop_live_item1_easy = 104300210
            drop_live_item1_normal = 104300220
            drop_live_item1_hard = 104300230
            drop_live_item2_easy = 100300210
            drop_live_item2_normal = 100300220
            drop_live_item2_hard = 100300230
            drop_live_item3_easy = 101300210
            drop_live_item3_normal = 101300220
            drop_live_item3_hard = 101300230
            drop_live_item4_easy = 102300210
            drop_live_item4_normal = 102300220
            drop_live_item4_hard = 102300230
            drop_live_item5_easy = 103300210
            drop_live_item5_normal = 103300220
            drop_live_item5_hard = 103300230
        elif attribute_live == 4:
            drop_live_item1_easy = 104400210
            drop_live_item1_normal = 104400220
            drop_live_item1_hard = 104400230
            drop_live_item2_easy = 100400210
            drop_live_item2_normal = 100400220
            drop_live_item2_hard = 100400230
            drop_live_item3_easy = 101400210
            drop_live_item3_normal = 101400220
            drop_live_item3_hard = 101400230
            drop_live_item4_easy = 102400210
            drop_live_item4_normal = 102400220
            drop_live_item4_hard = 102400230
            drop_live_item5_easy = 103400210
            drop_live_item5_normal = 103400220
            drop_live_item5_hard = 103400230
        elif attribute_live == 5:
            drop_live_item1_easy = 104500210
            drop_live_item1_normal = 104500220
            drop_live_item1_hard = 104500230
            drop_live_item2_easy = 100500210
            drop_live_item2_normal = 100500220
            drop_live_item2_hard = 100500230
            drop_live_item3_easy = 101500210
            drop_live_item3_normal = 101500220
            drop_live_item3_hard = 101500230
            drop_live_item4_easy = 102500210
            drop_live_item4_normal = 102500220
            drop_live_item4_hard = 102500230
            drop_live_item5_easy = 103500210
            drop_live_item5_normal = 103500220
            drop_live_item5_hard = 103500230
        elif attribute_live == 6:
            drop_live_item1_easy = 104600210
            drop_live_item1_normal = 104600220
            drop_live_item1_hard = 104600230
            drop_live_item2_easy = 100600210
            drop_live_item2_normal = 100600220
            drop_live_item2_hard = 100600230
            drop_live_item3_easy = 101600210
            drop_live_item3_normal = 101600220
            drop_live_item3_hard = 101600230
            drop_live_item4_easy = 102600210
            drop_live_item4_normal = 102600220
            drop_live_item4_hard = 102600230
            drop_live_item5_easy = 103600210
            drop_live_item5_normal = 103600220
            drop_live_item5_hard = 103600230
        else:
            drop_live_item1_easy = 0
            drop_live_item1_normal = 0
            drop_live_item1_hard = 0
            drop_live_item2_easy = 0
            drop_live_item2_normal = 0
            drop_live_item2_hard = 0
            drop_live_item3_easy = 0
            drop_live_item3_normal = 0
            drop_live_item3_hard = 0
            drop_live_item4_easy = 0
            drop_live_item4_normal = 0
            drop_live_item4_hard = 0
            drop_live_item5_easy = 0
            drop_live_item5_normal = 0
            drop_live_item5_hard = 0
    elif member_group_live == 3:
        member_mapping_live = 12130
        if attribute_live == 1:
            drop_live_item1_easy = 104100610
            drop_live_item1_normal = 104100620
            drop_live_item1_hard = 104100630
            drop_live_item2_easy = 100100610
            drop_live_item2_normal = 100100620
            drop_live_item2_hard = 100100630
            drop_live_item3_easy = 101100610
            drop_live_item3_normal = 101100620
            drop_live_item3_hard = 101100630
            drop_live_item4_easy = 102100610
            drop_live_item4_normal = 102100620
            drop_live_item4_hard = 102100630
            drop_live_item5_easy = 103100610
            drop_live_item5_normal = 103100620
            drop_live_item5_hard = 103100630
        elif attribute_live == 2:
            drop_live_item1_easy = 104200610
            drop_live_item1_normal = 104200620
            drop_live_item1_hard = 104200630
            drop_live_item2_easy = 100200610
            drop_live_item2_normal = 100200620
            drop_live_item2_hard = 100200630
            drop_live_item3_easy = 101200610
            drop_live_item3_normal = 101200620
            drop_live_item3_hard = 101200630
            drop_live_item4_easy = 102200610
            drop_live_item4_normal = 102200620
            drop_live_item4_hard = 102200630
            drop_live_item5_easy = 103200610
            drop_live_item5_normal = 103200620
            drop_live_item5_hard = 103200630
        elif attribute_live == 3:
            drop_live_item1_easy = 104300610
            drop_live_item1_normal = 104300620
            drop_live_item1_hard = 104300630
            drop_live_item2_easy = 100300610
            drop_live_item2_normal = 100300620
            drop_live_item2_hard = 100300630
            drop_live_item3_easy = 101300610
            drop_live_item3_normal = 101300620
            drop_live_item3_hard = 101300630
            drop_live_item4_easy = 102300610
            drop_live_item4_normal = 102300620
            drop_live_item4_hard = 102300630
            drop_live_item5_easy = 103300610
            drop_live_item5_normal = 103300620
            drop_live_item5_hard = 103300630
        elif attribute_live == 4:
            drop_live_item1_easy = 104400610
            drop_live_item1_normal = 104400620
            drop_live_item1_hard = 104400630
            drop_live_item2_easy = 100400610
            drop_live_item2_normal = 100400620
            drop_live_item2_hard = 100400630
            drop_live_item3_easy = 101400610
            drop_live_item3_normal = 101400620
            drop_live_item3_hard = 101400630
            drop_live_item4_easy = 102400610
            drop_live_item4_normal = 102400620
            drop_live_item4_hard = 102400630
            drop_live_item5_easy = 103400610
            drop_live_item5_normal = 103400620
            drop_live_item5_hard = 103400630
        elif attribute_live == 5:
            drop_live_item1_easy = 104500610
            drop_live_item1_normal = 104500620
            drop_live_item1_hard = 104500630
            drop_live_item2_easy = 100500610
            drop_live_item2_normal = 100500620
            drop_live_item2_hard = 100500630
            drop_live_item3_easy = 101500610
            drop_live_item3_normal = 101500620
            drop_live_item3_hard = 101500630
            drop_live_item4_easy = 102500610
            drop_live_item4_normal = 102500620
            drop_live_item4_hard = 102500630
            drop_live_item5_easy = 103500610
            drop_live_item5_normal = 103500620
            drop_live_item5_hard = 103500630
        elif attribute_live == 6:
            drop_live_item1_easy = 104600610
            drop_live_item1_normal = 104600620
            drop_live_item1_hard = 104600630
            drop_live_item2_easy = 100600610
            drop_live_item2_normal = 100600620
            drop_live_item2_hard = 100600630
            drop_live_item3_easy = 101600610
            drop_live_item3_normal = 101600620
            drop_live_item3_hard = 101600630
            drop_live_item4_easy = 102600610
            drop_live_item4_normal = 102600620
            drop_live_item4_hard = 102600630
            drop_live_item5_easy = 103600610
            drop_live_item5_normal = 103600620
            drop_live_item5_hard = 103600630
        else:
            drop_live_item1_easy = 0
            drop_live_item1_normal = 0
            drop_live_item1_hard = 0
            drop_live_item2_easy = 0
            drop_live_item2_normal = 0
            drop_live_item2_hard = 0
            drop_live_item3_easy = 0
            drop_live_item3_normal = 0
            drop_live_item3_hard = 0
            drop_live_item4_easy = 0
            drop_live_item4_normal = 0
            drop_live_item4_hard = 0
            drop_live_item5_easy = 0
            drop_live_item5_normal = 0
            drop_live_item5_hard = 0
    elif member_group_live == 4:
        member_mapping_live = 10001
        if attribute_live == 1:
            drop_live_item1_easy = 104100410
            drop_live_item1_normal = 104100410
            drop_live_item1_hard = 104100410
            drop_live_item2_easy = 100100410
            drop_live_item2_normal = 100100410
            drop_live_item2_hard = 100100410
            drop_live_item3_easy = 101100410
            drop_live_item3_normal = 101100410
            drop_live_item3_hard = 101100410
            drop_live_item4_easy = 102100410
            drop_live_item4_normal = 102100410
            drop_live_item4_hard = 102100410
            drop_live_item5_easy = 103100410
            drop_live_item5_normal = 103100410
            drop_live_item5_hard = 103100410
        elif attribute_live == 2:
            drop_live_item1_easy = 104200410
            drop_live_item1_normal = 104200410
            drop_live_item1_hard = 104200410
            drop_live_item2_easy = 100200410
            drop_live_item2_normal = 100200410
            drop_live_item2_hard = 100200410
            drop_live_item3_easy = 101200410
            drop_live_item3_normal = 101200410
            drop_live_item3_hard = 101200410
            drop_live_item4_easy = 102200410
            drop_live_item4_normal = 102200410
            drop_live_item4_hard = 102200410
            drop_live_item5_easy = 103200410
            drop_live_item5_normal = 103200410
            drop_live_item5_hard = 103200410
        elif attribute_live == 4:
            drop_live_item1_easy = 104400410
            drop_live_item1_normal = 104400410
            drop_live_item1_hard = 104400410
            drop_live_item2_easy = 100400410
            drop_live_item2_normal = 100400410
            drop_live_item2_hard = 100400410
            drop_live_item3_easy = 101400410
            drop_live_item3_normal = 101400410
            drop_live_item3_hard = 101400410
            drop_live_item4_easy = 102400410
            drop_live_item4_normal = 102400410
            drop_live_item4_hard = 102400410
            drop_live_item5_easy = 103400410
            drop_live_item5_normal = 103400410
            drop_live_item5_hard = 103400410
        elif attribute_live == 6:
            drop_live_item1_easy = 104600410
            drop_live_item1_normal = 104600410
            drop_live_item1_hard = 104600410
            drop_live_item2_easy = 100600410
            drop_live_item2_normal = 100600410
            drop_live_item2_hard = 100600410
            drop_live_item3_easy = 101600410
            drop_live_item3_normal = 101600410
            drop_live_item3_hard = 101600410
            drop_live_item4_easy = 102600410
            drop_live_item4_normal = 102600410
            drop_live_item4_hard = 102600410
            drop_live_item5_easy = 103600410
            drop_live_item5_normal = 103600410
            drop_live_item5_hard = 103600410
        else:
            drop_live_item1_easy = 0
            drop_live_item1_normal = 0
            drop_live_item1_hard = 0
            drop_live_item2_easy = 0
            drop_live_item2_normal = 0
            drop_live_item2_hard = 0
            drop_live_item3_easy = 0
            drop_live_item3_normal = 0
            drop_live_item3_hard = 0
            drop_live_item4_easy = 0
            drop_live_item4_normal = 0
            drop_live_item4_hard = 0
            drop_live_item5_easy = 0
            drop_live_item5_normal = 0
            drop_live_item5_hard = 0
    elif member_group_live == 100:
        member_mapping_live = 10001
        drop_live_item1_easy = 0
        drop_live_item1_normal = 0
        drop_live_item1_hard = 0
        drop_live_item2_easy = 0
        drop_live_item2_normal = 0
        drop_live_item2_hard = 0
        drop_live_item3_easy = 0
        drop_live_item3_normal = 0
        drop_live_item3_hard = 0
        drop_live_item4_easy = 0
        drop_live_item4_normal = 0
        drop_live_item4_hard = 0
        drop_live_item5_easy = 0
        drop_live_item5_normal = 0
        drop_live_item5_hard = 0
    cursor.execute("INSERT INTO main.m_live (live_id, is_2d_live, music_id, bgm_path, chorus_bgm_path, live_member_mapping_id, name, pronunciation, member_group, member_unit, original_deck_name, copyright, source, jacket_asset_path, background_asset_path, display_order) VALUES (?, '1', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'SI', ?);",
                   (live_id_masterdata, music_id_masterdata, sheet_name_file, sheet_name_file1, member_mapping_live, music_name_dictionary_masterdata, donot_insert, member_group_live, donot_insert, donot_insert, music_id_copyright_masterdata, donot_insert, thumbnail_music_path, display_order_new))
   
    # liella attribute 3 & 5, union & untyped doesn't not have drop https://github.com/arina999999997/elichika/tree/master/docs#server-implement-progress
    # cannot get information AC, Note Gimmick & Live Gimmick
    # if you are dev, feel free to edit
    
    cursor.execute("INSERT INTO main.m_live_difficulty (live_difficulty_id, live_id, live_3d_asset_master_id, live_difficulty_type, unlock_pattern, default_attribute, target_voltage, note_emit_msec, recommended_score, recommended_stamina, consumed_lp, reward_user_exp, judge_id, note_drop_group_id, drop_choose_count, rare_drop_rate, drop_content_group_id, rare_drop_content_group_id, additional_drop_max_count, additional_drop_content_group_id, additional_rare_drop_content_group_id,bottom_technique, additional_drop_decay_technique, reward_base_love_point, evaluation_s_score, evaluation_a_score, evaluation_b_score, evaluation_c_score, updated_at, lose_at_death, autoplay_requirement_id, skip_master_id, stamina_voltage_group_id, combo_voltage_group_id, difficulty_const_master_id, is_count_target, insufficient_rate) VALUES (?, ?, ?, 10, '1', ?, ?, ?, ?, ?, '10', '8', '1', ?, '2', '1500', ?, ?, '2', ?, ?, '50000', '9000', '12', ?, ?, ?, ?, '0', '1', ?, '16001', '1', '1', ?, '1', '6000');",
                   (music_diff1_masterdata, live_id_masterdata, donot_insert, attribute_live, evaluation_s_score_easy, note_emit_msec_easy, recommend_power_easy, recommend_stamina_easy, drop_live_item1_easy, drop_live_item2_easy, drop_live_item3_easy, drop_live_item4_easy, drop_live_item5_easy, evaluation_s_score_easy, evaluation_a_score_easy, evaluation_b_score_easy, evaluation_c_score_easy, donot_insert, live_constaddon_easy,))

    cursor.execute("INSERT INTO main.m_live_difficulty (live_difficulty_id, live_id, live_3d_asset_master_id, live_difficulty_type, unlock_pattern, default_attribute, target_voltage, note_emit_msec, recommended_score, recommended_stamina, consumed_lp, reward_user_exp, judge_id, note_drop_group_id, drop_choose_count, rare_drop_rate, drop_content_group_id, rare_drop_content_group_id, additional_drop_max_count, additional_drop_content_group_id, additional_rare_drop_content_group_id,bottom_technique, additional_drop_decay_technique, reward_base_love_point, evaluation_s_score, evaluation_a_score, evaluation_b_score, evaluation_c_score, updated_at, lose_at_death, autoplay_requirement_id, skip_master_id, stamina_voltage_group_id, combo_voltage_group_id, difficulty_const_master_id, is_count_target, insufficient_rate) VALUES (?, ?, ?, 20, '1', ?, ?, ?, ?, ?, '12', '13', '2', ?, '2', '1300', ?, ?, '2', ?, ?, '60000', '9000', '16', ?, ?, ?, ?, '0', '1', ?, '16001', '1', '1', ?, '1', '6000');",
                   (music_diff2_masterdata, live_id_masterdata, donot_insert, attribute_live, evaluation_s_score_normal, note_emit_msec_normal, recommend_power_normal, recommend_stamina_normal, drop_live_item1_normal, drop_live_item2_normal, drop_live_item3_normal, drop_live_item4_normal, drop_live_item5_normal, evaluation_s_score_normal, evaluation_a_score_normal, evaluation_b_score_normal, evaluation_c_score_normal, donot_insert, live_constaddon_normal,))
                   
    cursor.execute("INSERT INTO main.m_live_difficulty (live_difficulty_id, live_id, live_3d_asset_master_id, live_difficulty_type, unlock_pattern, default_attribute, target_voltage, note_emit_msec, recommended_score, recommended_stamina, consumed_lp, reward_user_exp, judge_id, note_drop_group_id, drop_choose_count, rare_drop_rate, drop_content_group_id, rare_drop_content_group_id, additional_drop_max_count, additional_drop_content_group_id, additional_rare_drop_content_group_id,bottom_technique, additional_drop_decay_technique, reward_base_love_point, evaluation_s_score, evaluation_a_score, evaluation_b_score, evaluation_c_score, updated_at, lose_at_death, autoplay_requirement_id, skip_master_id, stamina_voltage_group_id, combo_voltage_group_id, difficulty_const_master_id, is_count_target, insufficient_rate) VALUES (?, ?, ?, 30, '1', ?, ?, ?, ?, ?, '15', '21', '3', ?, '2', '1000', ?, ?, '3', ?, ?, '70000', '9000', '24', ?, ?, ?, ?, '0', '1', ?, '16001', '1', '1', ?, '1', '6000');",
                   (music_diff3_masterdata, live_id_masterdata, donot_insert, attribute_live, evaluation_s_score_hard, note_emit_msec_hard, recommend_power_hard, recommend_stamina_hard, drop_live_item1_hard, drop_live_item2_hard, drop_live_item3_hard, drop_live_item4_hard, drop_live_item5_hard, evaluation_s_score_hard, evaluation_a_score_hard, evaluation_b_score_hard, evaluation_c_score_hard, donot_insert, live_constaddon_hard,))
                   
    cursor.execute("INSERT INTO main.m_live_difficulty_const (id, sp_gauge_length, sp_gauge_additional_rate, sp_gauge_reducing_point, sp_skill_voltage_magnification, note_stamina_reduce, note_voltage_upper_limit, collabo_voltage_upper_limit, skill_voltage_upper_limit, squad_change_voltage_upper_limit) VALUES (?, '3600', '10000', '50', '10000', ?, '100000', '250000', '50000', '30000');", (live_constaddon_easy, note_stamina_damage_easy,))
    cursor.execute("INSERT INTO main.m_live_difficulty_const (id, sp_gauge_length, sp_gauge_additional_rate, sp_gauge_reducing_point, sp_skill_voltage_magnification, note_stamina_reduce, note_voltage_upper_limit, collabo_voltage_upper_limit, skill_voltage_upper_limit, squad_change_voltage_upper_limit) VALUES (?, '4800', '10000', '75', '10000', ?, '100000', '250000', '50000', '30000');", (live_constaddon_normal, note_stamina_damage_normal,))
    cursor.execute("INSERT INTO main.m_live_difficulty_const (id, sp_gauge_length, sp_gauge_additional_rate, sp_gauge_reducing_point, sp_skill_voltage_magnification, note_stamina_reduce, note_voltage_upper_limit, collabo_voltage_upper_limit, skill_voltage_upper_limit, squad_change_voltage_upper_limit) VALUES (?, '6000', '10000', '100', '10000', ?, '100000', '250000', '50000', '30000');", (live_constaddon_hard, note_stamina_damage_hard,))
    # live end give you reward 10 stargem
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '1', '1', '1', '1', '0', '2');", (music_diff1_masterdata,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '2', '6', ?, '1', '0', '3');", (music_diff1_masterdata, evaluation_b_score_easy,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '3', '4', ?, '1', '0', '5');", (music_diff1_masterdata, evaluation_s_score_easy,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '1', '1', '1', '1', '0', '2');", (music_diff2_masterdata,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '2', '6', ?, '1', '0', '3');", (music_diff2_masterdata, evaluation_b_score_normal,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '3', '4', ?, '1', '0', '5');", (music_diff2_masterdata, evaluation_s_score_normal,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '1', '1', '1', '1', '0', '2');", (music_diff3_masterdata,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '2', '6', ?, '1', '0', '3');", (music_diff3_masterdata, evaluation_b_score_hard,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '3', '4', ?, '1', '0', '5');", (music_diff3_masterdata, evaluation_s_score_hard,))
    
    if 'videoprime_file' in globals() or 'videoprime_file' in locals():
        cursor.execute("INSERT INTO main.m_live_movie (live_id, codec, movie_asset_path, stage_background_asset_path) VALUES (?, 'prime', ?, 'Bl7');", (live_id_masterdata, movie_genpath))
        
with sqlite3.connect('assets/db/gl/dictionary_en_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (music_name_dictionary_dic, music_name))
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (music_id_copyright_dic, music_copyright_name))
    
with sqlite3.connect('assets/db/gl/dictionary_ko_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (music_name_dictionary_dic, music_name))
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (music_id_copyright_dic, music_copyright_name))
    
with sqlite3.connect('assets/db/gl/dictionary_zh_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (music_name_dictionary_dic, music_name))
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (music_id_copyright_dic, music_copyright_name))

saved_diffx = "assets/stages/"
output_filename1 = saved_diffx + f"{music_diff1_masterdata}.json"
output_filename2 = saved_diffx + f"{music_diff2_masterdata}.json"
output_filename3 = saved_diffx + f"{music_diff3_masterdata}.json"

with open(easy_difficulty_file, 'r') as difficult_file:
    data_difff = json.load(difficult_file)
            
    data_difff["live_difficulty_id"] = music_diff1_masterdata
    
        
    with open(output_filename1, 'w') as difficult_file:
        json.dump(data_difff, difficult_file, indent=2)
    
with open(normal_difficulty_file, 'r') as difficult_file:
    data_difff = json.load(difficult_file)
            
    data_difff["live_difficulty_id"] = music_diff2_masterdata
    
        
    with open(output_filename2, 'w') as difficult_file:
        json.dump(data_difff, difficult_file, indent=2)
    
with open(hard_difficulty_file, 'r') as difficult_file:
    data_difff = json.load(difficult_file)
            
    data_difff["live_difficulty_id"] = music_diff3_masterdata
    
        
    with open(output_filename3, 'w') as difficult_file:
        json.dump(data_difff, difficult_file, indent=2)
# Check if the file exists
print("deleting temp folder")
shutil.rmtree(temp_directory, ignore_errors=True)
print("FINISHED")
print("go to ~/elichika/encrypted_data/ & copy files folder to android/data/com.klab.lovelive.allstars.global(jp version path is similar) to something else")
sys.exit(1)
