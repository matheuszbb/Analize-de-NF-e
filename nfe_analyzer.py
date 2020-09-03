import os #controle do sistema
# os.system("pip install pypdf4") ## caso nao tenha intalado
import PyPDF4 #leitura de pdf

 
print('> Iniciando...')
 
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
  dicionario[m] = conteudo[m]
 
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
    dicionario_pdf[add] = dicionario[cont+1].replace("\n","")
    dicionario_duplicado_pdf_verificador[add] = dicionario[cont+1].replace("\n","")
    dicionario_pdf_log[add] = dicionario[cont+1]
    log_pdf = open("C:/Users/mathe/Desktop/log_pdf.txt","a")
    log_pdf.write(dicionario_pdf_log[add])
    log_pdf.close()
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
    dicionario_aprovado[n_aprovada] = "99999999999999999999999999999999999999999999"
    n_aprovada = len(dicionario_aprovado.keys())
  print('> Adicionando Valores Extras Em NF-e APROVADA Para Funcionar O Cruzamento De Dados...')
  print('> Numeros De NF-e PDF:',n_pdf)
  print('> Numeros De NF-e APROVADA:',n_aprovada)
    
if (n_pdf < n_aprovada):
  print('> Numero De Pares Incompativel...')
  while(len(dicionario_aprovado.keys()) != len(dicionario_pdf.keys())):
    dicionario_pdf[n_pdf] = "88888888888888888888888888888888888888888888"
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
    if (dicionario_pdf[leitura_no_pdf] == "88888888888888888888888888888888888888888888"):
      erros = False
    else:
      print("> NF-e Do PDF Nao Encontrou O Arquivo XML Corespondente: ",dicionario_pdf[leitura_no_pdf]+"-nfe.XML")
      duplicado = True
 
if (duplicado == False):
  print("> Todas as NF-e No PDF Foram Encontradas Na Pasta Aprovada.xml!!!")
 
print("> Cruzando Valores do Aprovada.xml X PDF...")

cont = 0
dicionario_xml_erro = {}
duplicado = False 
for leitura_no_aprovado in range(0,len(dicionario_aprovado.keys())):
  erros = False
  for leitura_no_pdf in range(0,len(dicionario_pdf.keys())):
    if ((dicionario_aprovado[leitura_no_aprovado]) != (dicionario_pdf[leitura_no_pdf])):
      if ((leitura_no_pdf) == (len(dicionario_aprovado.keys())-1)):# se mesmo depois de vasculhar todo o pdf nao encontra um par
        erros = True                                               # correspondente ai sim pode declarar erro
    if ((dicionario_aprovado[leitura_no_aprovado]) == (dicionario_pdf[leitura_no_pdf])):
      erros = False
      break
  if (erros == True):
    if (dicionario_aprovado[leitura_no_aprovado] == "99999999999999999999999999999999999999999999"):
      erros = False
    else:  
      print("> NF-e Invalida Na Pasta Aprovadas: ",dicionario_aprovado[leitura_no_aprovado]+"-nfe.XML")
      duplicado = True
      dicionario_xml_erro[cont] = dicionario_aprovado[leitura_no_aprovado]+"-nfe.XML"
      cont = cont + 1 

if (duplicado == False):
  print("> Todas as NF-e Na Pasta Aprovada.xml Foram Encontradas No PDF!!!")
else:
  print("> Posso Deletar Os Arquivos.xml Que Nao Existem No PDF, Sim ou Nao?")
  op = ""
  feixar = False
  while feixar != True :
    op = input("> Minha Escolha: ")
    if ((op == "s")or(op == "n")or(op == "S")or(op == "N")or(op == "sim")or(op == "nao")):
      feixar = True
    else:
      print("Por Questoes De Seguranca Responda Exatamente ['s' ou 'n' ou 'S' ou 'N' ou 'sim' ou 'nao']")
  
  if ((op == "s")or(op == "S")or(op == "sim")):
    print("> Iniciando Processo De Exclusao...")

    print("> Iniciando Varedura Na Pasta Aprovada...")

    print("> Deletando Arquivos.xml Invalidos...")

    for x in range(0,len(dicionario_xml_erro.keys())):
      for xml in os.listdir("C:/Users/mathe/Desktop/Aprovada"):
        if (xml == dicionario_xml_erro[x]):
          os.remove("C:/Users/mathe/Desktop/Aprovada/" + xml)
          break
    print("> Arquivos.xml Invalidos Deletados Com Sucesso Da Pasta Aprovada !!!")

    print("> Gerando Log De XML Deletados...")

    log_xml_deletados = open("C:/Users/mathe/Desktop/log_xml_deletado.txt","w")
    log_xml_deletados.close()

    for i in range(0,len(dicionario_xml_erro.keys())):
      log_aprovado = open("C:/Users/mathe/Desktop/log_xml_deletado.txt","a")
      log_aprovado.write(dicionario_xml_erro[i]+"\n")
      log_aprovado.close()
  
  else:
    print("> Nenhum Arquivo.xml Foi Deletado!!!")

print("> Fim!!\n")

fim = input("Pressione Qualquer Tecla Para Fechar...")