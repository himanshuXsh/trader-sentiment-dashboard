# Trader Performance vs Market Sentiment Analysis

## Objective

This project analyzes how Bitcoin market sentiment (Fear vs Greed) influences trader behavior and performance.

The goal is to identify patterns that could help design better trading strategies.

---

## Dataset

Two datasets were used:

1. Bitcoin Market Sentiment
   - Date
   - Sentiment classification (Fear / Greed)

2. Historical Trader Data
   - Account
   - Trade size
   - Direction
   - Timestamp
   - Closed PnL

---

## Methodology

The analysis followed these steps:

1. Data preparation
   - Loaded both datasets
   - Checked missing values and duplicates
   - Converted timestamps
   - Merged datasets on daily date

2. Feature engineering
   - Daily PnL per trader
   - Win rate
   - Average trade size
   - Trades per day
   - Long vs Short ratio

3. Exploratory analysis
   - PnL distribution by sentiment
   - Trade frequency patterns
   - Trader segmentation

---

## Key Insights

1. Greed sentiment periods show higher trading activity.
2. Traders tend to take more long positions during Greed markets.
3. Frequent traders exhibit larger PnL volatility compared to infrequent traders.

---

## Strategy Recommendations

1. During Fear periods traders may reduce position size and trade frequency to manage risk.

2. During Greed periods momentum strategies may perform better but should be combined with risk controls.

---

## Dashboard

A lightweight Streamlit dashboard was built to explore the analysis results interactively.

Features include:

- PnL distribution visualization
- Trade direction analysis
- Trading activity trends
- Trader segmentation insights

---

## Setup Instructions

Install dependencies:
