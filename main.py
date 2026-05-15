from db import create_tables

def main():
    print("Creating database tables...")
    create_tables()
    print("Database setup completed successfully")

if __name__ == "__main__":
    main()