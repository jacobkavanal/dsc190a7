import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import os

    return os, pd


@app.cell
def _(pd):
    df = pd.read_csv('data/transformed/events.csv')
    return


@app.cell
def _(os, pd):
    events = pd.read_csv("data/transformed/events.csv")
    events["duration_minutes"] = events["duration_seconds"] / 60
    events["weekday"] = pd.to_datetime(events["date"]).dt.day_name()

    os.makedirs("data/features", exist_ok=True)
    events.to_csv("data/features/events.csv", index=False)
    return (events,)


@app.cell
def _(events):
    events
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
