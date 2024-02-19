import snowflake.connector

# Connection Details
conn_info = {
    'user': 'MODIRI2899',
    'password': '#Prats1598shah',
    'account': 'fwxbofb-iab18914',
    'warehouse': 'COMPUTE_WH',
    'role': 'ACCOUNTADMIN'
}

# Connect to Snowflake
conn = snowflake.connector.connect(**conn_info)
cur = conn.cursor()

try:
    # Creating a Database
    cur.execute('CREATE DATABASE IF NOT EXISTS predictit')
    
except Exception as e:
    print(f'An error occurred: {e}')
    
finally:
    cur.close()
    conn.close()