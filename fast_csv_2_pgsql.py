import psycopg2
import pandas as pd


conn = psycopg2.connect(database='aih', user='aih', host='host',password='pass')
cur = conn.cursor()



df = pd.read_csv('RDSC1906.csv', sep=",", low_memory=False)

df.to_csv('slice.csv',columns=['N_AIH', 'NASC', 'SEXO', 'MUNIC_RES', 'DT_SAIDA', 'PROC_SOLIC', 'PROC_REA', 'MORTE', 'UF_ZI', 'DIAG_PRINC', 'DT_INTER', 'CNES'], index=False)

with open('slice.csv', 'r') as f:
    next(f) 
    cur.copy_from(f, 'aih_rd_data', sep=',')
    conn.commit()