# encoding: utf-8
# ftppessoal
# funcoes para o ftp
# Hugo Rodrigues <hugonr@gmail.com>
from ftplib import FTP
import logging
import socket

# --------------------------------------------------------------------
# conexao com o servidor
# usuario (string) usuario para conexao
# senha (string) senha para conexao
# ip (string) endereco ftp para conexao
# porta (integer) porta para conexao
def conectarFTP(usuario=' ', senha=' ', ip='127.0.0.10', porta=2121):

    try:
        handler = FTP()
        handler.connect(ip, porta)
        handler.login(usuario, senha)
        
    except Exception:
        logging.critical('Nao foi possivel conectar ao servidor FTP')

    return handler

# --------------------------------------------------------------------
# ir para a pasta especificada no ftp
# handler (FTP.connect) variavel conexao ftp 
# Pasta (string) pasta a ser acessada 
def irParaPasta(handler, Pasta):

    try:
        handler.cwd(Pasta)
    except Exception:
        print('Nao foi possivel acessar o diretorio ou o diretorio nao existe')
# --------------------------------------------------------------------
# A função lista arquivos da pasta atual
# handler (FTP.connect) variavel conexao ftp 
# return files (line.rsplit) lista de arquivos com extensao
def listarArquivos(handler):
    log = []
    handler.retrlines('LIST', callback=log.append)
    files = (line.rsplit(None, 1)[1] for line in log)
    return files
# --------------------------------------------------------------------
# downloadArquivo
# fazer download do arquivo especificado do ftp
# handler (FTP.connect) variavel conexao ftp 
# arquivoString (string) nome do arquivo
def downloadArquivo(handler, arquivoString, pastaString):
    arquivoDownload = pastaString + '\\\\' + arquivoString
    # tratando erro do download
    retornoErro = "sem erro"
    try:
        handler.retrbinary("RETR "+arquivoString, open(arquivoDownload,"wb").write)
        return "sem erro"
    except (error_reply, error_perm, error_temp):
        return "com erro"
    except socket.gaierror as e:
        if e.errno != 10054:
            return "com erro reconectar"
        return "com erro"
    


