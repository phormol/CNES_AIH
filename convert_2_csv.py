import csv
from dbfread import DBF
import os.path
import os
import psycopg2
import pastalib
import csv
import pandas as pd

def decript(val):
    dict = {
        '{':'0',
        '|':'1',
        '}':'2',
        '~':'3',
        '':'4',
        'Ђ':'5',
        'Ѓ':'6',
        '‚':'7',
        'ѓ':'8',
        '„':'9'
    }
    for key in dict.keys():
       
        val = val.replace(key, str(dict[key]))

    return val

def dbf_to_csv(dbf_table_pth):#Input a dbf, output a csv, same name, same path, except extension
    csv_fn = dbf_table_pth[:-4]+ ".csv" #Set the csv file name
    table = DBF(dbf_table_pth, encoding="ISO-8859-1")# table variable is a DBF object
    with open(csv_fn, 'w', newline = '', encoding="ISO-8859-1") as f:# create a csv file, fill it with dbf content
        writer = csv.writer(f)
        writer.writerow(table.field_names)# write the column name
        for record in table:# write the rows
            l = list(record.values())
            #l[20] = decript(l[20])
            writer.writerow(l)
    return csv_fn# return the csv name

pastaLocal = 'D:/python/aih/data/ST'

datapath = 'D:\\python\\aih\\data\\ST\\'

for r, d, f in os.walk(pastaLocal):
    for filename in f:
            try:
                posicao = filename.find(".")
                filename_no_ext = filename[0:posicao]
                dbf = datapath + filename_no_ext + '.dbf'
                dbf_to_csv(dbf)
                     
            except AssertionError as error:
                print(error)       
