"""X-bar / R control charts (Control phase)."""
import matplotlib.pyplot as plt
import numpy as np

# Shewhart constants for subgroup size n=5
A2, D3, D4 = 0.577, 0.0, 2.114


def xbar_r_stats(subgroups):
    vals = subgroups.filter(regex=r"^x")
    xbars = vals.mean(axis=1)
    ranges = vals.max(axis=1) - vals.min(axis=1)
    xbb, rbar = float(xbars.mean()), float(ranges.mean())
    return {
        "xbars": xbars,
        "ranges": ranges,
        "xbar_bar": round(xbb, 2),
        "xbar_ucl": round(xbb + A2 * rbar, 2),
        "xbar_lcl": round(xbb - A2 * rbar, 2),
        "r_ucl": round(D4 * rbar, 2),
        "out_of_control": int(((xbars > xbb + A2 * rbar) |
                               (xbars < xbb - A2 * rbar)).sum()),
    }


def xbar_plot(stats, path, vline_day=None):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    days = stats["xbars"].index
    ax.plot(days, stats["xbars"], marker="o", ms=3, lw=1.2, color="#264653")
    ax.axhline(stats["xbar_ucl"], color="#e76f51", ls="--", lw=1)
    ax.axhline(stats["xbar_lcl"], color="#e76f51", ls="--", lw=1)
    ax.axhline(stats["xbar_bar"], color="#666", lw=1)
    if vline_day is not None:
        ax.axvline(vline_day - 0.5, color="#2a9d8f", lw=1.5)
        ax.text(vline_day + 0.3, ax.get_ylim()[0] + 1,
                "process change", color="#2a9d8f", fontsize=9)
    ax.set_title("X-bar chart: solder paste thickness (µm)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Subgroup mean (µm)")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
