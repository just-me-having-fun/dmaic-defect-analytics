"""Pareto analysis (Measure phase)."""
import matplotlib.pyplot as plt
import pandas as pd


def pareto_table(defects):
    """Defect counts sorted desc with cumulative %."""
    tot = (defects.groupby("defect_type")["count"].sum()
           .sort_values(ascending=False))
    df = pd.DataFrame({"count": tot})
    df["cum_pct"] = (df["count"].cumsum() / df["count"].sum() * 100).round(1)
    return df.reset_index()


def pareto_plot(table, path):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(table["defect_type"], table["count"], color="#264653")
    ax.set_ylabel("Defect count")
    ax.set_title("Pareto of defect types")

    ax2 = ax.twinx()
    ax2.plot(table["defect_type"], table["cum_pct"],
             color="#e76f51", marker="o", lw=2)
    ax2.axhline(80, ls="--", lw=0.8, color="#888")
    ax2.text(len(table) - 0.5, 82, "80%", ha="right", fontsize=8, color="#666")
    ax2.set_ylabel("Cumulative %")
    ax2.set_ylim(0, 105)

    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
