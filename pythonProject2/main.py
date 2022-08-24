per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input("Введите сумму:"))
deposit_1=money*(per_cent.get("ТКБ")/100)
deposit_2=money*(per_cent.get("СКБ")/100)
deposit_3=money*(per_cent.get("ВТБ")/100)
deposit_4=money*(per_cent.get("СБЕР")/100)
deposit=[round(deposit_1), round(deposit_2),round(deposit_3), round(deposit_4)]
print(deposit)
print("Максимальная сумма, которую вы можете заработать",max(deposit))
