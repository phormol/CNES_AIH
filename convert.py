import os.path
import os
import psycopg2
import pastalib
import csv
import pandas as pd

pastaLocal = 'D:/python/aih/data/ST'



datapath = os.getcwd() + '\\data\\'

datapath = 'D:\\python\\aih\\data\\ST\\'

for r, d, f in os.walk(pastaLocal):
    for filename in f:
            try:

                posicao = filename.find(".")
                filename_no_ext = filename[0:posicao]
                arquivoOrigem = datapath + filename
                pastalib.executarScript("dbf2dbc.exe " + arquivoOrigem + " " + datapath)
                #dbf = datapath + filename_no_ext + '.dbf'
                #csv = datapath + filename_no_ext + '.csv'
                #pastalib.executarScript('dbf2csv -ie utf-8 -oe ANSI ' + dbf + ' ' + csv )


                     
            except AssertionError as error:
                print(error)                                                    


