import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import os

    return os, pd


@app.cell
def _(pd):
    df = pd.read_csv('data/raw/events.csv')
    return (df,)


@app.cell
def _(df):
    dfna = df.replace(r'^\s*$', float('nan'), regex=True).dropna()
    return (dfna,)


@app.cell
def _(dfna):
    df_valid_events = dfna[dfna['event_type'].isin(['click', 'login', 'scroll', 'view', 'purchase'])]
    return (df_valid_events,)


@app.cell
def _(df_valid_events):
    df_valid_times = df_valid_events[df_valid_events['duration_seconds'] > 0].copy()
    df_valid_times['duration_seconds'] = df_valid_times['duration_seconds'].astype(int)
    return (df_valid_times,)


@app.cell
def _(df_valid_times, pd):
    df_valid_times['timestamp'] = pd.to_datetime(df_valid_times['timestamp'], format='mixed')

    df_valid_times['timestamp'] = df_valid_times['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')

    df_cleaned = df_valid_times
    return (df_cleaned,)


@app.cell
def _(df_cleaned):
    df_cleaned
    return


@app.cell
def _(df_cleaned, os):
    os.makedirs("data/clean", exist_ok=True)

    df_cleaned.to_csv("data/clean/events.csv", index=False)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
