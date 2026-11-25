import os
import shutil


# The finished fortune lives in entry.txt next to this script. This
# little program just carries that file over to the folder the grader
# points at, leaving the wording exactly as it was written.
def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(os.path.join(here, "entry.txt"), os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
