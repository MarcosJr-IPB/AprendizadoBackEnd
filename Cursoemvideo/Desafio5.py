print('Bem-vindo à lista de compras!')
lista = []
while True:
    item = input('Digite o nome do item (ou "sair" para finalizar): ')
    if (item.lower() == 'sair'):
        break
    lista.append(item)
print('Lista de compras:')
for i, item in enumerate(lista, start=1):
    print(f'{i}. {item}')
print('Obrigado por usar a lista de compras!')