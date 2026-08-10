# Accuracy Tester (macOS)

A standalone desktop tool that compares a digitized CSV against a reference
("original") CSV and reports accuracy metrics. Independent of the Digitizer app.

There are two ways to use it: the **app** compares two files at a time with plots,
and the **batch CLI** scores a whole folder in one command. Both use the same
statistics engine (`accuracy_core.py`), so their numbers agree exactly.

## Run the app (no Python needed)

Download `AccuracyTester-macos.app.zip` from the
[Releases page](https://github.com/RayanA07/digitizer_mac/releases), double-click
the zip to unpack `AccuracyTester.app`, then double-click the app.

On first launch macOS Gatekeeper may say the app is from an "unidentified
developer". Right-click (or Control-click) `AccuracyTester.app`, choose **Open**,
then **Open** again — or allow it under **System Settings → Privacy & Security →
Open Anyway**.

Then:

1. **Load the ORIGINAL CSV** into the left (blue) panel — click it and pick your
   reference file (or drag-drop).
2. **Load the DIGITIZED CSV** into the right (green) panel.
3. Make sure the **X column** and **Y column** boxes say `x` and `y`.
4. Click **Process & Compare.** It shows RMSE, correlation, R², bias, MAPE and
   more, plus plots: curve overlay, residuals, absolute error, and an outlier zoom.
5. **Export Comparison CSV** saves the aligned point-by-point comparison.

## Run from source

```bash
python3 -m pip install -r requirements.txt
python3 accuracytester_desktop.py
```

Load two CSV files (original vs digitized). Drag-and-drop works when `tkinterdnd2`
is installed; otherwise click the panels to browse for files.

## Score a whole folder (batch accuracy testing)

```bash
python3 accuracy_batch_cli.py --digitized-dir ~/Desktop/my_run/digitized_csvs --ground-truth-dir ~/Desktop/truth
```

It pairs files by **filename stem**, so `pilot_09_digitized_points.csv` matches
`pilot_09.csv` automatically. These suffixes are stripped when matching (longest
first): `_digitized_points`, `_ground_truth`, `_groundtruth`, `_digitized`,
`_points`, `_data`, `_gt`. Exact stem matches win; a tie is reported as
`ambiguous_match` and **never guessed**.

**Both CSVs need `x` and `y` column headers.** A bare two-column file with no
header row will not be read — add `x,y` as the first line, or pass `--x-col` /
`--y-col` with your real column names.

Options:

| Option | What it does | Default |
| --- | --- | --- |
| `--digitized-dir` | Folder of digitized CSVs. | required |
| `--ground-truth-dir` | Folder of ground-truth CSVs. | required |
| `--output-dir` *(`--out`, `-o`)* | Where the report goes. | `<digitized-dir>/accuracy_report` |
| `--x-col` / `--y-col` | Column names in both CSVs. | `x` / `y` |
| `--grid-mode` | Which x-values to score on: `original_x`, `digitized_x`, `common_uniform`. | `original_x` |
| `--grid-points` | Grid size for `common_uniform` (minimum 2). | `1000` |
| `--dup-policy` | How duplicate x-values collapse: `median`, `mean`, `first`. | `median` |
| `--color-slot` | Which color slot to use when a CSV holds several series. | first slot in numeric order |
| `--extra-suffix` | An extra filename suffix to strip when matching (repeatable). | — |
| `--no-default-suffixes` | Match on exact stems only. | off |

The defaults mirror the GUI, so batch and app results agree.

### Output

- **`accuracy_report.csv`** — one row per image: RMSE, correlation, MSE, R², MAE,
  median/p95/max absolute error, bias, MAPE/sMAPE/WAPE, `nrmse_range_pct`, the
  overlap range, `points_compared`, and a `status`.
- **`accuracy_summary.json`** — totals and the overall failure rate.

Two things to know when reading it:

- **`nrmse_range_pct`** (RMSE as a percentage of that figure's own y-range) is the
  number to quote — it makes figures with wildly different axis scales comparable.
- **Correlation and R² are undefined against a flat (zero-variance) reference.**
  The CSV still prints a huge number; read those cells as N/A. The RMSE on the
  same row is still meaningful.

Statuses: `ok`, `no_method_match` (truth file with nothing digitized matching it),
`no_ground_truth_match`, `invalid_data` (not scoreable as y=f(x), e.g. a vertical
line), `ambiguous_match`, `insufficient_overlap`, `parse_error`.

> The summary's **failure rate counts unmatched files**. Scoring 4 CSVs against 16
> ground truths reports 75% failure — that is a missing-file count, not a
> statement about accuracy. Read the per-row statuses before quoting it.

Full walkthrough, including the batch digitizer that produces the input folder:
see [Batch mode](../README.md#batch-mode--whole-folders-at-once) in the main README.

## Build the macOS app

macOS apps must be built on a Mac:

```bash
bash build_macos.sh
```

Output: `dist/AccuracyTester.app` (and `dist/AccuracyTester-macos.app.zip`) — a
windowed app you double-click to open. No Tesseract is needed for this tool.

## Tests

```bash
python3 -m pytest -q
```

## Folder contents

```text
AccuracyTesterPro.py        # The tool (Tkinter + matplotlib + pandas)
accuracytester_desktop.py   # Entry point
accuracy_core.py            # The statistics (RMSE, R2, correlation, ...)
accuracy_batch_cli.py       # Terminal CLI: score a whole folder
batch_scoring.py            # File pairing + per-image scoring engine
accuracytester_macos.spec   # PyInstaller spec (AccuracyTester.app)
build_macos.sh              # macOS build script
make_macos_icons.py         # Builds assets/accuracytester.icns from a source image
requirements.txt            # Python dependencies
version.json                # App name + version
assets/                     # Application icon source
```
