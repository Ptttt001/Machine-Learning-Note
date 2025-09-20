import os

def rename_md_files(base_path="."):
    for dirpath, _, filenames in os.walk(base_path):
        for filename in filenames:
            if filename.lower().endswith(".md"):
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, "README.md")

                # prevent overwriting if README.md already exists
                if os.path.exists(new_path) and old_path != new_path:
                    print(f"Skipped (README.md already exists): {old_path}")
                else:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")

if __name__ == "__main__":
    rename_md_files(".")  # start from current folder
