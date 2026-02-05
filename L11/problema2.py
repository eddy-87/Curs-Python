import pandas as pd
import numpy as np
import datetime

np.random.seed(42)
zile = 60
date_simulare = []
start_date_sim = datetime.date(2024, 1, 1)

for zi in range(zile):
    current_date = start_date_sim + datetime.timedelta(days=zi)
    nr_produse_azi = np.random.randint(5, 16)

    for _ in range(nr_produse_azi):
        pret_baza = np.random.normal(40, 8)
        cantitate = np.random.randint(1, 11)
        is_promo = np.random.rand() < 0.30

        if is_promo:
            pret_final = pret_baza * 0.8
        else:
            pret_final = pret_baza

        total_vanzare = pret_final * cantitate
        profit = total_vanzare * 0.30

        date_simulare.append({
            'zi': zi + 1,
            'data': current_date,
            'pret_unitar': round(pret_final, 2),
            'cantitate': cantitate,
            'promo': is_promo,
            'total_vanzare': round(total_vanzare, 2),
            'profit': round(profit, 2)
        })

df_sim = pd.DataFrame(date_simulare)

print("Statistici generale:")
print(df_sim[['pret_unitar', 'cantitate', 'profit']].agg(['mean', 'max', 'min']))

total_vanzari = df_sim['total_vanzare'].sum()
total_profit = df_sim['profit'].sum()

print(f"\nTotal Vanzari: {total_vanzari:.2f}")
print(f"Total Profit: {total_profit:.2f}")