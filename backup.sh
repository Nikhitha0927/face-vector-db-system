#!/bin/bash

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

pg_dump \
-U postgres \
-h localhost \
-p 5433 \
postgres \
> backups/backup_$TIMESTAMP.sql

echo "Backup Completed"
