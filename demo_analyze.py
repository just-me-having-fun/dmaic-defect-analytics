"""Demo: Analyze/Improve statistics — hypothesis tests, sigma level, fishbone."""
import os

from src.synth_defects import LSL, USL, generate_process
from src.tests_stats import f_test_variance, welch_t_test
from src.sigma_level import dpmo, sigma_level
from src.fishbone import fishbone

os.makedirs("outputs", exist_ok=True)

subgroups, defects = generate_process(days=40, improvement_day=25)
vals = subgroups.filter(regex=r"^x").to_numpy().ravel()
before, after = vals[:125], vals[125:]

# ---- Hypothesis tests -----------------------------------------------------------
print("=== HYPOTHESIS TESTS (alpha=0.05) ===")
print(f"F-test   : {f_test_variance(before, after)}")
print(f"Welch t  : {welch_t_test(before, after)}")

# ---- Sigma level -----------------------------------------------------------------
BOARDS_PER_DAY = 400  # production volume; SPI subgroups are a daily sample
total_defects = int(defects["count"].sum())
before_defects = int(defects[defects["day"] < 25]["count"].sum())
after_defects = total_defects - before_defects

d_before = dpmo(before_defects, 25 * BOARDS_PER_DAY)
d_after = dpmo(after_defects, 15 * BOARDS_PER_DAY)
print("\n=== SIGMA LEVEL ===")
print(f"  Before: {before_defects} defects -> {d_before:,.0f} DPMO -> {sigma_level(d_before)} sigma")
print(f"  After : {after_defects} defects -> {d_after:,.0f} DPMO -> {sigma_level(d_after)} sigma")

# ---- Fishbone ----------------------------------------------------------------------
cause_map = {
    "Machine": ["stencil wear", "printer squeegee pressure drift"],
    "Method": ["reflow profile drift", "print speed not standardised"],
    "Material": ["paste viscosity variation", "paste past shelf life"],
    ("Manpower"): ["operator changeover errors"],
    "Measurement": ["SPI calibration gap", "gage R&R unverified"],
    "Environment": ["humidity swings in storage"],
}
fishbone(cause_map)
print("\nSaved outputs/: fishbone.png")
