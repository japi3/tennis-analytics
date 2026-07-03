import pandas as pd
df_atp=pd.read_csv('atp_schedule.csv')
df_wta=pd.read_csv('wta_schedule.csv')
df_atp=df_atp.dropna(subset=['prize_money'])
df_wta=df_wta.dropna(subset=['prize_money'])
print(df_atp['category'].value_counts())
print("---")
print(df_wta['category'].value_counts())
df_atp['prize_money_usd'] = df_atp['prize_money'].str.replace('$', '').str.replace(',', '').astype(int)
df_wta['prize_money_usd'] = df_wta['prize_money'].str.replace('$', '').str.replace(',', '').astype(int)
print(df_atp.groupby('category')['prize_money_usd'].mean())
print("---")
print(df_wta.groupby('category')['prize_money_usd'].mean())

atp_avg=df_atp.groupby('category')['prize_money_usd'].mean().reset_index()
atp_avg['tour']='ATP'
atp_avg['tier'] = atp_avg['category'].str.replace('ATP ', '')

wta_avg = df_wta.groupby('category')['prize_money_usd'].mean().reset_index()
wta_avg['tour'] = 'WTA'
wta_avg['tier'] = wta_avg['category'].str.replace('WTA ', '')

df_comparison = pd.concat([atp_avg, wta_avg], ignore_index=True)
print(df_comparison)
df_comparison.to_csv('prize_money_comparison.csv', index=False)
print("saved!")
df_t = pd.read_csv('tournaments.csv')
df_atp_t = df_t[df_t['tour'] == 'ATP'].dropna(subset=['prize_money_usd'])
df_wta_t = df_t[df_t['tour'] == 'WTA'].dropna(subset=['prize_money_usd'])

atp_avg=df_atp_t.groupby('tier')['prize_money_usd'].mean()
wta_avg=df_wta_t.groupby('tier')['prize_money_usd'].mean()
df_kpi=pd.DataFrame({
    'tier':atp_avg.index,
    'atp_avg':atp_avg.values,
    'wta_avg':wta_avg.values,
})
df_kpi['wta_pct_of_atp'] = (df_kpi['wta_avg'] / df_kpi['atp_avg'] * 100).round(1)
print(df_kpi)
df_kpi.to_csv('kpi_pay_gap.csv', index=False)
