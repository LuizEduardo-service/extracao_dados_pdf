# importa as bibliotecas necessárias
from pathlib import Path
import PyPDF2
import re
import pandas as pd
from tkinter.filedialog import askopenfiles
import os

def cria_pasta(dir_raiz: str, nome_pasta: str):

    novoDiretorio = dir_raiz + '\\' + nome_pasta # type: ignore

    if os.path.isdir(novoDiretorio):
        return novoDiretorio
    else:
        os.mkdir(novoDiretorio)
        return novoDiretorio  

def remover_arquivo(dir_download_file, nome_arquivo):
    """Remove os arquivos dentro da pasta"""
    listagem_arquivos = Path(dir_download_file)
    arquivos = listagem_arquivos.glob(pattern='*.*')

    for arquivo in arquivos:
        if nome_arquivo in str(arquivo):
            os.remove(arquivo)

dir_bd = cria_pasta(r'C:', 'extracao_pdf')
filetypes = (
            ('text files', '*.pdf'),
            ('All files', '*.*')
            )

lista_dir_final = askopenfiles(filetypes=filetypes)

if lista_dir_final:
        remover_arquivo(dir_bd, '.')
        for idx, pdf in enumerate(lista_dir_final):
            if '.pdf' in pdf.name:
                pdf_file = open(pdf.name , 'rb')

                #Faz a leitura usando a biblioteca
                read_pdf = PyPDF2.PdfFileReader(pdf_file)

                # pega o numero de páginas
                number_of_pages = read_pdf.getNumPages()

                #lê a primeira página completa
                page = read_pdf.getPage(0)

                #extrai apenas o texto
                page_content = page.extractText()

                # faz a junção das linhas 
                parsed = ''.join(page_content)

                # remove as quebras de linha
                parsed = re.sub('n', '', parsed)

                df = pd.DataFrame(list(parsed.split("\n")))
                df.columns = ['LISTAGEM']  # type: ignore
                df.to_csv(os.path.join(dir_bd,f'base_pdf_{idx}.csv'),sep=';',encoding='cp1252')
                print(str(os.path.join(dir_bd,f'base_pdf_{idx}.csv')))
