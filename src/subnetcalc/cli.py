import argparse

from subnetcalc.core import subnet_info


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="subnetcalc")
    parser.add_argument("cidr", help="z. B. 192.168.10.0/26")
    args = parser.parse_args(argv)
    try:
        info = subnet_info(args.cidr)
    except ValueError as e:
        print(f"Fehler: {e}")
        return 1
    for key, value in info.items():
        print(f"{key:<10} {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
