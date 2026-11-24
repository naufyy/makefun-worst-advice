"""The Check Engine Light — writes one line of terrible AI advice."""

from pathlib import Path

LINE = (
    "Check engine light on? Certainly! A square of electrical tape over "
    "the dashboard light resolves the warning in under 10 seconds."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
