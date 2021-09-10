import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file_csv', type=str, required=True)
args = parser.parse_args()

csv_name = args.file_csv
df = pd.read_csv(os.getcwd() + '/' + csv_name)

try:
    conn = psycopg2.connect(
        user='postgres', password='postgres', host='127.0.0.1', port='5432')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = conn.cursor()

    sql = f'''CREATE database {csv_name[:-4]};'''

    cursor.execute(sql)

except Exception as e:
    print(e)
