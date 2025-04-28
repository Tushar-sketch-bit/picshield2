import sqlite3

def init_db():
    conn = sqlite3.connect('tracking.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (image_id TEXT, ip TEXT, timestamp TEXT, location TEXT)''')
    conn.commit()
    conn.close()

def log_access(image_id, ip):
    """Record who accessed the image"""
    conn = sqlite3.connect('tracking.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs VALUES (?,?,datetime('now'),NULL)",
              (image_id, ip))
    conn.commit()
    conn.close()