"""lumen_optics — shared runnable harness for HYPOTHESES hypothesis cards.

Deterministic, dependency-free (stdlib `math` only) physics primitives for the
EUV / sub-13.5 nm light-source problem. HYPOTHESES cards reference these functions
from their per-hypothesis run scripts under `state/<hX>/` (anima-parity: shared
machinery lives in repo-root `tool/`, per-hypothesis runs live in `state/`).

Every function is a closed-form public-physics relation — no fitting, no hidden
constants beyond the documented defaults. All inputs are explicit so a card's
falsifiers can be evaluated against the returned numbers.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


# --- projection-optics throughput (multilayer-mirror chain) -------------------

def mirror_chain_throughput(reflectivity: float, n_mirrors: int) -> float:
    """Optical throughput of an all-reflective EUV column = R**N.

    EUV is absorbed by all materials, so the column is a chain of N multilayer
    mirrors each passing a fraction `reflectivity` of the incident photons.
    """
    if not (0.0 < reflectivity <= 1.0):
        raise ValueError(f"reflectivity out of (0,1]: {reflectivity}")
    if n_mirrors < 1:
        raise ValueError(f"n_mirrors must be >= 1: {n_mirrors}")
    return reflectivity ** n_mirrors


def column_throughput_mixed(r_graze: float, n_graze: int, r_image: float, n_image: int) -> float:
    """Throughput of a mixed column: n_graze grazing-incidence surfaces (high R)
    feeding n_image near-normal imaging mirrors = r_graze**n_graze * r_image**n_image.
    Grazing optics suit collection/transport, not high-NA imaging (see card limits)."""
    for name, v in (("r_graze", r_graze), ("r_image", r_image)):
        if not (0.0 < v <= 1.0):
            raise ValueError(f"{name} out of (0,1]: {v}")
    if n_graze < 0 or n_image < 0:
        raise ValueError("mirror counts must be >= 0")
    return r_graze ** n_graze * r_image ** n_image


def source_power_multiplier(r_ref: float, r_new: float, n_mirrors: int) -> float:
    """How many times more source power a lower-reflectivity band needs to hold
    constant wafer dose through the same N-mirror column.

    = throughput(r_ref) / throughput(r_new) = (r_ref / r_new)**N.
    """
    return mirror_chain_throughput(r_ref, n_mirrors) / mirror_chain_throughput(
        r_new, n_mirrors
    )


# --- resolution / depth-of-focus trade ---------------------------------------

def resolution_half_pitch(k1: float, wavelength_nm: float, na: float) -> float:
    """Printable half-pitch (nm) = k1 * lambda / NA. Smaller is finer."""
    if na <= 0:
        raise ValueError(f"NA must be > 0: {na}")
    return k1 * wavelength_nm / na


def depth_of_focus(k2: float, wavelength_nm: float, na: float) -> float:
    """Depth-of-focus (nm) = k2 * lambda / NA**2. Falls with NA**2."""
    if na <= 0:
        raise ValueError(f"NA must be > 0: {na}")
    return k2 * wavelength_nm / (na ** 2)


# --- LPP source power budget --------------------------------------------------

def lpp_source_power(
    rep_rate_hz: float,
    drive_pulse_j: float,
    conversion_efficiency: float,
    collection_fraction: float,
) -> float:
    """In-band EUV power (W) delivered to intermediate focus from a
    laser-produced-plasma (LPP) source.

    P = f_rep * E_drive * CE * collection
      - rep_rate_hz       : Sn droplet / laser repetition rate (Hz)
      - drive_pulse_j     : drive-laser energy per pulse (J)
      - conversion_efficiency : drive -> in-band (2% BW @ 13.5 nm) fraction
      - collection_fraction   : collected/usable fraction at intermediate focus
    """
    for name, v in (
        ("conversion_efficiency", conversion_efficiency),
        ("collection_fraction", collection_fraction),
    ):
        if not (0.0 <= v <= 1.0):
            raise ValueError(f"{name} out of [0,1]: {v}")
    return rep_rate_hz * drive_pulse_j * conversion_efficiency * collection_fraction


# --- compact (plasma-wakefield) accelerator gradient --------------------------
# Reference-matched to dancinlab/demiurge cern-accelerator (hexa-lang
# stdlib/cern/plasma_wakefield.hexa): Dawson cold non-relativistic wave-breaking
# field. At n_e = 1e18 cm^-3 → omega_p = 5.6414e13 rad/s, E_0 = 96.159 GV/m.

_ELEM_CHARGE = 1.602176634e-19      # C
_ELECTRON_MASS = 9.1093837015e-31   # kg
_SPEED_OF_LIGHT = 299792458.0       # m/s
_VAC_PERMITTIVITY = 8.8541878128e-12  # F/m


def plasma_omega(n_e_cm3: float) -> float:
    """Plasma angular frequency omega_p = sqrt(n_e e^2 / (eps0 m_e)) [rad/s].
    Input density in cm^-3 (the LWFA-literature unit)."""
    if n_e_cm3 <= 0:
        raise ValueError(f"n_e must be > 0: {n_e_cm3}")
    n_e_m3 = n_e_cm3 * 1.0e6
    return math.sqrt(n_e_m3 * _ELEM_CHARGE ** 2 / (_VAC_PERMITTIVITY * _ELECTRON_MASS))


def wavebreak_field(omega_p: float) -> float:
    """Cold non-relativistic wave-breaking field E_0 = m_e c omega_p / e [V/m]
    (Dawson 1959) — the characteristic accelerating-gradient scale."""
    return _ELECTRON_MASS * _SPEED_OF_LIGHT * omega_p / _ELEM_CHARGE


def accelerator_length(target_energy_ev: float, gradient_v_per_m: float) -> float:
    """Accelerator length (m) to reach a target electron energy at a given
    accelerating gradient: L = E[eV] / gradient[V/m] (1 eV gained per volt)."""
    if gradient_v_per_m <= 0:
        raise ValueError(f"gradient must be > 0: {gradient_v_per_m}")
    return target_energy_ev / gradient_v_per_m


# --- electron-beam light generation (undulator / inverse-Compton) ------------
# Standard relativistic radiation relations. m_e c^2 = 0.51099895 MeV.

_ELECTRON_REST_EV = 510998.95  # eV


def lorentz_gamma(energy_ev: float) -> float:
    """Lorentz factor gamma = E_total / (m_e c^2). Ultra-relativistic regime."""
    if energy_ev <= 0:
        raise ValueError(f"energy must be > 0: {energy_ev}")
    return energy_ev / _ELECTRON_REST_EV


def undulator_wavelength(period_nm: float, gamma: float, k: float, harmonic: int = 1) -> float:
    """On-axis undulator radiation wavelength (nm):
    lambda_n = period / (2 n gamma^2) * (1 + K^2/2).
    K is the deflection parameter (K = 0.9337 * B[T] * period[cm])."""
    if gamma <= 0 or harmonic < 1:
        raise ValueError(f"bad gamma/harmonic: {gamma}, {harmonic}")
    return period_nm / (2.0 * harmonic * gamma ** 2) * (1.0 + k ** 2 / 2.0)


def energy_for_undulator_wavelength(target_nm: float, period_nm: float, k: float,
                                    harmonic: int = 1) -> float:
    """Electron energy (eV) whose undulator fundamental hits target wavelength."""
    if target_nm <= 0:
        raise ValueError(f"target must be > 0: {target_nm}")
    gamma_sq = period_nm * (1.0 + k ** 2 / 2.0) / (2.0 * harmonic * target_nm)
    return math.sqrt(gamma_sq) * _ELECTRON_REST_EV


def inverse_compton_wavelength(laser_nm: float, gamma: float) -> float:
    """Head-on inverse-Compton backscatter wavelength (nm):
    lambda_x ~ laser / (4 gamma^2)."""
    if gamma <= 0:
        raise ValueError(f"gamma must be > 0: {gamma}")
    return laser_nm / (4.0 * gamma ** 2)


# --- HVM throughput (wafers-per-hour) ----------------------------------------

def hvm_throughput_wph(source_power_w: float, ref_power_w: float, ref_wph: float) -> float:
    """Wafer-per-hour throughput under the first-order assumption that, at fixed
    dose, throughput scales linearly with in-band source power delivered to the
    wafer: WPH = ref_wph * (source_power / ref_power)."""
    if ref_power_w <= 0:
        raise ValueError(f"ref_power must be > 0: {ref_power_w}")
    return ref_wph * source_power_w / ref_power_w


def power_for_throughput(target_wph: float, ref_power_w: float, ref_wph: float) -> float:
    """Inverse of hvm_throughput_wph: in-band power (W) needed for target WPH."""
    if ref_wph <= 0:
        raise ValueError(f"ref_wph must be > 0: {ref_wph}")
    return ref_power_w * target_wph / ref_wph


def average_power(rep_rate_hz: float, pulse_energy_j: float) -> float:
    """Average power (W) of a pulsed source = rep rate * energy per pulse."""
    return rep_rate_hz * pulse_energy_j


def cost_of_ownership(capex_unit: float, opex_base: float, eta_ratio: float,
                      n_scanners: int) -> float:
    """Normalized $/wafer-layer for a coherent/ERL source:
    CAPEX amortized over N scanners + OPEX_energy scaled by 1/(efficiency ratio).
    = capex_unit / n_scanners + opex_base / eta_ratio."""
    if eta_ratio <= 0 or n_scanners < 1:
        raise ValueError("eta_ratio > 0 and n_scanners >= 1 required")
    return capex_unit / n_scanners + opex_base / eta_ratio


def gain_length_product(gain_per_cm: float, length_cm: float) -> float:
    """X-ray-laser gain-length product gL (dimensionless). Saturated ASE needs
    gL >= ~14-15 (the e^15 ~ 3e6 single-pass amplification rule of thumb)."""
    if gain_per_cm < 0 or length_cm < 0:
        raise ValueError("gain and length must be >= 0")
    return gain_per_cm * length_cm


def erl_rep_rate_ceiling(heat_budget_w: float, energy_per_bunch_j: float,
                         eta_recover: float) -> float:
    """Thermal-limited rep-rate ceiling [Hz] with energy-recovery linac (ERL):
    only the un-recovered fraction (1 - eta) deposits heat, so
    f_max = heat_budget / (energy_per_bunch * (1 - eta_recover)).
    As eta_recover -> 1 the ceiling diverges (no thermodynamic floor)."""
    if not (0.0 <= eta_recover < 1.0):
        raise ValueError(f"eta_recover out of [0,1): {eta_recover}")
    if energy_per_bunch_j <= 0 or heat_budget_w <= 0:
        raise ValueError("heat budget and bunch energy must be > 0")
    return heat_budget_w / (energy_per_bunch_j * (1.0 - eta_recover))


def spf_recovery(spf_transmission: float) -> float:
    """In-band power recovered by dropping the spectral-purity filter a broadband
    source needs but a narrow source does not: recovery = 1 / SPF_transmission."""
    if not (0.0 < spf_transmission <= 1.0):
        raise ValueError(f"spf_transmission out of (0,1]: {spf_transmission}")
    return 1.0 / spf_transmission


def undulator_natural_linewidth(harmonic: int, n_periods: int) -> float:
    """Relative spectral width of an ideal undulator line ~ 1/(n*N)."""
    if harmonic < 1 or n_periods < 1:
        raise ValueError(f"bad harmonic/n_periods: {harmonic}, {n_periods}")
    return 1.0 / (harmonic * n_periods)


def energy_spread_broadening(sigma_gamma_rel: float) -> float:
    """Relative undulator-line broadening from electron energy spread:
    delta_lambda/lambda ~ 2 * (sigma_gamma/gamma)."""
    if sigma_gamma_rel < 0:
        raise ValueError(f"sigma must be >= 0: {sigma_gamma_rel}")
    return 2.0 * sigma_gamma_rel


# --- falsifier harness --------------------------------------------------------

@dataclass
class Falsifier:
    """One pre-registered, measurable falsifier. `predicate(metrics) -> bool`
    returns True when the falsifier is TRIGGERED (hypothesis component refuted)."""

    name: str
    predicate: object  # callable(dict) -> bool
    desc: str = ""


def evaluate(metrics: dict, falsifiers: list) -> dict:
    """Run each falsifier against the measured metrics. A falsifier PASSes when
    it is NOT triggered. Returns a verdict ledger (all-stdlib, JSON-safe)."""
    results = []
    for f in falsifiers:
        triggered = bool(f.predicate(metrics))
        results.append(
            {"name": f.name, "triggered": triggered, "status": "FAIL" if triggered else "PASS"}
        )
    n_pass = sum(1 for r in results if r["status"] == "PASS")
    return {
        "metrics": metrics,
        "falsifiers": results,
        "n_pass": n_pass,
        "n_total": len(results),
        "all_pass": n_pass == len(results),
    }
