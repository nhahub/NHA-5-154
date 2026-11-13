
from pathlib import Path
from PIL import Image, ImageOps

folder = Path("assets/cities")

total_before = 0
total_after = 0

for path in sorted(folder.glob("*.jpg")):
    before = path.stat().st_size
    temp = path.with_name(path.stem + ".optimized.jpg")

    try:
        with Image.open(path) as original:
            img = ImageOps.exif_transpose(original)
            img.thumbnail((1600, 1600), Image.Resampling.LANCZOS)

            if img.mode != "RGB":
                img = img.convert("RGB")

            img.save(
                temp,
                "JPEG",
                quality=78,
                optimize=True,
                progressive=True
            )

        if temp.stat().st_size < before:
            temp.replace(path)
        else:
            temp.unlink()

        after = path.stat().st_size
        total_before += before
        total_after += after

        print(
            f"{path.name}: "
            f"{before / 1024 / 1024:.2f} MB -> "
            f"{after / 1024 / 1024:.2f} MB"
        )

    except Exception as error:
        if temp.exists():
            temp.unlink()
        print(f"Error with {path.name}: {error}")

print("\nFinished!")
print(f"Before: {total_before / 1024 / 1024:.2f} MB")
print(f"After:  {total_after / 1024 / 1024:.2f} MB")
