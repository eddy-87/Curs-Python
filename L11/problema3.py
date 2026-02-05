import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

plt.style.use('ggplot')
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
            'pret_unitar': round(pret_final, 2),
            'cantitate': cantitate,
            'promo': is_promo,
            'total_vanzare': round(total_vanzare, 2),
            'profit': round(profit, 2)
        })

df_sim = pd.DataFrame(date_simulare)
df_daily = df_sim.groupby('zi')[['total_vanzare', 'profit']].sum().reset_index()

plt.figure(figsize=(12, 5))
plt.plot(df_daily['zi'], df_daily['total_vanzare'], label='Venit Total', color='blue', marker='o')
plt.plot(df_daily['zi'], df_daily['profit'], label='Profit Total', color='green', linestyle='--')
plt.title('Evolutia Veniturilor si a Profitului')
plt.xlabel('Ziua')
plt.ylabel('Valoare')
plt.legend()
plt.show()

fig, ax = plt.subplots(1, 2, figsize=(14, 5))
ax[0].hist(df_sim['pret_unitar'], bins=20, color='orange', edgecolor='black')
ax[0].set_title('Distributia Preturilor')
ax[1].hist(df_sim['cantitate'], bins=10, color='purple', edgecolor='black', alpha=0.7)
ax[1].set_title('Distributia Cantitatilor')
plt.show()

promo_data = df_sim[df_sim['promo'] == True]['pret_unitar']
no_promo_data = df_sim[df_sim['promo'] == False]['pret_unitar']

plt.figure(figsize=(8, 5))
plt.boxplot([no_promo_data, promo_data], labels=['Fara Promotie', 'Cu Promotie'])
plt.title('Impact Promotii')
plt.ylabel('Pret Unitar')
plt.show()