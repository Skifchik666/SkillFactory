money=input("Введите количество денег")
money=float(money)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
dep=[per_cent.get('ТКБ')*(money/100),per_cent.get('СКБ')*(money/100),per_cent.get('ВТБ')*(money/100),per_cent.get('СБЕР')*(money/100)]
tkb=round(dep[0],2)
skb=round(dep[1],2)
vtb=round(dep[2],2)
sber=round(dep[3],2)
deposit=[tkb,skb,vtb,sber]
max=max(deposit)
print("ТКБ=",tkb)
print("СКБ=",skb)
print("ВТБ=",vtb)
print("СКБ=",skb)
print("СБЕР=",sber)
print("Максимальная сумма, которую вы можете заработать=",max)