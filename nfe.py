import os #controle do sistema

for i in os.listdir("C:/Users/mathe/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0/LocalCache/local-packages/Python38/site-packages"):
  if (i == "PyPDF4"):
    PyPDF4_ja_instalado = True

if (PyPDF4_ja_instalado == True):
  import PyPDF4 #leitura de pdf
else:
  os.system("pip install pypdf4")
  import PyPDF4 #leitura de pdf

 
print('> Iniciano...')
 
arquivo = open("C:/Users/mathe/Desktop/RelLivroFiscalSaidaNFCe.pdf", "rb")
 
linha = PyPDF4.PdfFileReader(arquivo)
numero_de_paginas = linha.getNumPages()
conteudo = ""
 
for n in range(0,numero_de_paginas):
  pagina = linha.getPage(n)
  pdf = pagina.extractText()
  conteudo = conteudo + pdf
 
print('> Conteudo PDF Lido Com Sucesso !!!')
 
arquivotxt = open("C:/Users/mathe/Desktop/RelLivroFiscalSaidaNFCe.txt","w")
arquivotxt.write(conteudo)
arquivotxt.close()
 
print('> Conteudo PDF Convertido em TXT !!!')
 
arquivo = open("C:/Users/mathe/Desktop/RelLivroFiscalSaidaNFCe.txt","r")
 
conteudo = arquivo.readlines()
 
dicionario = {}
 
print('> Procurando Codigos NF-e...')
 
for m in range(0,len(conteudo)):
  k = 'linha ' + str(m) +':'
  dicionario[k] = conteudo[m]
 
print('> Conteudo Encontrado...') 
 
log_pdf = open("C:/Users/mathe/Desktop/log_pdf.txt","w")
log_pdf.close()
 
dicionario_duplicado_pdf_verificador = {}
dicionario_pdf_log = {}
dicionario_pdf = {}
cont = 0
add = 0
for j in dicionario.values():
  if (j == "Id NFC-e:\n"):
    k = 'linha ' + str(cont+1) +':'
    dicionario_pdf[add] = dicionario[k].replace("\n","")
    dicionario_duplicado_pdf_verificador[add] = dicionario[k].replace("\n","")
    dicionario_pdf_log[add] = dicionario[k]
    log_pdf = open("C:/Users/mathe/Desktop/log_pdf.txt","a")
    log_pdf.write(dicionario_pdf_log[add])
    log_pdf.close()
    #print("estou na linha",cont+2,":",dicionario[k])
    cont = cont + 1
    add = add + 1
  else:
    cont = cont + 1
 
print('> Log PDF.txt Gerado...')
 
print('> Vasculhando Diretorio Aprovada...')
 
log_pdf = open("C:/Users/mathe/Desktop/log_aprovado.txt","w")
log_pdf.close()
 
dicionario_aprovado_log = {}
dicionario_aprovado = {}
cont = 0
for i in os.listdir("C:/Users/mathe/Desktop/Aprovada"):
    dicionario_aprovado_log[cont] = i.replace("-nfe.XML","") + "\n"
    dicionario_aprovado[cont] = i.replace("-nfe.XML","")
    log_aprovado = open("C:/Users/mathe/Desktop/log_aprovado.txt","a")
    log_aprovado.write(dicionario_aprovado_log[cont])
    log_aprovado.close()
    cont = cont + 1

print('> Log Aprovado.txt Gerado...')
 
print('> Conteudo Encontrado...')
 
print('> Iniciando Cruzamento De Dados...\n')
 
n_pdf = len(dicionario_pdf.keys())
n_aprovada = len(dicionario_aprovado.keys())
 
print('> Numeros De NF-e PDF:',n_pdf)
print('> Numeros De NF-e APROVADA:',n_aprovada)
 
if (len(dicionario_pdf.keys()) == len(dicionario_aprovado.keys())):
  print('> Numero De Pares Compativel...')
 
if (n_pdf > n_aprovada):
  print('> Numero De Pares Incompativel...')
  while(len(dicionario_pdf.keys()) != len(dicionario_aprovado.keys())):
    dicionario_aprovado[n_aprovada] = 99999999999999999999999999999999999999999999
    n_aprovada = len(dicionario_aprovado.keys())
  print('> Adicionando Valores Extras Em NF-e APROVADA Para Funcionar O Cruzamento De Dados...')
  print('> Numeros De NF-e PDF:',n_pdf)
  print('> Numeros De NF-e APROVADA:',n_aprovada)
    
if (n_pdf < n_aprovada):
  print('> Numero De Pares Incompativel...')
  while(len(dicionario_aprovado.keys()) != len(dicionario_pdf.keys())):
    dicionario_pdf[n_pdf] = 88888888888888888888888888888888888888888888
    n_pdf = len(dicionario_pdf.keys())
  print('> Adicionando Valores Extras Em NF-e PDF Para Funcionar O Cruzamento De Dados...')
  print('> Numeros De NF-e PDF:',n_pdf)
  print('> Numeros De NF-e APROVADA:',n_aprovada)
 
print("\n> Verificando Duplicidade No PDF...")
 
duplicado = False
for verifica_pdf in range(0,len(dicionario_pdf.keys())):
  erros = 0
  for verifica_pdf_log in range(0,len(dicionario_duplicado_pdf_verificador.keys())):
    if ((dicionario_pdf[verifica_pdf]) == (dicionario_duplicado_pdf_verificador[verifica_pdf_log])):
      erros = erros + 1
  if (erros >= 2):
    print("> NF-e Encontrada No PDF Esta Duplicada: ",dicionario_pdf[verifica_pdf])
    duplicado = True
 
if (duplicado == False):
  print("> Nao Foi Encontrada Nenhuma NF-e Duplicada No PDF...")
 
print("> Cruzando Valores do PDF X Aprovada.xml...")

duplicado = False
for leitura_no_pdf in range(0,len(dicionario_pdf.keys())):
  erros = False
  for leitura_no_aprovado in range(0,len(dicionario_aprovado.keys())):
    if ((dicionario_pdf[leitura_no_pdf]) != (dicionario_aprovado[leitura_no_aprovado])):
      erros = True
    if ((dicionario_pdf[leitura_no_pdf]) == (dicionario_aprovado[leitura_no_aprovado])):
      erros = False
      break
  if (erros  == True):
    if (dicionario_pdf[leitura_no_pdf] == 88888888888888888888888888888888888888888888):
        1#esse 1  e so para a maquina nao buga
    else:
      print("> NF-e Do PDF Nao Encontrou O Arquivo XML Corespondente: ",dicionario_pdf[leitura_no_pdf]+"-nfe.XML")
      duplicado = True
 
if (duplicado == False):
  print("> Todas as NF-e No PDF Foram Encontradas Na Pasta Aprovada.xml!!!")
 
print("> Cruzando Valores do Aprovada.xml X PDF...")

duplicado = False 
for leitura_no_aprovado in range(0,len(dicionario_aprovado.keys())):
  erros = False
  for leitura_no_pdf in range(0,len(dicionario_pdf.keys())):
    if ((dicionario_aprovado[leitura_no_aprovado]) != (dicionario_pdf[leitura_no_pdf])):
      if ((leitura_no_pdf) == (len(dicionario_aprovado.keys())-1)):# se mesmo de pois de vasculhar todo o pdf nao encontra um par
        erros = True                                               # correspondente ai sim pode declarar erro
    if ((dicionario_aprovado[leitura_no_aprovado]) == (dicionario_pdf[leitura_no_pdf])):
      erros = False
      break
    if (erros == True):
      if (dicionario_aprovado[leitura_no_aprovado] == 99999999999999999999999999999999999999999999):
        1#esse 1  e so para a maquina nao buga
      else:  
        print("> NF-e Invalida Na Pasta Aprovadas: ",dicionario_aprovado[leitura_no_aprovado])
        duplicado = True

if (duplicado == False):
  print("> Todas as NF-e Na Pasta Aprovada.xml Foram Encontradas No PDF!!!")

print("> Fim!!")