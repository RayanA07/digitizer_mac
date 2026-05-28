from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def make_icon(path: Path, bg: tuple[int, int, int, int], fg: tuple[int, int, int, int], text: str) -> None:
    sizes = [(1024, 1024), (512, 512), (256, 256), (128, 128), (64, 64), (32, 32), (16, 16)]
    images: list[Image.Image] = []
    for width, height in sizes:
        image = Image.new("RGBA", (width, height), bg)
        draw = ImageDraw.Draw(image)
        margin = max(8, width // 14)
        draw.rounded_rectangle(
            (margin, margin, width - margin, height - margin),
            radius=max(16, width // 8),
            fill=bg,
            outline=fg,
            width=max(4, width // 28),
        )
        try:
            font = ImageFont.truetype("Arial Bold.ttf", int(width * 0.5))
        except Exception:
            font = ImageFont.load_default()
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        draw.text(((width - text_width) / 2, (height - text_height) / 2 - height * 0.04), text, fill=fg, font=font)
        images.append(image)
    images[0].save(path, format="ICNS", append_images=images[1:])


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    make_icon(ASSETS / "digitizer.icns", (22, 96, 166, 255), (255, 255, 255, 255), "D")
    make_icon(ASSETS / "accuracytester.icns", (36, 122, 74, 255), (255, 255, 255, 255), "A")


if __name__ == "__main__":
    main()
