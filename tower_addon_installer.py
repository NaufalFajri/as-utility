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
def generate_unique_tower_id(cursor):
    while True:
        new_id333 = random.randint(0, 999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_tower WHERE tower_id = ?;", (new_id333,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id333
            
def generate_unique_towerperiod_id(cursor):
    while True:
        new_id3334 = random.randint(0, 999999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_tower_period WHERE id = ?;", (new_id3334,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id3334
                        
def thumbnail_path_randomhash(cursor):
    while True:
        new_hash2 = format(random.randint(0, 0xFFFFFFFF), 'x')
        cursor.execute("SELECT COUNT(*) FROM main.texture WHERE asset_path = ?;", (new_hash2,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_hash2
            
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
                try:
                    file_content = txt_file.read()
                    exec(file_content)
                except Exception as e:
                    print(f"Error executing file: {file_info.filename}\nError: {e}")


# Get user inputs
clear_terminal()
print('Name: ' + tower_name)
print('Description: ' + tower_description)
do_you_think_want_add_this = input("do you want add this? (y/n): ")

if do_you_think_want_add_this == "y" :
    clear_terminal()
else :
    clear_terminal()
    shutil.rmtree(temp_directory, ignore_errors=True)
    sys.exit(1)


# Extract filename and filesize from tower_thumbnail_file
tower_thumbnail_filename = "0_" + os.path.splitext(tower_thumbnail_file.split("/")[-1])[0]
# Replace with actual method to get filesize
tower_thumbnail_size = os.path.getsize(tower_thumbnail_file)

encrypted_thumbnail = "encrypted_data/files/files/pkg0/0_" + os.path.splitext(tower_thumbnail_file.split("/")[-1])[0]

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
    
with open(tower_thumbnail_file, "rb") as file:
    data = bytearray(file.read())

    key_0 = 12345
    key_1 = 0
    key_2 = 0
    print("encrypting tower thumbnail")
    manipulate_file(data, key_0, key_1, key_2)

    with open(encrypted_thumbnail, "wb") as file:
        file.write(data)

print("assets encrypted")
with sqlite3.connect('assets/db/jp/asset_a_ja.db') as conn:
    cursor = conn.cursor()
    
    tower_thumbnail_path = thumbnail_path_randomhash(cursor)
    
    # (light download auto delete fix)
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (tower_thumbnail_filename,))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (tower_thumbnail_path, tower_thumbnail_filename, tower_thumbnail_size))                                 

# REST CODE TO GL CLIENT & IOS PLATFORM

with sqlite3.connect('assets/db/jp/asset_i_ja.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (tower_thumbnail_filename,))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (tower_thumbnail_path, tower_thumbnail_filename, tower_thumbnail_size))

with sqlite3.connect('assets/db/gl/asset_a_en.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (tower_thumbnail_filename,))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (tower_thumbnail_path, tower_thumbnail_filename, tower_thumbnail_size))

with sqlite3.connect('assets/db/gl/asset_i_en.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (tower_thumbnail_filename,))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (tower_thumbnail_path, tower_thumbnail_filename, tower_thumbnail_size))

with sqlite3.connect('assets/db/gl/asset_a_ko.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (tower_thumbnail_filename,))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (tower_thumbnail_path, tower_thumbnail_filename, tower_thumbnail_size))

with sqlite3.connect('assets/db/gl/asset_i_ko.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (tower_thumbnail_filename,))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (tower_thumbnail_path, tower_thumbnail_filename, tower_thumbnail_size))

with sqlite3.connect('assets/db/gl/asset_a_zh.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (tower_thumbnail_filename,))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (tower_thumbnail_path, tower_thumbnail_filename, tower_thumbnail_size))

with sqlite3.connect('assets/db/gl/asset_i_zh.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO main.m_asset_pack (pack_name, auto_delete) VALUES (?, '0');", (tower_thumbnail_filename,))
    cursor.execute("INSERT INTO main.texture (asset_path, pack_name, head, size, key1, key2) VALUES (?, ?, '0', ?, '0', '0');",
                   (tower_thumbnail_path, tower_thumbnail_filename, tower_thumbnail_size))

# Connect to masterdata.db and perform INSERT
with sqlite3.connect('assets/db/jp/masterdata.db') as conn:
    cursor = conn.cursor()

    # Generate a unique costume_id_masterdata
    tower_id_masterdata = generate_unique_tower_id(cursor)
    tower_period_masterdata = generate_unique_towerperiod_id(cursor)
    tower_dictionary = "event_tower_title_" + str(tower_id_masterdata)
    tower_dictionary_masterdata = "inline_image." + tower_dictionary
    donot_insert = None 
    
    # Find the minimum display_order for the given chara_id
    cursor.execute("SELECT MAX(display_order) FROM main.m_tower;", ())
    result = cursor.fetchone()
    min_display_order_ja = result[0] if result[0] is not None else 0

    # Calculate the new display_order (decrease by 1)
    display_order_new_ja = min_display_order_ja + 1
    floor_no_start = 1
    default_consume_perfomance = 1
    # cannot get free recovery
    # cannot get reward
    # card limit by default is 1
    cursor.execute("INSERT INTO main.m_tower (tower_id, title, thumbnail_asset_path, display_order, tower_composition_id, trade_master_id, entry_restriction_type, entry_restriction_condition, card_use_limit, card_recovery_limit, free_recover_point_recovery_at, free_recover_point_max_count, recover_cost_by_sns_coin, background_asset_path) VALUES (?, ?, ?, ?, ?, '33000', '99', ?, '1', '3', '0', '5', '5', '0l?');",
                   (tower_id_masterdata, tower_dictionary_masterdata, tower_thumbnail_path, display_order_new_ja, tower_id_masterdata, donot_insert))
    for i, preset in enumerate(tower_composition_preset, start=floor_no_start):
        cursor.execute("""
            INSERT INTO main.m_tower_composition (
                tower_id, floor_no, name, thumbnail_asset_path,
                popup_thumbnail_asset_path, consume_performance, tower_cell_type,
                scenario_script_asset_path, live_difficulty_id, target_voltage,
                super_stage_asset_path, still_asset_path, music_id,
                tower_clear_reward_id, tower_progress_reward_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            tower_id_masterdata,  # tower_id
            str(i),  # floor_no (convert to string)
            tower_dictionary_masterdata,  # name
            donot_insert,  # thumbnail_asset_path
            donot_insert,  # popup_thumbnail_asset_path
            default_consume_perfomance,  # consume_performance
            preset[2],  # tower_cell_type
            donot_insert,  # scenario_script_asset_path
            preset[0],  # live_difficulty_id
            preset[1],  # target_voltage
            donot_insert,  # super_stage_asset_path
            donot_insert,  # still_asset_path
            donot_insert,  # music_id
            donot_insert,  # tower_clear_reward_id
            donot_insert,  # tower_progress_reward_id
        ))
    # Insert the new record with the updated display_order
   # cursor.execute("INSERT INTO main.m_tower_composition (tower_id, floor_no, name, thumbnail_asset_path, , popup_thumbnail_asset_path, consume_performance, tower_cell_type, scenario_script_asset_path, live_difficulty_id, target_voltage, super_stage_asset_path, still_asset_path,music_id, tower_clear_reward_id, tower_progress_reward_id) VALUES (?, '0');", (tower_composition_id_masterdata, floor_no_increasement, tower_name, donot_insert, donot_insert, tower_composition_preset[3], donot_insert, tower_composition_preset[1], tower_composition_preset[2], donot_insert, donot_insert, donot_insert, donot_insert, donot_insert,))
    cursor.execute("INSERT INTO main.m_tower_period (id, tower_id, start_at, opened_at, closed_at, result_at, end_at) VALUES (?, ?, '1616047200', '1616047200', '2147483647', '2147483647', '2147483647');", (tower_period_masterdata, tower_id_masterdata,))
   
with sqlite3.connect('assets/db/gl/masterdata.db') as conn:
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(display_order) FROM main.m_tower;", ())
    result = cursor.fetchone()
    min_display_order_en = result[0] if result[0] is not None else 0

    # Calculate the new display_order (decrease by 1)
    display_order_new_ja = min_display_order_en + 1
    floor_no_start_en = 1
    cursor.execute("INSERT INTO main.m_tower (tower_id, title, thumbnail_asset_path, display_order, tower_composition_id, trade_master_id, entry_restriction_type, entry_restriction_condition, card_use_limit, card_recovery_limit, free_recover_point_recovery_at, free_recover_point_max_count, recover_cost_by_sns_coin, background_asset_path) VALUES (?, ?, ?, ?, ?, '33000', '99', ?, '1', '3', '0', '5', '5', '0l?');",
                   (tower_id_masterdata, tower_dictionary_masterdata, tower_thumbnail_path, display_order_new_ja, tower_id_masterdata, donot_insert))
    for i, preset in enumerate(tower_composition_preset, start=floor_no_start_en):
        cursor.execute("""
            INSERT INTO main.m_tower_composition (
                tower_id, floor_no, name, thumbnail_asset_path,
                popup_thumbnail_asset_path, consume_performance, tower_cell_type,
                scenario_script_asset_path, live_difficulty_id, target_voltage,
                super_stage_asset_path, still_asset_path, music_id,
                tower_clear_reward_id, tower_progress_reward_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            tower_id_masterdata,  # tower_id
            str(i),  # floor_no (convert to string)
            tower_dictionary_masterdata,  # name
            donot_insert,  # thumbnail_asset_path
            donot_insert,  # popup_thumbnail_asset_path
            default_consume_perfomance,  # consume_performance
            preset[2],  # tower_cell_type
            donot_insert,  # scenario_script_asset_path
            preset[0],  # live_difficulty_id
            preset[1],  # target_voltage
            donot_insert,  # super_stage_asset_path
            donot_insert,  # still_asset_path
            donot_insert,  # music_id
            donot_insert,  # tower_clear_reward_id
            donot_insert,  # tower_progress_reward_id
        ))
    cursor.execute("INSERT INTO main.m_tower_period (id, tower_id, start_at, opened_at, closed_at, result_at, end_at) VALUES (?, ?, '1616047200', '1616047200', '2147483647', '2147483647', '2147483647');", (tower_period_masterdata, tower_id_masterdata,))

with sqlite3.connect('assets/db/jp/dictionary_ja_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (tower_dictionary, tower_name))

with sqlite3.connect('assets/db/gl/dictionary_en_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (tower_dictionary, tower_name))
    
with sqlite3.connect('assets/db/gl/dictionary_ko_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (tower_dictionary, tower_name))
    
with sqlite3.connect('assets/db/gl/dictionary_zh_inline_image.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.m_dictionary (id, message) VALUES (?, ?);", (tower_dictionary, tower_name))
            

print("deleting temp folder")
shutil.rmtree(temp_directory, ignore_errors=True)
print("FINISHED")
print("THIS DLP CREATION IS WORK IN PROGRESS")
print("go to ~/elichika/encrypted_data/ & copy files folder to android/data/com.klab.lovelive.allstars.global(jp version path is similar) to something else")
sys.exit(1)

