"""Synthetic solder-paste process data for the DMAIC case study (no real data)."""
import numpy as np
import pandas as pd

LSL, USL = 100.0, 150.0  # paste thickness spec limits (µm)

DEFECT_BASE = {
    "solder bridge": 6,
    "void": 5,
    "component shift": 4,
    "missing part": 2,
    "contamination": 2,
    "crack": 1,
}


def generate_process(days=40, seed=11, improvement_day=None,
                     mu=125.0, sigma_before=9.0, sigma_after=6.5, subgroup=5):
    """Daily subgroups of paste-thickness measurements + a defect log.

    If improvement_day is set, process sigma drops from sigma_before to
    sigma_after from that day on (simulating an Improve-phase fix).
    """
    rng = np.random.default_rng(seed)
    rows = []
    for day in range(days):
        s = sigma_before
        if improvement_day is not None and day >= improvement_day:
            s = sigma_after
        vals = rng.normal(mu, s, subgroup)
        rows.append({"day": day, **{f"x{i + 1}": round(v, 1) for i, v in enumerate(vals)}})
    subgroups = pd.DataFrame(rows)

    log_rows = []
    for day in range(days):
        decay = 0.45 if (improvement_day is not None and day >= improvement_day) else 1.0
        for dtype, base in DEFECT_BASE.items():
            cnt = int(rng.poisson(base * decay))
            if cnt:
                log_rows.append({"day": day, "defect_type": dtype, "count": cnt})
    defects = (pd.DataFrame(log_rows)
               .groupby(["day", "defect_type"], as_index=False)["count"].sum())
    return subgroups, defects
