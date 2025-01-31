import sqlite3

def query_messages():
    # Connect to SQLite database
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the query to fetch all messages
    cursor.execute('SELECT * FROM messages')

    # Fetch all rows from the result of the query
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Print the fetched messages
    for row in rows:
        print(f"ID: {row['id']}, Message: {row['content']}")

# Run the function
query_messages()
