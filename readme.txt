# Analize-de-NF-e

Esse progama tem como intuito ajudar o setor fiscal

1:  Inicialmente tive bastante dificuldade para encontrar conteudo que abordava a leitura de pdf. Resposta = { 
    import os #controle do sistema
    os.system("pip install pypdf4") ## caso nao tenha instalado
    import PyPDF4 #leitura de pdf
    }
2:  Depois a dificuldade foi como fazer o scraping do pdf afinal como eu iria achar qual linha que estariao os codigos das NF-e?
3:  Bem a resposta foi encontrada quando convertir tudo que o robo leu do pdf para txt assim percebi que antes do codigo sempre tem " Id NFC-e: "
    entao pensei ja que peguei uma montueira dados e cada dado foi escrito em uma linha diferente, vou encontrar a penas as linhas que tem " Id NFC-e: "
    e vou adicionar em um dicionario a linha posterior, pois a linha posterior sempre era o codigo.
4:  Como ler os arquivos que tem em uma pasta ?
5:  Bem inicialmente eu nao sabia entao foi pesquisar no google. Resposta = for i in os.listdir("endereco do diretorio")
6:  Agora devo cruzar os dados 
7:  entao fiz o primeiro cruzamento de dados inicialmente fiz alguns testes aleatorios... sabe coisas bestas so enquanto nao formava o algoritmo na cabeca
    me surpreendi com o resultado, pois o robo encontrou dois codigos NF-e duplicados no pdf, fui la verificar e para minha surpresa realmente esatvao duplicados.
    Entao fiz essa implementacao no algoritimo.
8:  Peguiei o dicionario com os codigos NF-e extarido do txt e repliqei em outro dicionario. Enatao pus eles para se cruzarem caso achase seu par eu adiconava +1
    ao contador, caso o contador fosse > 2 isso significava que a NF-e estava duplicada. Entao e printado na tela seu codigo.
9:  Em meu projeto inicial percebi que muitas vezes o numero total de NF-e do txt nao batia com o numero total de arquivos.xml e isso causava um bug chato
    na hora de cruzar os dados eu uso um for dentro de outro for entao enquanto um ia de 0 ate 100 o outro ia de 0 ate 99 a primeira vista isso nao parece que mude nada,
    mas o robo relatava que estava dando erro e realmente o numero de pares deveria ser igual. Pois quando o primeiro for era 99 e o segundo deveria ser 99 tambem para
    comparar de forma exata faltava 1 codigo NF-e. Resposta = criei uma condicional que acrescenta um certo valor a mais no dicionario_txt e no dicionario_xml.
10: Bem nesse momento peguei o dicionario_txt e comparei com o dicionario_xml, assim pego um codigo NF-e do txt e comparo com todos o outro codigos do xml. Caso a pesquisa
    Encontra-se o par correspondente parava a pesquisa e ia para a poxima pois assim gasta menos prossecamento de dados, mas caso nao encontra-se o par bem, imprimia na tela
    a NF-e do txt que nao foi encontrada.
11: Nessa hora eu so via o terminal lagando de tanto dado que ele me retornava, pois o robo estava fazendo exatamente oque pedi me mostardo sempre que um resulatdo fosse 
    imcompativel. Resposta = criei uma condicional que antes de imprimir na tela o segundo laco for deveria ser finalizado e se caso ate la nao tivesse achado o par ai sim
    poderia imprimir o codigo NF-e do txt que nao foi encontrado.
12: Bem nesse momento eu devria validar se a pasta Aprovadas continha apenas os codigos NF-e que realmente foram aprovados. Resposta = peguei todo o dicionario_xml
    e cruzei os dados com o dicionario_txt, basicamente inverti a pesquisa anterio.
13: E so pensar em uma lista de pessoas que entrarao em um hotel na lista consta que entrou 5 pessoas, mas nas cameras claramente consta 6 ou seja temos que pegar todas
    as 5 e acrecentar " x " como uma 6 pessoa na lista assim nos cruzamos de igual para igual e a pesoa que nao aparecer na lista e porque entrou de forma incorreta. Pensado
    assim cruzei os dados e o resultado imprimi na tela e e aproveitei para criar um dicionario_deletados que contem os arquivos que devem ser deletados.
14: Claramente o robo nao pode ter esse poder entao pus na mao do usuraio responder sim ou nao, respostas diferentes disso ocasionam em um loop com a mesma pergunta
    e uma questao de seguranca vai que a pessoa presiona uma tecla por engano e deleta os arquivos, apesar de que eles devem ser realmente deletado, voce tem que se por no 
    lugar de alguem que nao conhece seu programa esse pessoa ainda esta validando se realmente funciona, ela tem que verificar com seus prorios olhos. Resposta = Pensando 
    dessa forma criei um arquivo_log.txt com cada dado encontrado, tanto para arquivos que foram transcritos em txt como para arquivos que foram deletados ou os que nao foram,
    mas deviam ter sido deletados.
15: Depois de criar isso tudo foi que percibi a pessoa ia ter que ficar re abrendo o programa toda vez que fosse fazer uma nova analize , isso nao fazia sentido entao adicionei
    um loop com wile, assim a pessoa pode fazer uma nova pesquisa repetidas vezes abrindo o robo uma unica vez.
16: Muitas vezes fazemos coisas em nosso pc e esquecemos que esses progams devem funcionar no nosso, codificamos para que funcione exclusivamente nosso pc, e quando 
    vamos testar em outro pc notamos que tem coisa errada. Resposta =  {
    import os
    getUser = lambda: os.environ["USERNAME"] if "C:" in os.getcwd() else os.environ["USER"]
    usuario_pc = getUser()
    } dessa forma obtemos o nome do usuario atual do pc e podemos pesquisar os arquivos sem erros.
17: Muitas vezes criamos um progama e esquecemos que a maior parte das pessoas que vao ultilisar sao leigos, e isso pode ser um grande problema para eles, portanto temos que 
    criar mais dificuldade para nos e menos para eles. Resposta = {
    import os
    os.system("pip install auto-py-to-exe")
    os.system("python -m auto_py_to_exe")
    }assim criamos um arquivo.exe
18: Detalhes fazem a diferenca use o Inno Setup Compiler para criar um instalador 
19: Infelismente a microsoft nao ajuda devs que nao fazem parte dos seus negocio e estao certas pois muitos ja se aprovitar para criar programas maliciosos que estragam 
    toda a inteface e do widowns, nao tem como negar que eles estao certos em negar o acesso e tratar como virus qual quer programa que nao tenha um certificado emitido 
    por eles, para resolver isso baixe o programa pelo EDGE e quando chegar o alerta de erro escolha a opcao manter arquivo e relate como falso positivo.
20: Caso queira por um codigo de versionamento em seu programa criado em python. Resposta = basta copiar meu arquivo vercionamento.txt e fazer as devidas auteracoes.
21: Caso clik no programa e ele nao abra, ponha ele em um diretorio separado tipo D:/ ou diretamente no C:/ e clik que vai funcionar.
22: O mais importante, aproveite seus projetos se desenvolva, divirta-se, nao fique com medo de inovar acresentando mais futures achando que vai dar mais trabalho. Por fim
    Mesmo que pareca impossivel que sua mente esteja a ponto de explodir durma um pouco, coma alguma coisa, se foque por alguns instantes em outra coisa sem perder o foco 
    no projeto principal claro e se mesmo assim nao achar a resposta bem voce provavelmente esta encarando o problema da forma errada.
    
