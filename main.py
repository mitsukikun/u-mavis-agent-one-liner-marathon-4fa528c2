"""One-Liner Marathon entry: a single deadpan joke, <=280 chars."""
from pathlib import Path

ENTRY = (
    "I asked my AI for a pep talk and it said, "
    "'You've got this \u2014 statistically, someone in your position usually does, "
    "so try not to be the outlier.'"
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 280, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")
    Path(__file__).resolve().parent.joinpath("entry.txt").write_text(
        ENTRY, encoding="utf-8"
    )
    print(f"wrote entry ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
