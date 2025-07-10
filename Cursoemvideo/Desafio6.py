print('Vamos fazer uma liste afazeres domésticos?')
lista1 = []
while True:
    tarefa = input('Digite a tarefa (ou "sair" para finalizar):')
    if (tarefa.lower() == 'sair'):
        break
    lista1.append(tarefa)
print('Lista de afazeres domésticos:')
for i, tarefa in enumerate(lista1, start=1):
    print(f'{i}.{tarefa}')
print('Obrigado por usar a Lista de Afazeres Domésticos!')
print('Tenha um ótimo dia!')
