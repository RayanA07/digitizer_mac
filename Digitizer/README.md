# Data Digitizer 2.15 (macOS) — User Guide

## What is this?

**Data Digitizer** turns a *picture of a graph* into *numbers you can use*. You give it an image of a chart (a screenshot, a scan, a figure from a paper), and it reads the curve off the picture and hands you back a **spreadsheet-friendly table of data points** (a CSV file) plus an **overlay image** that shows you exactly which points it detected, drawn on top of your original graph. That way you can check its work at a glance.

There are **three ways to use it**:

- **The click-and-go app** — a normal macOS application. Double-click and follow the on-screen steps. No coding, nothing to install. **This is what most people want.**
- **The command line** — a one-line typed command for people who like terminals. This needs Python and the source files (see [Using the command line](#using-the-command-line)).
- **Batch mode** — point it at a *folder* and it digitizes every image inside, then scores the results against known-correct data. See [Batch mode](#batch-mode--whole-folders-at-once).

If you just want your data out, head to the [Quick start](#quick-start).

> **New to all this?** Don't worry about the technical words yet. Just follow [Quick start](#quick-start) and then [Using the app](#using-the-app-step-by-step) — every button is explained as you go. You can ignore the entire command-line half of this guide.

---

## Quick start

1. Go to the **[Releases page](https://github.com/RayanA07/digitizer_mac/releases/tag/v2.15)**. Scroll down until you see a heading called **Assets**, then click the file named **`Digitizer-macos.app.zip`** to download it. (See [Download & install](#download--install-no-python-needed) for exactly what that page looks like.)
2. **Double-click the downloaded zip** to unpack `Digitizer.app`, then **double-click `Digitizer.app`** to open it. On the very first run, macOS says the app is from an "unidentified developer" — **right-click** the app and choose **Open**, then **Open** again. This is normal and safe; the full explanation is in [Download & install](#the-first-run-macos-warning-expected).
3. In the app, work top to bottom: **Import** your graph image → set the **curve color** → run **Axis Detection** → run **Calibration** → **Place Points** → **Export** to CSV.

That's the whole flow. **Don't worry if those words mean nothing yet** — each one is explained, with exactly what to click, in [Using the app](#using-the-app-step-by-step) below.

---

## Download & install (no Python needed)

You do **not** need Python, and you do **not** need to install anything. The OCR engine (the part that reads the axis numbers) is already built into the app.

### Step 1 — Open the Releases page

Go to <https://github.com/RayanA07/digitizer_mac/releases/tag/v2.15>.

This is a GitHub *release page*. It shows a title and a description at the top. **Scroll down** past the description until you see a grey heading called **Assets** with a small triangle next to it. If the list under it looks collapsed, click the word **Assets** to open it.

### Step 2 — Download the program

In the **Assets** list, click the file named **`Digitizer-macos.app.zip`**. (Ignore the green **Source code (zip)** and **Source code (tar.gz)** links — you do not need those.)

Your browser will **download** the file. Safari usually unzips it automatically into a `Digitizer.app`; Chrome and Firefox leave the `.zip` for you to double-click.

> *Optional:* if you also want the accuracy-checking tool, download **`AccuracyTester-macos.app.zip`** the same way — see the [last section](#accuracy-tester-optional).

### Step 3 — Find the downloaded file

The file lands in your **Downloads** folder. To get there: open **Finder** (the smiling face icon in the Dock), then click **Downloads** in the left-hand sidebar.

If you only see `Digitizer-macos.app.zip`, double-click it to produce `Digitizer.app`. You can leave the app there, or drag it into **Applications** or onto your **Desktop**. There is nothing to "install" — the `.app` *is* the program.

### Step 4 — Launch it

**Double-click `Digitizer.app`** to open the app.

### The first-run macOS warning (expected)

The first time you run it, macOS Gatekeeper shows a dialog saying **"Digitizer.app" cannot be opened because it is from an unidentified developer.** This is **not** a virus warning. It appears because the app is not notarized with a paid Apple Developer ID, and macOS is cautious about any program it hasn't seen before.

To run it, use either method:

1. **Right-click** (or Control-click) `Digitizer.app` in Finder, choose **Open**, then click **Open** again in the dialog that appears, **or**
2. Open **System Settings → Privacy & Security**, scroll down to the message about the blocked app, and click **Open Anyway**. Then double-click the app again.

You'll only need to do this once.

> If macOS instead reports the app as **"damaged and can't be opened"**, the quarantine flag is set. Open **Terminal** (Applications → Utilities → Terminal) and run:
>
> ```bash
> xattr -dr com.apple.quarantine "$HOME/Downloads/Digitizer.app"
> ```
>
> then right-click → **Open** as above.

---

## Using the app (step by step)

When the app opens you'll see your future graph in the big main area, a floating **Cursor Zoom** panel in the top-right corner, and a **status bar** along the bottom. A few things to know up front:

- **The status bar is the thin strip along the very bottom edge of the window.** It shows a short message after every action — **watch it.** It confirms success or tells you why something didn't work. At the start it reads *"Load an image to begin."*
- **Cursor Zoom** is just a magnifying glass — it shows an enlarged view of whatever is under your mouse so you can click precisely. It's a helper only; it has nothing to do with exporting.
- **Import, Tools, Advanced, and Export are buttons along the top of the window.** Clicking one opens a small menu of choices. Throughout this guide, "open the **Tools** button → **Pick Color**" means: click **Tools** at the top, then click **Pick Color** in the menu that drops down.

Follow these steps in order.

### 1. Load your graph image

Click the **Import** button (top-left), then choose:

- **Import Image** — to pick a file from your computer (PNG, JPG, JPEG, BMP, TIF/TIFF), or
- **Paste Image** — to use a screenshot you've already copied to the clipboard (**⌘ + Control + Shift + 4** copies a screen selection on macOS).

Your chart appears in the main area. The app automatically guesses your curve's color and shows it as the first colored square in the **Selected color** row at the bottom of the window.

### 2. Confirm or set the curve color

Look at the auto-picked color square in the **Selected color** row (the strip of colored squares near the bottom).

- If it already matches your data line, **keep it** — you're done with this step.
- To set it yourself: open the **Tools** button, click **Pick Color** (your cursor becomes a crosshair), then click directly on the curve in the image. The color square updates, and Pick Color turns itself off.

> **Tracing more than one curve?** Click the small green **`+`** square in the Selected color row to add another color slot, select it, then use Pick Color again for that line. (Most people only have one curve and can skip this.)

### 3. Read the axis numbers automatically

Open the **Advanced** button → **Axis Scale Detection** submenu → click **Run Axis Detection**.

The app uses OCR (text recognition) to read the numbers printed along your axes and automatically fills in the four boxes in the **Min-Max Coordinates** panel: **X min, X max, Y min, Y max**. The same submenu also displays the detected values for reference.

### 4. Check and fix the axis numbers

Look at the four **Min-Max Coordinates** boxes. OCR is good but not perfect, so **always sanity-check them.** If any value is missing or misread, just **type the correct number into the box** yourself.

> These four values are required. Export will not run until all four boxes contain valid numbers.

### 5. Calibrate the plot box

This tells the app exactly where your plotted area sits in the image. Open **Tools → Calibration**, then choose one:

- **Coordinate-Mediated Calibration** *(recommended — easiest)* — run **Axis Detection** first (step 3), because this option uses those detected axis positions. It automatically snaps a **dashed green box** onto your plot area. **If you ran step 3, use this and you can skip manual calibration entirely.**
- **Manual Calibration** *(by hand)* — you click four ticks **directly on your chart image**. A **large green step-by-step banner** appears above the image and walks you through each click in order: **X MIN** (smallest X), **X MAX** (largest X), **Y MIN** (smallest Y), **Y MAX** (largest Y), telling you exactly which point to click at each step. You are clicking *locations on the picture*, not typing numbers. The points don't have to be in textbook positions — the box is built correctly from wherever you click, as long as **X MIN is left of X MAX** and **Y MIN is below Y MAX**.

Either way, you'll end up with a **dashed green box** (a rectangle drawn with a dashed green outline) marking the plotted region.

> If you pick Coordinate-Mediated Calibration without running Axis Detection first, the status bar will say *"Run Axis Scale Detection first."*

### 5a. Enhanced Human Click (optional, for manual calibration)

Human clicks miss by about **0.9 px** on average. **Tools → Calibration → Enhanced Human Click** (a checkbox) fixes that: while you are doing **Manual Calibration**, every click is snapped onto the exact centre of the nearest crosshair, corner, or axis line.

- Turn it on **before** you start Manual Calibration. It's **off by default** and affects manual calibration clicks only — it does nothing to Place Points or to Coordinate-Mediated Calibration.
- After each click the status bar reports what happened, e.g. *"Enhanced click: corner found, corrected by 1.4 px. ⌘Z to undo."*
- **⌘Z undoes the last calibration click** (snapped or not) and steps the banner back, so you can retry it.
- **Tools → Calibration → Enhanced Click Settings…** has a slider for how far a click may be moved. If the status bar says a feature was *N px away (limit …)*, raise the slider above N, press **⌘Z**, and click again — the new limit applies immediately, with no need to restart calibration.

### 6. Adjust the box if needed (optional)

If the dashed green box edges don't line up exactly with your axes, hover over an edge until the cursor becomes a **resize arrow**, then **drag** it into place. The app remembers your adjusted box for export.

### 7. Extract the data points

Open **Tools → Place Points → Run**.

The app scans the image for your chosen color and overlays the detected points on the curve. The **status bar tells you how many points were placed.**

> **Stray text or a legend getting picked up as data?** Use the optional **Masking** tools first. Under **Advanced → Masking** you can blank out words, numbers, or a legend, or hand-draw mask rectangles (Manual Mask Mode), so they aren't mistaken for your curve. Do this *before* Place Points. There's also a **Clear Masks** option to undo them.

### 8. Choose which colors to export (only for multiple curves)

If you traced more than one curve: open the **Export** button → **Colors to Export** submenu, and tick the color slots you want (or choose **Active Color Only** / **All Configured Colors**). **With a single curve this is already handled for you** — skip it.

### 9. Export your data

Open the **Export** button and choose:

- **Export CSV → Raw values** — a plain text spreadsheet file that opens in Numbers, Excel, Google Sheets, Python, etc.
- **Export Excel → Raw values** — a real Excel `.xlsx` workbook.

A standard macOS **Save** dialog appears. **Note which folder is shown at the top** (Downloads or Desktop are easy choices so you can find it again), keep the suggested name **`digitized_points.csv`**, and click **Save**.

**That's it — you now have a spreadsheet of your graph's data.** To open it, go to the folder you just saved into and **double-click the CSV file**; it opens in Numbers (or Excel) by default, where you'll see your X and Y columns.

### Where your files go

Exports go **wherever you choose in the Save dialog** — they are not forced into a fixed folder, so make a note of the location you pick. The app suggests the filename **`digitized_points.csv`** (or **`digitized_points.xlsx`** for Excel) and forces the correct extension.

Each row in the file is one detected point, with these columns:

| Column | Meaning |
| --- | --- |
| `color_slot` | which color slot the point belongs to (1 for a single curve) |
| `color_r`, `color_g`, `color_b` | the curve's color (0–255 each) |
| `x`, `y` | the real-world data values |
| `x_px`, `y_px` | the original pixel position in the image |

The CSV is saved as UTF-8, with one header row followed by one row per point.

> **Excel export needs a helper library** (`openpyxl`). In the prebuilt app it's already included. If you're running from source and it's missing, the status bar will say so and nothing is saved — use CSV instead, or install it (see [Run from source](#run-from-source-for-developers)).

### Two things that block export (and how the app tells you)

Export will **quietly refuse** and show a status message unless **both** of these are true:

1. **The four Min-Max Coordinate boxes contain valid numbers** — otherwise you'll see *"Export requires X/Y min/max values."*
2. **A calibration has been run** (the dashed green box exists) — otherwise you'll see *"Export requires calibration."*

If either message appears, glance at the status bar, go back, and finish that step.

### Log-scale axes (optional)

Most plots are linear, so leave this alone for a normal graph — but if your graph uses a **logarithmic** X or Y axis, turn it on with the small **log** toggle buttons that sit just to the **right of the Min-Max Coordinates boxes** (one on the X-min/X-max row, one on the Y-min/Y-max row):

- Click the **log** button beside the X boxes and/or the one beside the Y boxes. It turns **green** when it's on.
- Calibrate and enter the axis min/max **as the real numbers printed on the axis** (e.g. `1` and `1000`), exactly as you would for a linear plot.
- On export, that axis is interpolated in log space, so the values come out correct for a log scale. Leave the buttons off (grey) for normal linear axes.

> A log axis needs **positive** min/max values (you can't take the log of zero or a negative number). If a value is zero or negative, export will tell you instead of producing wrong numbers.

### Tips for the best results

- A **clean, distinctly-colored curve** works best. Point extraction matches your selected color within a tolerance and takes the vertical midpoint of matching pixels in each column.
- **Loading a new image resets everything** — points, color slots, calibration, and the coordinate boxes. Finish one image before loading the next.
- If **Axis Detection** ever says Tesseract OCR isn't available, just **type the four axis values in by hand** (step 4) — everything else still works.
- Stuck on an error? **Advanced → Error Log** opens a window of recent errors.

---

# For developers

> **Using the click-and-go app? You can stop here.** Everything below is the optional command-line and build-from-source material for people comfortable with a terminal. If you just want your data, you're already done — see [Troubleshooting](#troubleshooting) if anything went wrong.

## Using the command line

> ### ⚠️ Read this first — the `.app` is NOT the command line
>
> The **`Digitizer.app`** you downloaded is the **graphical app**. It does **not**
> contain `digitizer.py`, and you **cannot run command-line commands inside it**.
>
> If you open a terminal *inside* the app and try the CLI, e.g.:
>
> ```bash
> cd /Applications/Digitizer.app
> python3 digitizer.py 'digitizer_cli(pic_dir="...")'
> ```
>
> you will get exactly this error — and it is **not a bug**:
>
> ```text
> python3: can't open file '/Applications/Digitizer.app/digitizer.py': [Errno 2] No such file or directory
> ```
>
> The command line is a **separate** way to use the tool that runs from the **source
> code** (the project files), with Python — not from the `.app`. The `.app` always just
> opens the graphical window and ignores any command-line options.
>
> **Most people don't need the command line at all — just double-click `Digitizer.app`.**
> Only follow the steps below if you specifically want to script/batch from the terminal.

### Set up the command line from scratch (one time, ~5 minutes)

You need three things the `.app` alone doesn't give you: **Python**, **Tesseract** (the OCR
engine), and the **source code**. Open **Terminal** (press **⌘ + Space**, type
`Terminal`, press **Enter**) and do this:

**1. Make sure you have Python 3.** Run `python3 --version`. If it prints a version
(e.g. `Python 3.13.x`) you're set. If it says *command not found*, install it from
<https://python.org> (or `brew install python`), then reopen Terminal.

**2. Install Homebrew** (a package manager — skip if `brew --version` already works):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow its prompts, then **close and reopen Terminal**.

**3. Install Tesseract** (so OCR axis-detection works from source):

```bash
brew install tesseract
```

**4. Download the source code.** The app is not enough — get the project files. Easiest
way, no git needed:

  1. Open **<https://github.com/RayanA07/digitizer_mac>** in your browser.
  2. Click the green **`<> Code`** button → **Download ZIP**.
  3. Open your **Downloads** folder and **double-click the ZIP** to unzip it. You'll get a
     folder named **`digitizer_mac-main`**.

  *(If you prefer git: `git clone https://github.com/RayanA07/digitizer_mac.git`.)*

**5. Go into the `Digitizer` folder** — the one that actually contains `digitizer.py`
(inside `digitizer_mac-main`, **not** the `.app`):

```bash
cd ~/Downloads/digitizer_mac-main/Digitizer
```

Confirm you're in the right place — this must list the file:

```bash
ls digitizer.py
```

If that says *No such file or directory*, you're in the wrong folder. You must be in the
**source** `Digitizer` folder — not `Digitizer.app`, and not `digitizer_mac-main` itself.

**6. Install the Python libraries** (one time):

```bash
python3 -m pip install -r requirements.txt
```

You're done setting up. Stay in this `Digitizer` folder and run the commands below. For
example, to digitize an image (use your own file's full path):

```bash
python3 digitizer.py ~/Downloads/pilot_04.png
```

or the function-call form:

```bash
python3 digitizer.py 'digitizer_cli(pic_dir="/Users/you/Downloads/pilot_04.png")'
```

### Open a terminal in the Digitizer folder (shortcut for next time)

Once you have the source, instead of typing `cd` each time you can:

1. Open **Finder** and find the **`Digitizer`** source folder (the one with `digitizer.py`).
2. **Right-click** (or Control-click) the folder.
3. Choose **New Terminal at Folder**. (If you don't see it, enable **System Settings → Keyboard → Keyboard Shortcuts → Services → "New Terminal at Folder"**.)

A Terminal window opens, already pointed at the right folder. Type your commands there.

> The examples below use the placeholder image name **`graph.png`**. Substitute the real name of your own image file. The image must be either in the folder the terminal is pointed at, or in your Downloads folder, or you must give its full path in quotes.

### The simplest command

Give it an image. That's it:

```bash
python3 digitizer.py graph.png
```

With nothing else, the app automatically:

1. **detects the curve color**,
2. **detects the axes and tick positions** with OCR (so it reads X min / X max / Y min / Y max straight off the image), and
3. **writes a CSV of data points plus an overlay PNG** to your **Downloads** folder.

A bare filename like `graph.png` is looked up first in the current folder, then in your Downloads folder — so the one-liner works as long as the image is in either place. By default it stays quiet: it prints just a success line and the output folder. Add **`--verbose 1`** to see the full detail — the color, pixel coordinates, the OCR readings, the point count, and the **OCR confidence score** (see [Seeing more detail](#seeing-more-detail---verbose)).

> Two other spellings do exactly the same thing: `python3 digitizer_2_11.py cli graph.png` and `python3 digitizer_2_11.py digitize graph.png`.

### Options

Add any of these to the command for more control:

| Option (aliases) | What it does | Default |
| --- | --- | --- |
| `pic_path` *(positional)* | Path to the image. A bare filename is searched in the current folder, then Downloads. Either this **or** `--pic-dir` is required. | none (required) |
| `--pic-dir` | Another way to give the image path. If both are given, `--pic-dir` wins. | none |
| `--color R,G,B` | Curve color, e.g. `255,0,0` (each part 0–255). Also accepts `[r,g,b]`. **Must match your curve's actual color**, or the run finds no points. | auto-detected |
| `--axis-values` *(`--axis`)* | Axis numbers as `xmin,xmax,ymin,ymax`. X min must differ from X max, and Y min from Y max. | read by OCR |
| `--ticks` *(`--tick-setting`, `--tick-coordinates`)* | Four tick pixel points in `x_min,x_max,y_min,y_max` order, e.g. `[10,200],[500,200],[10,200],[10,20]`. | found by OCR |
| `--log-x` | Read the X axis in base-10 **log** space (X min/max must be positive). Mirrors the GUI's **log** toggle. | off (linear) |
| `--log-y` | Read the Y axis in base-10 **log** space (Y min/max must be positive). Mirrors the GUI's **log** toggle. | off (linear) |
| `--output-dir` *(`--out`, `-o`)* | Folder to save into. Created if it doesn't exist. | your Downloads folder |
| `--verbose N` *(`-v`)* | How much to print. `1` (or a bare `-v` / `--verbose`) shows the color, pixel coords, tick→OCR values, point count, and OCR confidence, and writes a `<image>_log.txt`. `0` prints only success + the output folder. | `0` (quiet) |
| `--json` | Print the result details as JSON instead of plain text. | off |
| `-h` / `--help` | Show the usage help and exit. | — |
| `--normalize-y` *(optional extra)* | Adds an extra `y_norm` column (Y rescaled to 0–1 over the axis range). Leave it off for normal use. | off |
| `--limit-to-calibration` *(optional extra)* | Export **only** points inside the calibration box. **Off by default** since 2.14: if OCR reads an extreme tick slightly short, the box would otherwise clip real data off the ends of the curve. | off |
| `--no-limit-to-calibration` *(optional extra)* | Also export points that fall outside the calibration box. This is **already the default**; the flag is kept so older scripts keep working. | (the default) |

### The "fill-in-the-blank" template and function-call style

If you'd like a copy-and-edit reference, run:

```bash
python3 digitizer.py template
```

This **prints a fill-in-the-blank line** (it does **not** digitize anything). It shows a minimal example, a full example listing every option, and a short legend explaining each value.

You can then run that **function-call form** — one quoted line. Wrap the whole `digitizer_cli(...)` call in **single quotes** so the inner double quotes survive.

**Minimal example** (just the image; everything else auto-detected). This is the form to copy first:

```bash
python3 digitizer.py 'digitizer_cli(pic_dir="graph.png")'
```

**Full example** — the `color`, `axis_values`, and `tick_setting` values below are **placeholders you must edit to match your own chart.** A leftover `color=(255,0,0)` (red) on a non-red curve finds no points and exits with *"produced no points."* Either delete the options you don't need (so those values auto-detect) or replace them with your real values:

```bash
python3 digitizer.py 'digitizer_cli(pic_dir="graph.png", color=(255,0,0), axis_values=(0,10,0,100), tick_setting=([10,200],[500,200],[10,200],[10,20]), log_x=False, log_y=False, output_dir="/Users/you/Downloads/out", verbose=1, json=False, normalize_y=False, limit_to_calibration=False)'
```

The values you can put inside `digitizer_cli(...)`:

| Name (aliases) | What it is | Default |
| --- | --- | --- |
| `pic_dir` *(`pic_path`, `plot_location`, `image`, `image_path`)* | **Required.** The image path; a bare filename is looked up in the current folder, then Downloads. | none (required) |
| `color` *(`rgb`, `color_rgb`)* | Curve color as `(R,G,B)` or `"255,0,0"`. Blank = auto-detect. Must match your curve's real color. | auto-detected |
| `tick_setting` *(`ticks`, `tick_coordinates`, `tick_coordinate`)* | Four tick pixel points in `x_min,x_max,y_min,y_max` order. Blank = OCR. | OCR-detected |
| `axis_values` *(`axis`, `bounds`)* | Axis numbers as `(xmin,xmax,ymin,ymax)`. Blank = OCR. | OCR-detected |
| `log_x` *(`logx`, `x_log`)* | `True` reads the X axis in base-10 log space (X min/max must be positive). | False |
| `log_y` *(`logy`, `y_log`)* | `True` reads the Y axis in base-10 log space (Y min/max must be positive). | False |
| `output_dir` *(`out_dir`, `out`)* | Folder to save into. Blank = Downloads. | Downloads |
| `verbose` *(`v`)* | `1` prints full detail and writes a `<image>_log.txt`; `0` stays quiet. | `0` |
| `json` *(`as_json`, `print_json`)* | `True` prints full details as JSON. **Only accepted in this function-call form** (the flag version is `--json`). | False |
| `normalize_y` *(`normalize`)* — *optional extra* | `True` adds the `y_norm` (0–1) column. Leave off for normal use. | False |
| `limit_to_calibration` *(`limit`)* — *optional extra* | `True` keeps only points inside the calibration window. | False |

Arguments can be **positional** in the order `pic_dir, color, tick_setting, axis_values, output_dir`, or by **name** using any alias above. Empty positions are allowed and fall back to defaults, and the words `none` / `null` / blank are treated as "auto".

### Worked examples

Auto-detect everything (color and axes), save to Downloads — **the safest example to copy as-is**:

```bash
python3 digitizer.py graph.png
```

Set the axis values yourself but still auto-detect the color:

```bash
python3 digitizer.py graph.png --axis 0,10,0,100
```

Force a specific curve color — **change `130,5,255` to your curve's real R,G,B**; a color that doesn't match the curve produces no points:

```bash
python3 digitizer.py graph.png --color 130,5,255 --axis 0,10,0,100
```

Use a full path, choose an output folder, and read the Y axis on a **log scale**:

```bash
python3 digitizer.py "/Users/you/Pictures/graph.png" --out "/Users/you/Desktop/out" --log-y
```

See everything the run worked out — color, pixel coordinates, the tick→OCR values, point count, and the **OCR confidence score** — and drop a `log.txt` alongside the output:

```bash
python3 digitizer.py graph.png --verbose 1
```

> **Tip:** There's also an interactive wizard that asks for each field one at a time. Start it with `python3 digitizer_2_11.py interactive` (or `wizard`).

### Seeing more detail (`--verbose`)

By default the command line is **quiet** — it just confirms success and tells you the output folder. When you want to see (or keep a record of) exactly what the tool did, raise the verbosity:

```bash
python3 digitizer.py graph.png --verbose 1
```

At level `1` it prints, and the run also writes a `<image>_log.txt`, the following:

- **color (r,g,b)** — the curve color it used.
- **pixel coords** — where the four axis ticks sit in the image, in pixels.
- **tick → values** — the four axis numbers (X min, X max, Y min, Y max) the tool used, and whether it read them automatically or you typed them in.
- **OCR confidence** — how sure the built-in number-reader (Tesseract) was about the axis numbers it read off your image, as a percentage. A low number is a hint to double-check the numbers, or to type them in yourself with `--axis`. Shows **n/a** only when you supply *both* the axis values **and** the tick pixel coordinates yourself (so no reading is done); if you pass `--axis` but let the tick positions auto-detect, the reader still runs and a percentage is shown.
- **num points** — how many data points were extracted.
- **elapsed (s)** — how long the run took, in seconds.

Level `0` (the default) stays quiet; you can also write just `--verbose` or `-v` as shorthand for level `1`.

### Output files

Every run writes two files (named after your image), plus a third at `--verbose 1`:

- **`<imageName>_digitized_points.csv`** — the table of digitized points.
- **`<imageName>_digitized_overlay.png`** — a copy of your image with the calibration box, the OCR axis-detection rectangles, and the detected points drawn on top (in the inverse of the curve color, so they stand out).
- **`<imageName>_log.txt`** — *(only with `--verbose 1`)* a plain-text record of the run: time, color, pixel coords, tick→OCR values, point count, OCR confidence, and the output paths.

The CSV columns:

| Column | Meaning |
| --- | --- |
| `color_slot` | 1-based color slot number (1 for a single-color run). |
| `color_r` | Red component (0–255) of the curve color. |
| `color_g` | Green component (0–255) of the curve color. |
| `color_b` | Blue component (0–255) of the curve color. |
| `x` | Digitized X value in data coordinates (rounded to 6 decimals). |
| `y` | Digitized Y value in data coordinates (rounded to 6 decimals). |
| `x_px` | Raw X pixel position in the image. |
| `y_px` | Raw Y pixel position in the image. |
| `y_norm` | *Only when `--normalize-y` is on.* Y rescaled to 0–1 over the axis range; appended as the last column (rounded to 6 decimals). |

---

# Batch mode — whole folders at once

Everything above handles one image. This chapter does two things at scale:

1. **Batch digitize** — point the tool at a *folder* of chart images and it digitizes every one.
2. **Batch accuracy test** — score all those results against known-correct ("ground truth") data in one command, and get a table of RMSE / R² / correlation per image.

Both run from the same source folder you set up in [Set up the command line from scratch](#set-up-the-command-line-from-scratch-one-time-5-minutes). Neither needs the `.app`.

A folder of images to try this on ships with the Windows repo under `Pilot/`; any folder of your own chart images works exactly the same way.

## A1 — Digitize a WHOLE FOLDER of images

From the **`Digitizer`** source folder:

```bash
python3 digitizer.py ~/Downloads/charts --output-dir ~/Desktop/my_run
```

- Give it a **folder** and it digitizes every image inside; give it a single **file** and it does just that one. Both go through the same command.
- `--output-dir` says where results go. Leave it off and results land **inside** the input folder instead.
- Supported image types: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.tif`, `.tiff`. Anything else in the folder is reported as *skipped*, not treated as a failure.
- **One bad file never stops the run.** A corrupt image, a photo that isn't a plot, or an OCR failure is recorded in the report and the batch moves on to the next file.

`python3 digitizer_batch_cli.py ~/Downloads/charts` and `python3 digitizer.py batch ~/Downloads/charts` are the same command by other names.

## A2 — What you get

Inside `my_run/` you'll find **two subfolders plus a report**:

```text
my_run/
    digitized_csvs/       one <image>_digitized_points.csv per image  (the data)
    digitized_overlays/   one <image>_digitized_overlay.png per image (points drawn on the chart — EYEBALL THESE)
    batch_report.csv      per-image: ok / failed / skipped, point count, reason
    batch_report.json     the same, plus totals and the overall failure rate
```

Open a few overlays in `digitized_overlays/` — if the coloured dots sit on the curve, that image digitized well. This eyeball check catches more problems in ten seconds than any metric.

`batch_report.csv` columns: `image`, `status`, `points`, `csv`, `overlay`, `elapsed_seconds`, `reason`.

## A3 — Batch options

Every option here applies to **every image in the folder**, so only set the ones your whole batch shares:

| Option | What it does | Default |
| --- | --- | --- |
| `input_dir` *(positional)* or `--input-dir` | The folder of images. | required |
| `--output-dir` *(`--out`, `-o`)* | Where results go. | inside the input folder |
| `--color R,G,B` | One curve color for every image. | per-image auto-pick |
| `--axis-values` *(`--axis`)* | One `xmin,xmax,ymin,ymax` for every image. | per-image OCR |
| `--ticks` | Four tick pixel points for every image (only sensible when all images share a layout). | per-image OCR |
| `--log-x` / `--log-y` | Treat that axis as base-10 logarithmic on every image. | off |
| `--verbose N` *(`-v`)* | At `1`, each image also gets a `<stem>_log.txt`. | `0` |
| `--normalize-y` | Add a `y_norm` column to each CSV. | off |
| `--limit-to-calibration` | Keep only points inside the calibration box. | off |

## A4 — When an image comes out wrong, help it

Two things break automatic mode, and both have a one-line fix:

- **Wrong colour picked** (it grabbed gridlines, or nothing). Tell it the curve colour as R,G,B — `0,0,0` for a black trace:

  ```bash
  python3 digitizer.py ~/Downloads/charts/corundum.png --color 0,0,0
  ```

- **Wrong axis numbers** (OCR misread them). Give the real axis min/max as `xmin,xmax,ymin,ymax`:

  ```bash
  python3 digitizer.py ~/Downloads/charts/corundum.png --axis 200,1600,0.2,1
  ```

  **These are the values of the four ticks it locked onto — not the range of your data.** Run with `--verbose 1` first and read the `tick -> values` line; whatever pixels it picked, your numbers must describe *those* ticks. If the y-min tick it used is the `0.2` gridline, then `...,0.2,1` is right and `...,0,1` would silently skew every y value by claiming that tick means zero.

Dropped minus signs and superscript/power-of-ten axis labels are the known OCR weak spots — those are the figures where `--axis` earns its keep.

## B1 — Score the results against the TRUE data (batch accuracy testing)

This is the part that tells you *how good* the digitization actually was. It compares every digitized CSV to a ground-truth CSV **by matching file names**, using the Accuracy Tester's exact statistics.

Change into the **`AccuracyTester`** folder and run:

```bash
cd ~/Downloads/digitizer_mac-main/AccuracyTester
python3 accuracy_batch_cli.py --digitized-dir ~/Desktop/my_run/digitized_csvs --ground-truth-dir ~/Desktop/truth
```

That's the whole command. `--digitized-dir` is the `digitized_csvs/` folder the batch digitizer just wrote; `--ground-truth-dir` is your folder of known-correct CSVs.

**Your ground-truth CSVs need an `x` and a `y` column header.** A bare two-column file with no header row will not be read — add `x,y` as the first line. (Use `--x-col` / `--y-col` if your columns are named something else.)

### How files are paired

Files pair up by **filename stem**, so `pilot_09_digitized_points.csv` matches `pilot_09.csv` automatically. These suffixes are stripped when matching (longest first):

`_digitized_points`, `_ground_truth`, `_groundtruth`, `_digitized`, `_points`, `_data`, `_gt`

Exact stem matches win over suffix-stripped ones. If several files match equally well, that is reported as `ambiguous_match` and **never guessed**. Add your own suffix with `--extra-suffix` (repeatable), or turn the built-in list off with `--no-default-suffixes`.

### Options

| Option | What it does | Default |
| --- | --- | --- |
| `--digitized-dir` | Folder of digitized CSVs. | required |
| `--ground-truth-dir` | Folder of ground-truth CSVs. | required |
| `--output-dir` *(`--out`, `-o`)* | Where the report goes. | `<digitized-dir>/accuracy_report` |
| `--x-col` / `--y-col` | Column names in **both** CSVs. | `x` / `y` |
| `--grid-mode` | Which x-values to score on: `original_x` (at the ground-truth x-values), `digitized_x`, or `common_uniform`. | `original_x` |
| `--grid-points` | Grid size for `common_uniform` (minimum 2). | `1000` |
| `--dup-policy` | How duplicate x-values collapse: `median`, `mean`, or `first`. | `median` |
| `--color-slot` | Which color slot to use when a CSV holds several series. | first slot in numeric order (noted in the report) |
| `--extra-suffix` | An extra filename suffix to strip when matching (repeatable). | — |
| `--no-default-suffixes` | Match on exact stems only (plus any `--extra-suffix`). | off |

The defaults mirror the Accuracy Tester GUI exactly, so the batch numbers and the app's numbers agree.

## B2 — Read the accuracy report

It writes an `accuracy_report/` folder next to the digitized CSVs:

- **`accuracy_report.csv`** — one row per image: the name, then **RMSE, correlation, MSE, R²**, MAE, median/p95/max absolute error, bias, MAPE/sMAPE/WAPE, the overlap range, the number of points compared, and a `status`. Lower RMSE = closer to truth.
- **`accuracy_summary.json`** — the totals and the overall **failure rate**.

Three columns worth knowing:

- **`nrmse_range_pct`** — RMSE as a percentage of that figure's own y-range. **This is the number to quote.** A raw RMSE of 63.9 and one of 0.026 are about equally accurate if their axes differ by 1000×; the normalized number makes them comparable.
- **`points_compared`** — how many x-positions were actually scored. A small number here means the two curves barely overlap, and the metrics describe only that slice.
- **correlation / R² on a flat line** — **undefined**, because both divide by the variance of the ground truth, which is zero for a horizontal reference. The CSV still prints something (e.g. `-2.6e+25`). Read those as **N/A**, not as an accuracy. The RMSE on the same row is still meaningful.

Statuses you may see:

| Status | Means |
| --- | --- |
| `ok` | scored; metrics present |
| `no_method_match` | a truth file exists but nothing digitized matched it — the image failed to digitize |
| `no_ground_truth_match` | a digitized file whose name matches no truth file |
| `invalid_data` | can't be scored as y=f(x) — e.g. a vertical line |
| `ambiguous_match` | several files matched equally well; reported, never guessed |
| `insufficient_overlap` | the two curves share too little x-range to score |
| `parse_error` | the CSV couldn't be read |

> **The headline "failure rate" counts unmatched files too.** If you score 4 digitized CSVs against a folder of 16 ground truths, the other 12 are reported as unmatched and the summary reads *75% failure* — that is a **missing-file** count, not a statement about digitizing quality. Look at the per-row statuses before quoting that number.

## B3 — A complete worked run

Start to finish, from the unzipped source folder:

```bash
cd ~/Downloads/digitizer_mac-main/Digitizer
python3 digitizer.py ~/Downloads/charts --output-dir ~/Desktop/my_run
cd ../AccuracyTester
python3 accuracy_batch_cli.py --digitized-dir ~/Desktop/my_run/digitized_csvs --ground-truth-dir ~/Desktop/truth
```

The second command prints a summary line like:

```text
Scored 4/16 images ok; 0 failed, 0 ambiguous, 12 unmatched (failure rate 75.0%).
Report  -> /Users/you/Desktop/my_run/digitized_csvs/accuracy_report/accuracy_report.csv
Summary -> /Users/you/Desktop/my_run/digitized_csvs/accuracy_report/accuracy_summary.json
```

Open `accuracy_report.csv` in Numbers or Excel and sort by `nrmse_range_pct` to see which figures digitized well and which need a `--color` or `--axis` hint.

> **Comparing two tools?** Score each tool's output folder against the *same* ground-truth folder and compare the `nrmse_range_pct` column image by image. Because both runs use the same grid mode, duplicate policy and statistics, the numbers are directly comparable.

## B4 — The two-file GUI version

The Accuracy Tester app compares **two files at a time**, which is the right tool when you want to *look* at one comparison rather than tabulate many:

1. Double-click **`AccuracyTester.app`**.
2. **Load the ORIGINAL CSV** into the left (blue) panel — click it and pick your ground-truth file (or drag-drop).
3. **Load the DIGITIZED CSV** into the right (green) panel.
4. Make sure the **X column** and **Y column** boxes say `x` and `y`.
5. Click **Process & Compare.** It shows RMSE, correlation, R², bias, MAPE and more, plus plots: curve overlay, residuals, absolute error, and an outlier zoom.
6. **Export Comparison CSV** saves the aligned point-by-point comparison.

Use `accuracy_batch_cli.py` (above) to score a whole folder at once.

---

## Run from source (for developers)

You'll need a **recent Python 3** installed (from <https://python.org>, or via Homebrew with `brew install python`).

1. Get the source code — download it from the [repo](https://github.com/RayanA07/digitizer_mac) or clone it:

   ```bash
   git clone https://github.com/RayanA07/digitizer_mac.git
   ```

2. Open a terminal in the `Digitizer` folder and install the dependencies:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. For OCR features (axis detection, masking) when running from source, install Tesseract:

   ```bash
   brew install tesseract
   ```

   *(The prebuilt `Digitizer.app` bundles Tesseract, so this step is only needed when running from source.)*

4. Launch the graphical app:

   ```bash
   python3 digitizer_2_11.py
   ```

The command-line interface ([above](#using-the-command-line)) also runs from this same source setup.

The dependencies are: `PyInstaller` (for building the app), `PyQt6` (the window), `numpy`, `pillow` (image handling), `pytesseract` (OCR), and `openpyxl` (Excel export).

### Running the tests

```bash
cd Digitizer        && python3 -m pytest -q
cd ../AccuracyTester && python3 -m pytest -q
```

---

## Build pipeline — turning the code into an app

The project is plain Python (a PyQt6 GUI plus a small CLI). There are three "shapes" you can run it as, and the conversion is the same idea each time — **[PyInstaller](https://pyinstaller.org)** bundles the Python interpreter, this code, and the dependencies into one self-contained program described by a `.spec` file:

| Target | What it is | How it's made |
| --- | --- | --- |
| **CLI** | `python3 digitizer.py …` | No build needed — it runs straight from the source files with Python (see [Run from source](#run-from-source-for-developers)). |
| **macOS `.app`** | a `Digitizer.app` bundle you double-click | PyInstaller reads `digitizer_macos.spec`, bundles the GUI entry `digitizer_desktop.py` **and** the Tesseract OCR runtime in `vendor/tesseract`, and writes `dist/Digitizer.app`. |
| **Windows `.exe`** | a one-file `Digitizer.exe` | Same tool, the Windows spec/scripts in the separate **[DataDigitizer](https://github.com/aj24by7/DataDigitizer)** repo (`.\build_windows.ps1`) produce `dist\Digitizer.exe`. |

### Starter command (macOS)

macOS apps must be built **on a Mac**. From the `Digitizer` source folder, with Homebrew installed:

```bash
python3 -m pip install -r requirements.txt
bash build_macos.sh
```

The script installs dependencies, generates the icon, vendors a self-contained Tesseract runtime into `vendor/tesseract`, runs PyInstaller, ad-hoc signs the bundle, and zips it. The result is **`dist/Digitizer.app`** (and `dist/Digitizer-macos.app.zip`) — a windowed app you can double-click. The **Tesseract OCR runtime** is **bundled into the app**, so OCR features (axis-value detection and the text/number/legend masking tools) work without anyone needing a separate Tesseract install.

Build the Accuracy Tester the same way from its own folder (`cd AccuracyTester && bash build_macos.sh`).

> The `Build macOS 2.15` GitHub Actions workflow builds both apps on the `macos-26` (Tahoe) runner, runs the test suites and a CLI + batch-accuracy smoke test, and uploads the zips. Pushing a tag like `v2.15` publishes a GitHub Release named **Data Digitizer 2.15 (macOS)** with both `.app` zips attached.

---

## Troubleshooting

**macOS says the app is from an "unidentified developer" or is "damaged."**
Expected on the first run — the app just isn't notarized. Right-click → **Open** → **Open**, or use **System Settings → Privacy & Security → Open Anyway**. If it says "damaged", clear quarantine with `xattr -dr com.apple.quarantine "$HOME/Downloads/Digitizer.app"`. (Full explanation in [Download & install](#the-first-run-macos-warning-expected).)

**I can't find `Digitizer.app` after downloading it.**
It's in your **Downloads** folder. Open **Finder** and click **Downloads** in the sidebar. If you only see the `.zip`, double-click it to unpack the app.

**`can't open file '/Applications/Digitizer.app/digitizer.py': No such file or directory`** (or any `digitizer.py` "No such file" error).
You're trying to run the command line from **inside the `.app`** — but the `.app` is the graphical program and doesn't contain `digitizer.py`. The CLI runs from the **source code**, which is a separate download. Follow [Set up the command line from scratch](#set-up-the-command-line-from-scratch-one-time-5-minutes), then run the command from the **source `Digitizer` folder** (the one where `ls digitizer.py` succeeds) — not from `Digitizer.app`. If you only want to digitize without the terminal, just double-click `Digitizer.app`.

**"`python3: command not found`" in the terminal.**
Python isn't installed. Install it from <https://python.org> or run `brew install python`, then open a fresh terminal and try again. (Reminder: the command line needs Python; the `.app` does not.)

**"Tesseract OCR executable not found" when running from source.**
Install it with `brew install tesseract`, then reopen Terminal. You can also point at a specific binary with `export TESSERACT_CMD=/opt/homebrew/bin/tesseract`. The prebuilt `.app` bundles its own copy and never needs this.

**It picked the wrong curve color.**
- *In the app:* use **Tools → Pick Color** and click your curve (step 2).
- *On the command line:* pass it yourself, e.g. `--color 130,5,255` (flags) or `color=(130,5,255)` (function-call form) — using your curve's real R,G,B.

**The command line says "produced no points" / exits without a CSV.**
The color it's matching doesn't match your curve. If you passed `--color` (or `color=`), the values are wrong — fix them, or drop the option entirely to let it auto-detect. The placeholder `255,0,0` (red) in the template will fail on any non-red plot.

**The axis numbers came out wrong.**
OCR can misread numbers. Always check them.
- *In the app:* type the correct value into the **Min-Max Coordinates** box.
- *On the command line:* give them with `--axis xmin,xmax,ymin,ymax` (flags) or `axis_values=(xmin,xmax,ymin,ymax)` (function-call form). Run with `--verbose 1` to see the **OCR confidence score** — a low number is a strong hint that you should type the axis values in yourself with `--axis`.

**"Image file not found" on the command line.**
Put the image in your **Downloads** folder or in the folder the terminal is pointed at (a bare filename is searched in both), or pass the **full path in quotes**, e.g. `python3 digitizer.py "/Users/you/Pictures/graph.png"`.

**Export does nothing in the app.**
Check the status bar (the thin strip at the bottom). You need **all four Min-Max Coordinate boxes filled** *and* **a calibration run** (the dashed green box). Finish whichever is missing, then export again.

**The batch accuracy report says every row is `no_ground_truth_match`.**
The filenames don't line up. Pairing is by filename stem after stripping a known suffix — `pilot_09_digitized_points.csv` matches `pilot_09.csv`, but `run3.csv` matches nothing called `pilot_09.csv`. Rename one side, or pass your own suffix with `--extra-suffix`.

**The batch accuracy report can't read my ground-truth CSVs.**
They need a header row naming the columns — `x,y` as the first line. Files exported by other digitizers are often bare two-column data with no header; add one, or pass `--x-col` / `--y-col` with your real column names.

**Where did my files go?**
- *In the app:* wherever you chose in the **Save** dialog.
- *On the command line:* your **Downloads** folder by default, or the folder you set with `--out` / `output_dir=`.
- *In batch mode:* inside `--output-dir`, split into `digitized_csvs/` and `digitized_overlays/`.

---

## Folder contents

This repository mirrors the Windows 2.15 layout, adapted for macOS:

```text
README.md                          # This guide (root)
CHANGELOG.md                       # Version history
RELEASE_NOTES.md                   # macOS release notes
.github/workflows/build-macos.yml  # CI: tests, smoke test, and builds both apps on macos-26
Digitizer/                         # The main app (self-contained)
AccuracyTester/                    # The optional accuracy tool (self-contained)
```

Inside `Digitizer/`:

```text
digitizer.py            # CLI / function-call launcher
digitizer_2_11.py       # GUI + CLI dispatch and runtime path setup (macOS-adapted)
digitizer_desktop.py    # GUI-only entry used by the PyInstaller build
digitizer_cli.py        # Terminal CLI (single image)
digitizer_batch_cli.py  # Terminal CLI (whole folder)
digitizer_api.py        # Programmatic API (digitize_image)
function.py             # Thin re-export of digitize_image
UI.py                   # Main window and GUI workflows
ImageTray.py            # Canvas rendering and interaction
PointPlacer.py          # Color-based point extraction + interpolation
AxisReader.py           # OCR axis detection (macOS-adapted)
Calibration.py          # Calibration strategies
EnhancedClick.py        # Sub-pixel snapping for manual calibration clicks
Masking.py              # OCR / manual masking helpers (macOS-adapted)
ErrorLogger.py          # Error logging utilities
digitizer_macos.spec    # PyInstaller spec (Digitizer.app)
build_macos.sh          # macOS build script
vendor_tesseract_macos.sh  # Vendors a self-contained Tesseract runtime
make_macos_icons.py     # Builds assets/digitizer.icns from a source image
requirements.txt        # Python dependencies
version.json            # App name + version
assets/                 # Application icon source
vendor/tesseract/       # Bundled Tesseract OCR runtime (generated at build time)
```

Inside `AccuracyTester/`:

```text
AccuracyTesterPro.py        # The GUI tool (Tkinter + matplotlib + pandas)
accuracytester_desktop.py   # Entry point
accuracy_core.py            # The statistics (RMSE, R2, correlation, ...)
accuracy_batch_cli.py       # Terminal CLI: score a whole folder
batch_scoring.py            # File pairing + per-image scoring engine
accuracytester_macos.spec   # PyInstaller spec (AccuracyTester.app)
build_macos.sh              # macOS build script
requirements.txt            # Python dependencies
version.json                # App name + version
```

---

## Accuracy Tester (optional)

This is a **separate, optional** tool. It's completely independent of the main Digitizer — you don't need it to get your data out.

**What it does:** it measures how faithfully a digitized curve reproduces a reference curve. You load **two CSV files** — an *original* reference and a *digitized* one — and it lines them up on a common X grid and reports accuracy numbers (MAE, RMSE, R-squared, bias, MAPE/sMAPE/WAPE, and more) alongside diagnostic plots: the curve overlay, residuals, absolute error, and zoomable outliers. It cleans messy data (drops non-numeric rows, collapses duplicate X values), can filter by color slot, and can optionally optimize a constant X-shift before comparing. Results can be exported to a comparison CSV.

**Run the app (no Python needed):**
Double-click **`AccuracyTester.app`** (download `AccuracyTester-macos.app.zip` from [Releases](https://github.com/RayanA07/digitizer_mac/releases) and unpack it, or, if you built from source, find it in `AccuracyTester/dist`). It's a windowed app — no install or console needed. The same Gatekeeper note applies on first launch (right-click → **Open**).

**Run from source:**

```bash
python3 accuracytester_desktop.py
```

**Score a whole folder instead of two files:** see [Batch mode](#b1--score-the-results-against-the-true-data-batch-accuracy-testing) above, or `AccuracyTester/README.md`.

---

*Runtime logs are written to `~/Library/Application Support/DataDigitizer/2.15/logs` (you can also view them in-app via **Advanced → Error Log**).*
