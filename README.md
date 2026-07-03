# Tennis Prize Money & Rankings Analysis | 2025

A portfolio project analyzing prize money equity, tournament distribution, and player earnings across the ATP and WTA tours using original data collected via web scraping.

## Business Questions

1. **How large is the prize money gap between ATP and WTA across tournament tiers?**
2. **Which surfaces and tournament categories offer the highest prize pools?**
3. **Where are professional tennis tournaments concentrated geographically?**
4. **Does ranking predict earnings, and how do top ATP vs WTA earners compare?**

## Key Findings

- **Grand Slams** are nearly equal: WTA earns **95.8%** of ATP prize money
- The gap widens dramatically at smaller tiers — WTA earns only **35.8%** of ATP at the 250 level and **37.5%** at the 500 level
- **Clay** courts host the highest average prize pools; Hard courts are the most common surface
- **Europe** dominates tournament geography, with North America hosting the biggest prize events
- **Carlos Alcaraz** and **Aryna Sabalenka** are the top earners on each tour in 2025; top-ranked players generally earn more but several lower-ranked players outperform expectations

## Dashboards

### Dashboard 1 — Tennis Prize Money Analysis
![Tennis Prize Money Analysis](dashboards/dashboard1_prize_money.png)

- ATP vs WTA prize money comparison by tournament tier (250 / 500 / 1000 / Grand Slam)
- Average prize money by surface (Clay, Grass, Hard)
- Pay parity chart: WTA earnings as % of ATP per tier

### Dashboard 2 — Tournament Landscape
![Tournament Landscape](dashboards/dashboard2_tournament_landscape.png)

- Treemap of all 111 tournaments sized by prize money
- Top 15 tournaments by average prize pool (ATP + WTA side-by-side)
- World map of tournament locations

### Dashboard 3 — Player Earnings & Rankings
![Player Earnings & Rankings](dashboards/dashboard3_player_earnings.png)

- Scatter plot: Ranking vs. Total Earnings (top 10 ATP + WTA)
- Horizontal bar chart: Top 10 earners across both tours

## Data Sources

| Dataset | Source | Method |
|---|---|---|
| ATP Rankings (150 players) | ESPN | BeautifulSoup + requests |
| WTA Rankings (150 players) | ESPN | BeautifulSoup + requests |
| ATP Tournament Schedule | Wikipedia (2025 ATP Tour) | pandas read_html |
| WTA Tournament Schedule | Wikipedia (2025 WTA Tour) | pandas read_html |
| Player Earnings | WTA / ATP official sites | Manual collection |

## Tech Stack

- **Python** — requests, BeautifulSoup, pandas, re
- **Data collection** — Web scraping (ESPN, Wikipedia)
- **Analysis** — pandas groupby, currency normalization (EUR/GBP/AUD → USD)
- **Visualization** — Tableau (3 dashboards)

## Files

```
tennis_analytics/
├── scraping.py          # Web scraping — ESPN rankings + Wikipedia schedules
├── analysis.py          # Prize money comparison + KPI calculation
├── atp_rankings.csv     # 150 ATP players (rank, points, tournaments played)
├── wta_rankings.csv     # 150 WTA players
├── tournaments.csv      # 60 unique tournaments with prize money + surface
├── prize_money_comparison.csv  # Avg prize by tier + tour
├── kpi_pay_gap.csv      # WTA % of ATP per tier
├── player_earnings.csv  # Top 10 earners ATP + WTA
└── dashboards/          # Dashboard screenshots
```
