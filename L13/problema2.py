import pandas as pd

data = {
    'Produs': ['Lapte', 'Paine', 'Oua'],
    'Cantitate': [2, 5, 10],
    'Pret unitar': [4.5, 2.0, 0.5]
}
df = pd.DataFrame(data)
df.to_csv('comenzi_input.csv', index=False)

df_procesat = pd.read_csv('comenzi_input.csv')
df_procesat['Valoare Totala'] = df_procesat['Cantitate'] * df_procesat['Pret unitar']

df_procesat.to_csv('comenzi_output.csv', index=False)

print("Date procesate:")
print(df_procesat)