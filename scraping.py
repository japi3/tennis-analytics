import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import re


# --- ATP Rankings ---
url = "https://www.espn.com/tennis/rankings"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, 'lxml')
rows = soup.find('table').find_all('tr')
players = []
for row in rows[1:]:
    tds = row.find_all('td')
    players.append({
        'rank': tds[0].get_text(strip=True),
        'player': tds[2].get_text(strip=True),
        'points': tds[3].get_text(strip=True),
        'tournaments': tds[4].get_text(strip=True)
    })
df_atp = pd.DataFrame(players)
df_atp['points'] = df_atp['points'].str.replace(',', '').astype(int)
df_atp['rank'] = df_atp['rank'].astype(int)
df_atp['tournaments'] = df_atp['tournaments'].astype(int)
df_atp.to_csv('atp_rankings.csv', index=False)
print(f"ATP rankings saved: {df_atp.shape}")


# --- WTA Rankings ---
url = "https://www.espn.com/tennis/rankings/_/type/wta"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, 'lxml')
rows = soup.find('table').find_all('tr')
players = []
for row in rows[1:]:
    tds = row.find_all('td')
    players.append({
        'rank': tds[0].get_text(strip=True),
        'player': tds[2].get_text(strip=True),
        'points': tds[3].get_text(strip=True),
        'tournaments': tds[4].get_text(strip=True)
    })
df_wta = pd.DataFrame(players)
df_wta['points'] = df_wta['points'].str.replace(',', '').astype(int)
df_wta['rank'] = df_wta['rank'].astype(int)
df_wta['tournaments'] = df_wta['tournaments'].astype(int)
df_wta.to_csv('wta_rankings.csv', index=False)
print(f"WTA rankings saved: {df_wta.shape}")


def extract_schedule(tables, label):
    frames = []
    for t in tables:
        cols = t.columns.tolist()
        if 'Tournament' in cols and 'Week' in cols:
            frames.append(t)
    if not frames:
        print(f"No schedule tables found for {label}")
        return None
    df = pd.concat(frames, ignore_index=True)
    df['category'] = df['Tournament'].apply(
        lambda x: re.search(r'ATP \d+|WTA \d+|Grand Slam', str(x))
    )
    df['category'] = df['category'].apply(lambda m: m.group() if m else None)
    df['prize_money'] = df['Tournament'].apply(
        lambda x: re.search(r'\$[\d,]+', str(x))
    )
    df['prize_money'] = df['prize_money'].apply(lambda m: m.group() if m else None)
    df = df.dropna(subset=['category'])
    return df


# --- ATP Schedule ---
response = requests.get("https://en.wikipedia.org/wiki/2025_ATP_Tour",
                        headers={'User-Agent': 'Mozilla/5.0'})
atp_tables = pd.read_html(io.StringIO(response.text))
df_atp_schedule = extract_schedule(atp_tables, 'ATP')
df_atp_schedule.to_csv('atp_schedule.csv', index=False)
print(f"ATP schedule saved: {df_atp_schedule.shape}")


# --- WTA Schedule ---
response = requests.get("https://en.wikipedia.org/wiki/2025_WTA_Tour",
                        headers={'User-Agent': 'Mozilla/5.0'})
wta_tables = pd.read_html(io.StringIO(response.text))
df_wta_schedule = extract_schedule(wta_tables, 'WTA')
df_wta_schedule.to_csv('wta_schedule.csv', index=False)
print(f"WTA schedule saved: {df_wta_schedule.shape}")
