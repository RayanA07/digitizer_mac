from __future__ import annotations

import sys
from typing import Sequence

from digitizer_2_11 import configure_runtime_paths
from digitizer_cli import interactive_main, main as cli_main


def main(argv: Sequence[str] | None = None) -> int:
    """CLI-only launcher used by the macOS datadigitizer executable."""

    configure_runtime_paths()
    args = list(sys.argv[1:] if argv is None else argv)

    if not args:
        return interactive_main()

    command = args[0].lower()
    if command in {"interactive", "wizard", "menu"}:
        return interactive_main()
    if command in {"cli", "digitize", "run"}:
        if len(args) == 1:
            return interactive_main()
        return cli_main(args[1:])
    if command in {"help", "--help", "-h"}:
        print_help()
        return 0

    return cli_main(args)


def print_help() -> None:
    print(
        "\n".join(
            [
                "Data Digitizer 2.11.mac CLI",
                "",
                "Interactive menu:",
                "  /Users/aakashsjoshi/Downloads/DataDigitizer-2.11.mac/datadigitizer",
                "",
                "One-line digitization:",
                "  /Users/aakashsjoshi/Downloads/DataDigitizer-2.11.mac/datadigitizer --pic-dir /path/to/plot.png --color 255,0,0 --tick-setting \"[10,200],[500,200],[10,200],[10,20]\" --axis-values 0,10,0,100",
                "",
                "Auto color, OCR ticks, and OCR axis values:",
                "  /Users/aakashsjoshi/Downloads/DataDigitizer-2.11.mac/datadigitizer --pic-dir /path/to/plot.png",
                "",
                "Full option help:",
                "  /Users/aakashsjoshi/Downloads/DataDigitizer-2.11.mac/datadigitizer cli --help",
            ]
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
