import pandas as pd

data_dummy = {
    'produs': ['Laptop', 'Mouse', 'Tastatura', 'Laptop', 'Monitor', 'Mouse', 'Monitor'],
    'cantitate_vanduta': [1, 5, 2, 1, 2, 3, 1],
    'pret': [3000, 50, 150, 3200, 800, 50, 850],
    'data_vanzarii': ['2024-01-15', '2024-01-20', '2024-02-10', '2024-02-15', '2024-03-05', '2024-03-10', '2024-03-12']
}
df_dummy = pd.DataFrame(data_dummy)
df_dummy.to_csv('vanzari.csv', index=False)

df = pd.read_csv('vanzari.csv')
df['data_vanzarii'] = pd.to_datetime(df['data_vanzarii'])
df['venit_total'] = df['cantitate_vanduta'] * df['pret']
df['luna'] = df['data_vanzarii'].dt.to_period('M')

print("1. Cele mai vandute produse pe luna:")
print(df.groupby(['luna', 'produs'])['cantitate_vanduta'].sum().sort_values(ascending=False))

print("\n2. Venitul total pe fiecare produs:")
print(df.groupby('produs')['venit_total'].sum())

start_date = '2024-01-01'
end_date = '2024-03-31'
df_filtrat = df[(df['data_vanzarii'] >= start_date) & (df['data_vanzarii'] <= end_date)]
print(f"\n3. Numar tranzactii in interval: {len(df_filtrat)}")

venit_lunar = df.groupby('luna')['venit_total'].sum().mean()
print(f"\n4. Venitul mediu lunar: {venit_lunar}")