import os
from datetime import datetime


def create_backup():

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    backup_file = (
        f"backups/backup_{timestamp}.sql"
    )

    command = f"""

    pg_dump \
    -U postgres \
    -h localhost \
    -p 5433 \
    postgres > {backup_file}

    """

    os.system(command)

    print("Backup Created:", backup_file)


if __name__ == "__main__":

    create_backup()