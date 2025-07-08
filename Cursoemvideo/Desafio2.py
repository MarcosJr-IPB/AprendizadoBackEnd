dia = input("Qual é o dia do seu nascimento?")
Mês = input("Qual é o mês do seu nascimento?")
ano = input("qual é o ano do seu nascimento?")
if Mês == "01":
    Mês = "Janeiro"
elif Mês == "02":
    Mês = "Fevereiro"
elif Mês == "03":
    Mês = "Março"
elif Mês == "04":
    Mês = "Abril"
elif Mês == "05":
    Mês = "Maio"
elif Mês == "06":
    Mês = "Junho"
elif Mês == "07":
    Mês = "Julho"
elif Mês == "08":
    Mês = "Agosto"
elif Mês == "09":
    Mês = "Setembro"
elif Mês == "10":
    Mês = "Outubro"
elif Mês == "11":
    Mês = "Novembro"
elif Mês == "12":
    Mês = "Dezembro"
else:
    Mês = "Mês inválido"
print("Você nasceu no dia", dia, "de", Mês, "do ano de", ano, ".")
