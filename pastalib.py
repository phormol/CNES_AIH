# encoding: utf-8
# pastalib
# funções para trabalhar com a biblioteca os (pastas e execucao de scripts externos)
# Hugo Rodrigues <hugonr@gmail.com>
import os.path # pastas
import shutil # para copia de arquivos

# --------------------------------------------------------------------
# verificaPasta
# verifica se existe uma pasta
# pastastring (string) nome da pasta
def verificaPasta(pastastring):
    return os.path.isdir(pastastring)
# --------------------------------------------------------------------
# criarPasta
# cria uma pasta
# pastastring (string) nome da pasta
def criarPasta(pastastring):
    return os.mkdir(pastastring)
# --------------------------------------------------------------------
# listaPastaAtual
# mostra o nome da pasta atual
def listaPastaAtual():
    return os.getcwd()
# --------------------------------------------------------------------
# executarScript
# executa o script da string
def executarScript(scriptString):
    return os.system(scriptString)
# --------------------------------------------------------------------
# listarArquivos
# lista os arquivos da pasta e extensao especificada nos parametros
# stringPasta string com a pasta onde estao os arquivos a serem listados
# stringExtensao string com a extensao a ser listada
def listarArquivos(stringPasta, stringExtensao = ".dbc"):
    items = os.listdir(stringPasta)
    arquivos = []
    for names in items:
        if names.endswith(stringExtensao):
            arquivos.append(names)
    return arquivos
# --------------------------------------------------------------------
# copiarArquivo
# copia um arquivo da fonte para o destino
# stringFonte string com o caminho e nome do arquivo a ser copiado
# stringDestino string com o destino do arquivo a ser copiado
def copiarArquivo(stringFonte, stringDestino):
    return shutil.copy(stringFonte, stringDestino)
# --------------------------------------------------------------------
# concatenaPastaArquivo
# concatena strings de pastas e arquivos
# stringPathA string com o caminho para concatenar
# stringPathB string com o caminho para concatenar
def concatenaPastaArquivo(stringPathA, stringPathB):
    return os.path.join(stringPathA, stringPathB)
    