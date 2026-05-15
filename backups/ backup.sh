#!/bin/bash

pg_dump -U postgres -h localhost -p 5433 postgres > backup.sql

echo "Backup completed successfully"