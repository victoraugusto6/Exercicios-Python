from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = '/home/victor/Documentos/Python - Projects/Curso em Vídeo/Exercises-Python/Programas/Mundo 3/modulos/Ex0115/arquivo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas',
                     'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        exit(0)
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
