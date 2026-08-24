"""Hypothesis tests for the Analyze/Improve phases (scipy)."""
import numpy as np
from scipy import stats


def f_test_variance(before, after):
    """Two-sided F-test: H0 = equal process variance."""
    before, after = np.asarray(before), np.asarray(after)
    f = before.var(ddof=1) / after.var(ddof=1)
    p = 2 * min(stats.f.cdf(f, len(before) - 1, len(after) - 1),
                1 - stats.f.cdf(f, len(before) - 1, len(after) - 1))
    return {"F": round(float(f), 3), "p_value": round(float(p), 5),
            "verdict": "variance reduced" if p < 0.05 else "no significant change"}


def welch_t_test(before, after):
    """Welch t-test on means: H0 = same process mean."""
    res = stats.ttest_ind(np.asarray(before), np.asarray(after), equal_var=False)
    return {"t": round(float(res.statistic), 3),
            "p_value": round(float(res.pvalue), 5),
            "verdict": "mean shifted" if res.pvalue < 0.05 else "mean unchanged"}
