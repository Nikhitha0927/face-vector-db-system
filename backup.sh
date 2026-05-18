#!/bin/bash

DATE=$(date +%Y-%m-%d_%H-%M-%S)

BACKUP_DIR="./backups"

mkdir -p $BACKUP_DIR

pg_dump -U postgres -h localhost -p 5433 postgres > \
$BACKUP_DIR/backup_$DATE.sql

echo "Backup completed"
