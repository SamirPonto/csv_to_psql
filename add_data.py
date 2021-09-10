import pandas as pd
import argparse
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import sys

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--csv_file',  type=str, required=True)
parser.add_argument('-n', '--nrows',  type=int, required=True)
parser.add_argument('-c', '--connstring', type=str, required=False)
parser.add_argument('-t', '--table_name', type=str, required=True)
parser.add_argument('-r', '--replace', type=str, required=False)  # adicionado

args = parser.parse_args()

csv_name = args.csv_file
db_conn = args.connstring
table = args.table_name
replace = args.replace

if not db_conn:
    # Do you need put the postgresql://... in .env
    db_conn = os.getenv('DB_CONNSTRING')

engine = None

try:
    engine = create_engine(db_conn)
except Exception as e:
    print("Falha ao conectar no banco de dados, verifique a conexão", e)
    sys.exit(1)

if __name__ == '__main__':

    # Replace a data in already table.
    # Careful, this will change the column's name.
    if replace == 'r':
        for df in pd.read_csv(os.getcwd() + '/' + csv_name, chunksize=args.nrows):
            try:
                df.to_sql(table,
                          engine,
                          index=False,
                          if_exists='replace')
            except Exception as e:
                print("error ao tentar inserir no banco:", e)

    # Just append data in the table.
    elif not replace:
        for df in pd.read_csv(os.getcwd() + '/' + csv_name, chunksize=args.nrows):
            try:
                df.to_sql(table,
                          engine,
                          index=False,
                          if_exists='append')
            except Exception as e:
                print("error ao tentar inserir no banco:", e)
