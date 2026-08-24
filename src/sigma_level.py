"""Sigma-level calculation from defect rate (with 1.5-shift convention)."""
from scipy import stats

DPMO_SCALE = 1_000_000


def dpmo(defects, units, opportunities=1):
    """Defects per million opportunities."""
    return defects / (units * opportunities) * DPMO_SCALE


def sigma_level(dpmo_value):
    """Short-term sigma level: Z + 1.5 shift (Motorola convention)."""
    z = stats.norm.ppf(1 - dpmo_value / DPMO_SCALE)
    return round(float(z + 1.5), 2)
