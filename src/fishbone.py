"""Fishbone (Ishikawa) diagram rendering for root-cause analysis."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def fishbone(cause_map, title="Fishbone — solder bridge defects", path="outputs/fishbone.png"):
    """cause_map: {category: [cause, ...]} rendered on a standard spine."""
    categories = list(cause_map.keys())
    n = len(categories)
    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.annotate("", xy=(10.2, 0), xytext=(0.3, 0),
                arrowprops=dict(arrowstyle="-|>", lw=2.2, color="#1a1a2e"))
    ax.text(10.25, 0, "Solder\nbridge", fontsize=11, fontweight="bold", va="center")

    for i, cat in enumerate(categories):
        top = i % 2 == 0
        x0 = 1.4 + i * 1.55
        y1 = 1.9 if top else -1.9
        ax.plot([x0 + 0.75, x0], [y1, 0], color="#264653", lw=1.8)
        ax.text(x0 + 0.05, y1 * 1.06, cat, fontsize=10, fontweight="bold",
                ha="center", color="#264653")
        for j, cause in enumerate(cause_map[cat]):
            yc = y1 / (j + 2) * 1.35
            dx = -0.28 if top else -0.28
            ax.plot([x0 + 0.45 + j * 0.22 + dx, x0 + 0.32 + j * 0.22 + dx],
                    [yc, yc], color="#777", lw=1)
            ax.text(x0 + 0.30 + j * 0.22 + dx - 0.03, yc, cause,
                    fontsize=7.6, va="center",
                    ha="left" if top else "left")

    ax.set_xlim(-0.2, 12)
    ax.set_ylim(-3.1, 3.1)
    ax.axis("off")
    ax.set_title(title, fontsize=13, pad=12)
    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
