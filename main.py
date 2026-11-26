import os

# Self-checkout one-liner: the text is emitted verbatim, no trailing newline.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = "Twelve yoghurts, no spoon. So the plan is to drink them like soup and lie about it later?"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
