from db import create_tables

def main():
    print("db.py loaded successfully")
    print("Creating all tables...")
    create_tables()
    print("Database setup completed successfully")

if __name__ == "__main__":
    main()
