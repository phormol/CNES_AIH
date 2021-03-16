import ftppessoal
import os.path
import os

conexaoftp = ftppessoal.conectarFTP('anonymous', 'guest', 'ftp.datasus.gov.br', 21)
ftppessoal.irParaPasta(conexaoftp, '/dissemin/publicos/CNES/200508_/Dados/PF')
arquivos = ftppessoal.listarArquivos(conexaoftp)
conexaoftp.close

pastaLocal = 'D:/python/aih/data/PF'

for f in list(arquivos):
    try:
        nomeArquivo = None
        if "." in f:
            posicao = f.find(".")
            nomeArquivo = f[0:posicao]

            if nomeArquivo[:6] == 'PFBA20':

                if os.path.exists(pastaLocal + '/' + nomeArquivo + '.dbc'):
                    a = 1
                else:    
                    arq = nomeArquivo + '.dbc'
                    print("*** baixando arquivo " + arq)
                    conexaoftp = ftppessoal.conectarFTP('anonymous', 'guest', 'ftp.datasus.gov.br', 21)
                    ftppessoal.irParaPasta(conexaoftp, '/dissemin/publicos/CNES/200508_/Dados/PF')
                    ftppessoal.downloadArquivo(conexaoftp, arq, pastaLocal)
                    conexaoftp.close
        else:
            nomeArquivo = f
    except:
        try:
            print("*** removendo arquivo " + arq)
            os.remove(arq)
        except:
            a = 1    
                    








