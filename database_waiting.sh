#!/bin/sh
# my tricky script for waiting 4 database

until timeout -t 2 nc -z database 3306; do
    continue
done

${@}
