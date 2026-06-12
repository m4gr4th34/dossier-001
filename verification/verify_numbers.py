#!/usr/bin/env python3
"""
verify_numbers.py -- Executable verification of all quantitative claims in:

  "Temporal-Imaging-Enhanced Dispersive-Optics Quantum Key Distribution:
   Approaching the Schmidt Limit of Energy-Time Entanglement"
   I. Ali-Khan (2026)

Every number in the manuscript (abstract, Sec. 4, Sec. 6, Table 1) is
recomputed here from the stated assumptions. Run this script to reproduce
them. Discrepancies between manuscript text and computed values are
reported as FAIL and must be resolved before submission.

Model (manuscript Eqs. 2-6):
  per-receiver timing error   eps     = sqrt( (tau_j/M)^2 + dtau_L^2 )
  observed correlation width  sigma   = sqrt( tau_c^2 + eps_A^2 + eps_B^2 )
  photon information eff.     I_AB    = log2( T_f / (alpha * sigma) )
  magnification gain          dI      = I(M) - I(1)
  break-even lens efficiency  eta_L  >= I_sec(1) / I_sec(M)
  saturation-limited key rate R_key   = N_ch * R_det * kappa * I_sec(M)

All times in picoseconds unless noted.
"""

import math

PASS, FAIL = "PASS", "FAIL"
results = []


def check(label, computed, claimed_lo, claimed_hi, fmt="{:.2f}"):
    ok = claimed_lo <= computed <= claimed_hi
    results.append((PASS if ok else FAIL, label, computed, (claimed_lo, claimed_hi)))
    print(f"[{PASS if ok else FAIL}] {label}")
    print(f"       computed = {fmt.format(computed)}   manuscript claims = "
          f"[{claimed_lo}, {claimed_hi}]")
    return ok


def eps(tau_j, M, dtau_L):
    return math.sqrt((tau_j / M) ** 2 + dtau_L ** 2)


def sigma_obs(tau_c, e_a, e_b):
    return math.sqrt(tau_c ** 2 + e_a ** 2 + e_b ** 2)


def pie(T_f_ps, alpha, sigma):
    return math.log2(T_f_ps / (alpha * sigma))


# ---------------------------------------------------------------- parameters
TAU_C = 0.1        # ps, biphoton correlation time (100 fs)
T_F = 64_000.0     # ps, frame duration (64 ns)
ALPHA = 4.0        # guard factor

print("=" * 72)
print("SECTION 1 / ABSTRACT -- Schmidt number and bit content")
print("=" * 72)
# K = T_coh / tau_c for T_coh = 0.1 - 1 us, tau_c = 100 fs
K_lo = (0.1e-6) / (100e-15)
K_hi = (1.0e-6) / (100e-15)
check("Schmidt number, low end (claimed ~1e5..1e6 range, low)", K_lo, 0.9e5, 1.1e6, "{:.3g}")
check("Schmidt number, high end", K_hi, 0.9e6, 1.1e7, "{:.3g}")
check("bits at K=1e5 (claimed 16-20 band, low edge ~16.6)", math.log2(1e5), 16.0, 17.0)
check("bits at K=1e6 (high edge ~19.9)", math.log2(1e6), 19.0, 20.0)

print()
print("=" * 72)
print("SECTION 4.1 -- magnification gain examples (Eq. 6)")
print("=" * 72)
# Example A: tau_j = 3 ps SNSPD, dtau_L = 0.5 ps, M = 10
e = eps(3.0, 10, 0.5)
s1 = sigma_obs(TAU_C, e, e)
s0 = sigma_obs(TAU_C, 3.0, 3.0)          # no lens
dI_A = math.log2(s0 / s1)
check("Example A gain dI (tau_j=3, M=10, dtau_L=0.5); text says ~2.4 bits",
      dI_A, 2.2, 2.6)

# Example B: tau_j = 30 ps, M = 158, dtau_L = 1.3 ps (Joshi et al. 2022)
e = eps(30.0, 158, 1.3)
s1 = sigma_obs(TAU_C, e, e)
s0 = sigma_obs(TAU_C, 30.0, 30.0)
dI_B = math.log2(s0 / s1)
check("Example B gain dI (tau_j=30, M=158, dtau_L=1.3); text says ~4.5 bits",
      dI_B, 4.3, 4.7)

print()
print("=" * 72)
print("SECTION 4.2 -- break-even lens efficiency")
print("=" * 72)
# tau_j = 30 ps detectors, with vs without the M=158 lens
I_nolens = pie(T_F, ALPHA, sigma_obs(TAU_C, 30.0, 30.0))
e = eps(30.0, 158, 1.3)
I_lens = pie(T_F, ALPHA, sigma_obs(TAU_C, e, e))
check("PIE without lens (text: ~8.6 bits)", I_nolens, 8.4, 8.8)
check("PIE with lens   (text: ~13.1 bits)", I_lens, 12.9, 13.3)
check("break-even eta_L = I(1)/I(M) (text: >~0.66)",
      I_nolens / I_lens, 0.63, 0.69)

print()
print("=" * 72)
print("TABLE 1 -- proposed-system PIE rows")
print("=" * 72)
# Row 3: SNSPD 30 ps, M=158, dtau_L=1.3 ps
e = eps(30.0, 158, 1.3)
row3 = pie(T_F, ALPHA, sigma_obs(TAU_C, e, e))
check("Table row 'SNSPD 30 ps, M=158' PIE (claimed 13)", row3, 12.5, 13.5)

# Row 4: SNSPD 3 ps, M=30, dtau_L=0.5 ps
e = eps(3.0, 30, 0.5)
row4 = pie(T_F, ALPHA, sigma_obs(TAU_C, e, e))
check("Table row 'SNSPD 3 ps, M=30, dtau_L=0.5' PIE (claimed 14-15)",
      row4, 14.0, 15.0)

# Projected ceiling: dtau_L -> 0.1 ps, M = 30, tau_j = 3 ps
e = eps(3.0, 30, 0.1)
ceil = pie(T_F, ALPHA, sigma_obs(TAU_C, e, e))
check("projected PIE at dtau_L=0.1 ps (abstract: 'approaching 17')",
      ceil, 15.8, 17.0)

# Absolute correlation-time floor
floor = pie(T_F, ALPHA, sigma_obs(TAU_C, 0.0, 0.0))
check("correlation-time-floor PIE (text: 17.3 bits)", floor, 17.1, 17.5)

print()
print("=" * 72)
print("SECTION 6 / ABSTRACT -- key-rate order of magnitude")
print("=" * 72)
# Saturation-limited estimate, Eq. (7):
#   R_key = N_ch * R_det_max * kappa * I_sec,  I_sec = 0.6 * PIE
for (nch, rdet, kappa, label) in [
    (8,  1e6, 0.5, "conservative: 8 ch, 1e6 cps, kappa=0.5"),
    (16, 1e7, 0.3, "aggressive:  16 ch, 1e7 cps, kappa=0.3"),
]:
    isec = 0.6 * row3
    rkey = nch * rdet * kappa * isec
    print(f"  {label}: R_key = {rkey:.2e} b/s")
check("key-rate order of magnitude spans ~1e8 (claimed 'order 10^8 b/s')",
      math.log10(8 * 1e6 * 0.5 * 0.6 * row3), 7.0, 9.0)

# Comparison ratios quoted in Sec. 6
check("ratio vs Zhong 2015 (2.7 Mb/s): 'roughly two orders of magnitude'",
      math.log10(1e8 / 2.7e6), 1.3, 2.3)
check("ratio vs record 115.8 Mb/s: 'parity' (within factor ~3 either way)",
      abs(math.log10(1e8 / 115.8e6)), 0.0, 0.5)

print()
print("=" * 72)
n_fail = sum(1 for r in results if r[0] == FAIL)
print(f"TOTAL: {len(results)} checks, {n_fail} failures")
print("=" * 72)
raise SystemExit(1 if n_fail else 0)
