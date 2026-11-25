"""Entry for "Fridge Roast: One Line, Biggest Laugh" (make.fun).

The roast lists everything the smart fridge can do — camera, Wi-Fi,
an app — and then points out the one job it still fails at: telling
fresh milk from a science experiment.
"""

ENTRY = (
    "Your smart fridge has Wi-Fi, a camera, and an app — and still "
    "thinks expired milk is a science experiment worth keeping."
)


def get_entry() -> str:
    """Return the entry line."""
    return ENTRY


def write_entry(output_dir: str) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    import os

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry to $MAKEFUN_OUTPUT_DIR (default /output)."""
    import os

    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
