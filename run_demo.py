"""Runnable demo for Excellence Engine v4.

    python run_demo.py

Builds a ledger from real program claims (plus one deliberate overclaim so you
can see beta bite), scores it, and prints the human report, then the JSON, then
the deterministic run stamp. Also demonstrates each firewall guard firing.
"""
from excellence_engine_v4 import (
    ExcellenceEngine,
    EngineInput,
    Claim,
    ClaimLedger,
    Status,
    Quantity,
    Metric,
    NP_ANALOGY,
    bind_domain_coordinate,
    FirewallError,
    UndefinedMetricError,
    NonSovereigntyError,
)


def build_ledger() -> ClaimLedger:
    led = ClaimLedger()
    # FORMAL spine
    led.add(Claim("CI", "Kakeya/common-center completion identity", Status.FORMAL, 1.0))
    led.add(Claim("C2", "C_2(delta) ~ log(1/delta)", Status.FORMAL, 1.0))
    led.add(Claim("EM", "excess-mass identity I.1/I.2", Status.FORMAL, 1.0))
    led.add(Claim("TN", "trace-neutral operator Thm A-C", Status.FORMAL, 1.0))
    # OPEN fireholds
    led.add(Claim("RH", "Riemann Hypothesis", Status.OPEN, 1.0))
    led.add(Claim("CO", "Coleman Conjecture (K=>R)", Status.OPEN, 1.0))
    led.add(Claim("C3", "C_3 compression rate", Status.OPEN, 1.0))
    led.add(Claim("2AS", "002.A-strong", Status.OPEN, 1.0))
    # CLOSED-NEGATIVE
    led.add(Claim("ZT", "zeta(0) transport to Re(s)=1/2", Status.CLOSED_NEGATIVE, 1.0))
    # ANALOGY
    led.add(Claim("WBC", "L^2_C as white-blood-cell", Status.ANALOGY, 1.0))
    # One DELIBERATE overclaim: Coleman presented as FORMAL though it is OPEN.
    led.add(Claim("OVR", "Coleman asserted as settled", Status.OPEN, 1.0,
                  asserted_as=Status.FORMAL))
    return led


def main() -> None:
    inp = EngineInput(
        agreements=[0.92, 0.88, 0.95, 0.90],   # Claude / Grok / GPT / Gemini agreement
        ledger=build_ledger(),
        contradiction_rate=0.0,
        cup_pass_rate=0.9,
        d=0.9, c=0.95, e=0.82, h=0.99,
        headline_metrics={
            "cup_pass": Metric(
                value=0.90,
                counted="claims surviving adversarial probe",
                population="all CUP probes this run",
                source="cup_probe_log v4",
            ),
        },
    )

    report = ExcellenceEngine().score(inp)
    print(report.render())
    print()
    print("JSON report:")
    print(report.to_json())

    print()
    print("Ledger status counts:", inp.ledger.counts())

    # --- firewall demonstrations --------------------------------------------
    print()
    print("Firewall guards (each SHOULD raise):")

    try:
        bind_domain_coordinate(Quantity(-0.5, "codomain_value", "zeta(0)"))
    except FirewallError as ex:
        print("  [blocked] zeta(0) transport ->", str(ex).split(".")[0])

    try:
        Metric(0.94, counted="", population="runs", source="log")
    except UndefinedMetricError as ex:
        print("  [blocked] undefined headline metric ->", ex)

    try:
        NP_ANALOGY.as_mechanism()
    except FirewallError as ex:
        print("  [blocked] NP-as-mechanism ->", str(ex).split(".")[0])

    try:
        ExcellenceEngine().score(EngineInput(h=1.0))
    except NonSovereigntyError as ex:
        print("  [blocked] h >= 1 ->", str(ex).split("(")[0].strip())


if __name__ == "__main__":
    main()
