import sqlite3
import random

print("elichika Costume Clone")

def generate_unique_costume_id(cursor):
    while True:
        new_id = random.randint(0, 999999999)
        cursor.execute("SELECT COUNT(*) FROM main.m_suit WHERE id = ?;", (new_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            return new_id

# Input values
costume_id = input("Enter source costume_id: ")
chara_id = input("Enter target chara_id: ")
input("is everything correct?, Press Enter to add")

# Open the SQLite database file
conn = sqlite3.connect('jp/masterdata.db')
cursor = conn.cursor()

costume_id_masterdata = generate_unique_costume_id(cursor)

# Select the row containing the specified costume_id
cursor.execute("SELECT * FROM m_suit WHERE id=?", (costume_id,))
row = cursor.fetchone()

if row is not None:
    # Extract the necessary values from the selected row
    (_, member_m_id, _, _, _, _, _, _) = row

    # Calculate the new_display_sort value
    cursor.execute("SELECT MIN(display_order) FROM m_suit WHERE member_m_id=?", (member_m_id,))
    min_display_order = cursor.fetchone()[0]
    new_display_sort = min_display_order - 1

    # Insert a new row into the table
    cursor.execute("""
        INSERT INTO m_suit (id, member_m_id, name, thumbnail_image_asset_path, suit_release_route, 
                                     suit_release_value, model_asset_path, display_order)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (costume_id_masterdata, chara_id, row[2], row[3], row[4], row[5], row[6], new_display_sort))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

    with sqlite3.connect('serverdata.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO main.s_user_suit (user_id, suit_master_id, is_new) VALUES ('588296696', ?, '1');", (costume_id_masterdata,))


    print("costume copied to database.")
    

else:
    print("No row found with costume_id:", costume_id)
