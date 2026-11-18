import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    events = pd.read_csv("../data/features/events.csv")
    plt.hist(events["duration_minutes"].dropna())
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Number of events")
    plt.title("Distribution of Event Durations")
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
