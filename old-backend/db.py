# db.py
import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_mappings (
    okta_user_id TEXT PRIMARY KEY,
    junction_user_id TEXT NOT NULL
)
""")
conn.commit()

# Maps oktaUserId to junctionUserId
def save_user_mapping(okta_user_id: str, junction_user_id: str):
    cursor.execute("""
        INSERT OR REPLACE INTO user_mappings (okta_user_id, junction_user_id)
        VALUES (?, ?)
    """, (okta_user_id, junction_user_id))
    conn.commit()
    print(f"[DB] Saving mapping: {okta_user_id} -> {junction_user_id}")

def get_junction_user_id(okta_user_id: str):
    print(f"[DB] Looking up junction_user_id for: {okta_user_id}")
    cursor.execute("""
        SELECT junction_user_id FROM user_mappings WHERE okta_user_id = ?
    """, (okta_user_id,))
    result = cursor.fetchone()
    print(f"[DB] Result: {result}")
    cursor.execute("SELECT * FROM user_mappings")
    print("[DB] All mappings:", cursor.fetchall())
    return result[0] if result else None

