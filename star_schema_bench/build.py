#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path
import csv

# Move to script directory
SCRIPT_DIR = Path(__file__).resolve().parent

# Change to SSB directory and build
print("building ...")
os.chdir(f"{SCRIPT_DIR}/StarSchemaBenchmark")
subprocess.run(["make"], check=True)

# Generate data
print("generating data ...")
subprocess.run(["./dbgen", "-fT", "a"], check=True)

# Convert .tbl to .csv
tables = ["supplier", "part", "lineorder", "date", "customer"]
data_dir = Path("../data")

for table in tables:
    path_src = f"{table}.tbl"
    path_dest = f"{data_dir}/{table}.csv"
    with (
        open(path_src, newline='', encoding="utf-8") as infile,
        open(path_dest, "w", newline='', encoding="utf-8") as outfile
    ):
        print(f"converting {table} ...")
        reader = csv.reader(infile, delimiter='|')
        writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            writer.writerow(row)

print(f"done")
