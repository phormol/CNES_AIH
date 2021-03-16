import os.path
import os
import psycopg2
import pastalib
import csv
import pandas as pd

pastaLocal = 'D:/python/aih/data/DF'

conn = psycopg2.connect(database='aih', user='aih', host='host',password='pass')
cursor = conn.cursor()

datapath = os.getcwd() + '\\data\\'

datapath = 'D:\\python\\aih\\data\\DF\\'

for r, d, f in os.walk(pastaLocal):
    for filename in f:
        try:
            posicao = filename.find(".")
            filename_no_ext = filename[0:posicao]
            print('*** Importando arquivo ' + filename_no_ext)    

            query = "select count(*) as total from tb_dbf where no_arquivo = '{0}'".format(filename_no_ext)
            cursor.execute(query)
            processed = cursor.fetchall()
            if processed[0][0] == 0:
                arquivoOrigem = datapath + filename
                pastalib.executarScript("dbf2dbc.exe " + arquivoOrigem + " " + datapath)
                dbf = datapath + filename_no_ext + '.dbf'
                csv = datapath + filename_no_ext + '.csv'
                pastalib.executarScript('dbf2csv -ie ISO-8859-1 -oe ISO-8859-1 ' + dbf + ' ' + csv )
                df = pd.read_csv(csv, sep=",", encoding='ISO-8859-1', low_memory=False)
                df.to_csv('temp_' + filename_no_ext + '.csv' ,columns=['N_AIH', 'NASC', 'SEXO', 'MUNIC_RES', 'DT_SAIDA', 'PROC_SOLIC', 'PROC_REA', 'MORTE', 'UF_ZI', 'DIAG_PRINC', 'DT_INTER', 'CNES'], index=False)

                with open('temp_' + filename_no_ext + '.csv', 'r') as f:
                    next(f) 
                    cursor.copy_from(f, 'aih_rd_data', sep=',')
                    query2 = "INSERT INTO public.tb_dbf(no_arquivo) VALUES ('{0}')".format(filename_no_ext)        
                    try:    
                        cursor.execute(query)
                        cursor.execute(query2)        
                        conn.commit()
                    except AssertionError as error:
                        print(error)  
        except AssertionError as error:
            print(error)                                                    


