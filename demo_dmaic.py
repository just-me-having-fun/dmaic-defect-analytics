"""Demo: mini DMAIC pipeline on synthetic solder-paste data.

Measure (Pareto) -> Analyze (control chart) -> Improve/Control (capability
before vs after a variance-reduction change).
"""
import os

from src.synth_defects import LSL, USL, generate_process
from src.pareto import pareto_plot, pareto_table
from src.spc import xbar_plot, xbar_r_stats
from src.capability import cp_cpk

os.makedirs("outputs", exist_ok=True)

IMPROVEMENT_DAY = 25
subgroups, defects = generate_process(days=40, improvement_day=IMPROVEMENT_DAY)

# ---- MEASURE: Pareto ----------------------------------------------------------
table = pareto_table(defects)
print("=== MEASURE — Pareto of defect types ===")
print(table.to_string(index=False))
vital = table[table["cum_pct"] <= 80]["defect_type"].tolist()
print(f"\nVital few (<=80% of defects): {', '.join(vital)}")
pareto_plot(table, "outputs/pareto_defects.png")

# ---- ANALYZE: control chart -----------------------------------------------------
stats = xbar_r_stats(subgroups)
print("\n=== ANALYZE — X-bar / R statistics ===")
print(f"  Grand mean : {stats['xbar_bar']} µm  (spec {LSL:.0f}–{USL:.0f})")
print(f"  UCL / LCL  : {stats['xbar_ucl']} / {stats['xbar_lcl']}")
print(f"  R-bar UCL  : {stats['r_ucl']}")
print(f"  Out-of-control points: {stats['out_of_control']}")
xbar_plot(stats, "outputs/xbar_chart.png", vline_day=IMPROVEMENT_DAY)

# ---- IMPROVE/CONTROL: capability before vs after ---------------------------------
vals = subgroups.filter(regex=r"^x").to_numpy().ravel()
before = vals[:IMPROVEMENT_DAY * 5]
after = vals[IMPROVEMENT_DAY * 5:]
print("\n=== IMPROVE — process capability (before vs after) ===")
print(f"  Before: {cp_cpk(before, LSL, USL)}")
print(f"  After : {cp_cpk(after, LSL, USL)}")

print("\nSaved outputs/: pareto_defects.png, xbar_chart.png")
