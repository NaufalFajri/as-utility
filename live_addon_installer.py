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
    music_name_dictionary_masterdata = "inline_image.song_name_so" + str(live_id_masterdata)
    music_id_copyright_masterdata = "inline_image.song_copyright_so" + str(live_id_masterdata)
    music_name_dictionary_dic = "song_name_so" + str(live_id_masterdata)
    music_id_copyright_dic = "song_copyright_so" + str(live_id_masterdata)
    
    # Find the minimum display_order for the given chara_id
    cursor.execute("SELECT MAX(display_order) FROM main.m_live WHERE member_group=?;", (member_group_live,))
    result = cursor.fetchone()
    min_display_order = result[0] if result[0] is not None else 0

    # Calculate the new display_order (decrease by 1)
    display_order_new = min_display_order + 1

    # Insert the new record with the updated display_order
    if member_group_live == 1:
        member_mapping_live = 10001
    elif member_group_live == 2:
        member_mapping_live = 11001
    elif member_group_live == 3:
        member_mapping_live = 12001
    elif member_group_live == 4:
        member_mapping_live = 10001 # there no liella chibi so i will reuse myuzu
    cursor.execute("INSERT INTO main.m_live (live_id, is_2d_live, music_id, bgm_path, chorus_bgm_path, live_member_mapping_id, name, pronunciation, member_group, member_unit, original_deck_name, copyright, source, jacket_asset_path, background_asset_path, display_order) VALUES (?, '1', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'SI', ?);",
                   (live_id_masterdata, music_id_masterdata, sheet_name_file, sheet_name_file1, member_mapping_live, music_name_dictionary_masterdata, donot_insert, member_group_live, donot_insert, donot_insert, music_id_copyright_masterdata, donot_insert, thumbnail_music_path, display_order_new))
   
    # using template live_id 12048
    # by defualt maximum score to get is 4 which is pointless (1C, 2B, 3A, 4S)
    # no consumed LP
    # no reward
    # no drop item
    # no skip ticket requirement
    # no stamina damage
    # no recommend requirement
    # if you are dev, feel free to edit
    
    cursor.execute("INSERT INTO main.m_live_difficulty (live_difficulty_id, live_id, live_3d_asset_master_id, live_difficulty_type, unlock_pattern, default_attribute, target_voltage, note_emit_msec, recommended_score, recommended_stamina, consumed_lp, reward_user_exp, judge_id, note_drop_group_id, drop_choose_count, rare_drop_rate, drop_content_group_id, rare_drop_content_group_id, additional_drop_max_count, additional_drop_content_group_id, additional_rare_drop_content_group_id,bottom_technique, additional_drop_decay_technique, reward_base_love_point, evaluation_s_score, evaluation_a_score, evaluation_b_score, evaluation_c_score, updated_at, lose_at_death, autoplay_requirement_id, skip_master_id, stamina_voltage_group_id, combo_voltage_group_id, difficulty_const_master_id, is_count_target, insufficient_rate) VALUES (?, ?, ?, 10, '1', ?, '4', '3620', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '50000', '9000', '0', '4', '3', '2', '1', '0', '1', ?, ?, '1', '1', '10027101', '1', '0');",
                   (music_diff1_masterdata, live_id_masterdata, donot_insert, attribute_live, donot_insert, donot_insert,))

    cursor.execute("INSERT INTO main.m_live_difficulty (live_difficulty_id, live_id, live_3d_asset_master_id, live_difficulty_type, unlock_pattern, default_attribute, target_voltage, note_emit_msec, recommended_score, recommended_stamina, consumed_lp, reward_user_exp, judge_id, note_drop_group_id, drop_choose_count, rare_drop_rate, drop_content_group_id, rare_drop_content_group_id, additional_drop_max_count, additional_drop_content_group_id, additional_rare_drop_content_group_id,bottom_technique, additional_drop_decay_technique, reward_base_love_point, evaluation_s_score, evaluation_a_score, evaluation_b_score, evaluation_c_score, updated_at, lose_at_death, autoplay_requirement_id, skip_master_id, stamina_voltage_group_id, combo_voltage_group_id, difficulty_const_master_id, is_count_target, insufficient_rate) VALUES (?, ?, ?, 20, '1', ?, '4', '3077', '0', '0', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '60000', '9000', '0', '4', '3', '2', '1', '0', '1', ?, ?, '1', '1', '10027201', '1', '0');",
                   (music_diff2_masterdata, live_id_masterdata, donot_insert, attribute_live, donot_insert, donot_insert,))
                   
    cursor.execute("INSERT INTO main.m_live_difficulty (live_difficulty_id, live_id, live_3d_asset_master_id, live_difficulty_type, unlock_pattern, default_attribute, target_voltage, note_emit_msec, recommended_score, recommended_stamina, consumed_lp, reward_user_exp, judge_id, note_drop_group_id, drop_choose_count, rare_drop_rate, drop_content_group_id, rare_drop_content_group_id, additional_drop_max_count, additional_drop_content_group_id, additional_rare_drop_content_group_id,bottom_technique, additional_drop_decay_technique, reward_base_love_point, evaluation_s_score, evaluation_a_score, evaluation_b_score, evaluation_c_score, updated_at, lose_at_death, autoplay_requirement_id, skip_master_id, stamina_voltage_group_id, combo_voltage_group_id, difficulty_const_master_id, is_count_target, insufficient_rate) VALUES (?, ?, ?, 30, '1', ?, '4', '2534', '0', '0', '0', '0', '3', '0', '0', '0', '0', '0', '0', '0', '0', '70000', '9000', '0', '4', '3', '2', '1', '0', '1', ?, ?, '1', '1', '10027301', '1', '0');",
                   (music_diff3_masterdata, live_id_masterdata, donot_insert, attribute_live, donot_insert, donot_insert,))
                   
    # live end give you reward 10 stargem
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '1', '1', '1', '1', '0', '2');", (music_diff1_masterdata,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '2', '6', '2', '1', '0', '3');", (music_diff1_masterdata,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '3', '4', '4', '1', '0', '5');", (music_diff1_masterdata,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '1', '1', '1', '1', '0', '2');", (music_diff2_masterdata,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '2', '6', '2', '1', '0', '3');", (music_diff2_masterdata,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '3', '4', '4', '1', '0', '5');", (music_diff2_masterdata,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '1', '1', '1', '1', '0', '2');", (music_diff3_masterdata,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '2', '6', '2', '1', '0', '3');", (music_diff3_masterdata,))
    cursor.execute("INSERT INTO main.m_live_difficulty_mission (live_difficulty_master_id, position, target_type, target_value, content_type, content_id, content_amount) VALUES (?, '3', '4', '4', '1', '0', '5');", (music_diff3_masterdata,))
    
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
