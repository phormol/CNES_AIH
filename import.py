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
                        query = "select count(*) as total from tb_dbf where no_arquivo = '{0}'".format(filename_no_ext)
                        cursor.execute(query)
                        processed = cursor.fetchall()
                        if processed[0][0] == 0:
                                arquivoOrigem = datapath + filename
                                pastalib.executarScript("dbf2dbc.exe " + arquivoOrigem + " " + datapath)
                                dbf = datapath + filename_no_ext + '.dbf'
                                csv = datapath + filename_no_ext + '.csv'
                                pastalib.executarScript('dbf2csv -ie ISO-8859-1 -oe ISO-8859-1 ' + dbf + ' ' + csv )

                                data = pd.read_csv(csv, sep=",", encoding='ISO-8859-1')
                                i = 1
                                query = "INSERT INTO public.aih_rd(n_aih, nasc, sexo, munic_res, dt_inter, dt_saida, proc_solic, proc_rea, morte, uf_zi, diag_princ) VALUES "
                                try:
                                        data = pd.read_csv(csv, sep=",")
                                except:
                                        a = 1   
                                if (data.values.shape[0] > 0):             
                                        for d in data.values:
                                                
                                                nasc = str(d[9])
                                                nasc = nasc[:4] + '-' + nasc[4:6] + '-' + nasc[6:8] 
                                                dt_inter = str(d[38])
                                                dt_inter = dt_inter[:4] + '-' + dt_inter[4:6] + '-' + dt_inter[6:8]
                                                dt_saida = str(d[39])
                                                dt_saida = dt_saida[:4] + '-' + dt_saida[4:6] + '-' + dt_saida[6:8]

                                                if (i == data.values.shape[0]):
                                                        query += " ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', {8}, '{9}', '{10}')".format(d[5], nasc, d[10], d[8], dt_inter, dt_saida, d[22], d[23], d[51], d[0], d[40])
                                                else:
                                                        query += " ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', {8}, '{9}', '{10}'),".format(d[5], nasc, d[10], d[8], dt_inter, dt_saida, d[22], d[23], d[51], d[0], d[40])

                                                print(d[5])
                                                i = i + 1
                                query2 = "INSERT INTO public.tb_dbf(no_arquivo) VALUES ('{0}')".format(filename_no_ext)        
                                try:    
                                        if (data.values.shape[0] > 0):
                                                cursor.execute(query)
                                        cursor.execute(query2)        
                                        conn.commit()
                                except AssertionError as error:
                                        print(error)  
                except AssertionError as error:
                        print(error)                                                    


