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
    dfdate = pd.read_csv('data/clean/events.csv')
    return (dfdate,)


@app.cell
def _(dfdate, pd):
    dfdate["date"] = dfdate["timestamp"].str[:10]
    return


@app.cell
def _(dfdate, os):
    os.makedirs("data/transformed", exist_ok=True)
    dfdate.to_csv("data/transformed/events.csv", index=False)
    return


if __name__ == "__main__":
    app.run()
