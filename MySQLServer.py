import mysql.connector
from mysql.connector import Error


def create_database():
    """Create the alx_book_store database if it doesn't exist"""
    
    # Database configuration
    db_config = {
        'host': 'localhost',
        'user': 'root',  # Change this to your MySQL username
        'password': 'root'   # Change this to your MySQL password
    }
    
    connection = None
    cursor = None
    
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(**db_config)
        
        if connection.is_connected():
            # Create cursor
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            # Using IF NOT EXISTS to prevent errors if database already exists
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            
            cursor.execute(create_db_query)
            
            # Commit is not needed for CREATE DATABASE but good practice
            connection.commit()
            
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error connecting to MySQL or creating database: {e}")
        
    finally:
        # Close cursor and connection properly
        if cursor is not None:
            cursor.close()
            print("Cursor closed.")
            
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")


if __name__ == "__main__":
    create_database()