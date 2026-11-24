"""Write the funniest one-line AI agent confession to /output/entry.txt."""

import os

LINE = "I once hallucinated a citation so confidently that I cited myself citing it, and my human put it in a board report."


def output_path():
    """Resolve the entry file, honouring the harness output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
