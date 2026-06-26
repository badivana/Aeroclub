import os
import re
from PIL import Image

ASSETS_DIR = "assets"

TEXT_EXTENSIONS = (".html", ".ejs", ".css", ".js")

converted = 0
skipped = 0
deleted = 0
updated_files = 0

print("=" * 60)
print("Converting images to WebP")
print("=" * 60)

# -------------------------------------------------
# STEP 1 - Convert PNG/JPG/JPEG to WEBP
# -------------------------------------------------

for root, dirs, files in os.walk(ASSETS_DIR):

    for file in files:

        if not file.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        old_path = os.path.join(root, file)
        new_path = os.path.splitext(old_path)[0] + ".webp"

        # Skip if already converted
        if os.path.exists(new_path):
            print(f"[SKIP] {old_path}")
            skipped += 1
            continue

        try:
            print(f"[CONVERT] {old_path}")

            img = Image.open(old_path)

            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGB")

            img.save(
                new_path,
                "WEBP",
                quality=70,
                method=6,
                optimize=True
            )

            converted += 1

        except Exception as e:
            print(f"[FAILED] {old_path}")
            print(e)

print("\nImages converted:", converted)
print("Already converted:", skipped)

# -------------------------------------------------
# STEP 2 - Update HTML/EJS/CSS/JS references
# -------------------------------------------------

print("\nUpdating file references...")

patterns = [
    (".png", ".webp"),
    (".jpg", ".webp"),
    (".jpeg", ".webp")
]

for root, dirs, files in os.walk("."):

    # Ignore node_modules
    if "node_modules" in root:
        continue

    for file in files:

        if not file.endswith(TEXT_EXTENSIONS):
            continue

        path = os.path.join(root, file)

        try:

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = content

            for old, new in patterns:
                new_content = re.sub(
                    re.escape(old) + r'(?=["\'?)])',
                    new,
                    new_content,
                    flags=re.IGNORECASE
                )

            if new_content != content:

                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)

                updated_files += 1
                print(f"[UPDATED] {path}")

        except Exception:
            pass

print("\nFiles updated:", updated_files)

# -------------------------------------------------
# STEP 3 - Delete originals ONLY if WEBP exists
# -------------------------------------------------

print("\nDeleting originals...")

for root, dirs, files in os.walk(ASSETS_DIR):

    for file in files:

        if not file.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        old_path = os.path.join(root, file)
        webp = os.path.splitext(old_path)[0] + ".webp"

        if os.path.exists(webp):

            try:
                os.remove(old_path)
                deleted += 1
                print(f"[DELETED] {old_path}")

            except Exception as e:
                print(f"[FAILED DELETE] {old_path}")
                print(e)

print("\nDeleted originals:", deleted)

print("\n")
print("=" * 60)
print("DONE!")
print("=" * 60)
print("Converted :", converted)
print("Skipped   :", skipped)
print("Updated   :", updated_files)
print("Deleted   :", deleted)
print("=" * 60)