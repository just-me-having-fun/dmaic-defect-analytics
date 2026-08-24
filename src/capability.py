"""Process capability — Cp / Cpk (Improve/Control phases)."""
import numpy as np


def cp_cpk(values, lsl, usl):
    """Capability indices from raw measurements and spec limits."""
    v = np.asarray(values, dtype=float)
    mu = float(v.mean())
    s = float(v.std(ddof=1))
    cp = (usl - lsl) / (6 * s)
    cpk = min(usl - mu, mu - lsl) / (3 * s)
    return {"mean": round(mu, 1), "sigma": round(s, 2),
            "Cp": round(cp, 2), "Cpk": round(cpk, 2)}
