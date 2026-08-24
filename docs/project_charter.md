# DMAIC Project Charter — Solder-Paste Process Variance Reduction

## Problem Statement
Solder-paste thickness on the PCB assembly line runs at Cp ≈ 0.98 (sigma ≈ 8.5 µm std dev against a 100–150 µm spec). Yield losses concentrate in solder bridging and voiding — the top two Pareto categories.

## Goal Statement
Reduce process variance to achieve Cp/Cpk ≥ 1.33 within one improvement cycle; cut defect DPMO by ≥ 50%.

## Scope
**In:** paste printing process, stencil/reflow parameters, SPI measurement system.
**Out:** board design changes, downstream assembly defects.

## SIPOC

| Suppliers | Inputs | Process | Outputs | Customers |
|---|---|---|---|---|
| Paste supplier | Solder paste (alloy, viscosity) | Print → Inspect → Place → Reflow | Assembled PCBs within spec | Next-line assembly |
| Stencil vendor | Stencil (aperture design) | | Defect log & SPI data | Quality/engineering |
| Equipment team | Printer, SPI machine | | Capability reports | End customer |

## CTQ Tree
- **Need:** reliable boards → **CTQ:** paste thickness in-spec → **Measure:** subgroup σ ≤ 6.5 µm, Cpk ≥ 1.33

## Team & Timeline
Process owner, quality engineer, line technicians; Define→Control across 40 production days.
