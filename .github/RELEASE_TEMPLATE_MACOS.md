# LinePilot Digitizer <!-- vX.Y --> (macOS)

Turn a picture of a line plot into numbers — a CSV plus an overlay image showing the detected points. No install, no Python: the Tesseract OCR engine is bundled inside the app.

Three calibration modes, one curve-recovery workflow:
- **Standard** — click four axis ticks.
- **Enhanced** — the same four clicks, snapped to tick centers at sub-pixel precision (`Tools → Calibration → Enhanced Human Click`).
- **OCR** — fully automatic axis reading (`Advanced → Axis Scale Detection`), also used by the command line and batch mode.

This is the same code as the Windows release, built for Mac.

## Install (macOS 15 Sequoia or newer)

**1. Pick the zip for your Mac's chip.** Apple menu → **About This Mac**:
- **Chip: Apple M1 / M2 / M3 / M4…** → download `Digitizer-<!-- vX.Y -->-macOS-AppleSilicon.zip`
- **Processor: Intel…** → download `Digitizer-<!-- vX.Y -->-macOS-Intel.zip`

**2.** Double-click the zip to unpack **`Digitizer.app`**, then drag it into **Applications** (optional).

**3. First launch only — allow the app.** It isn't signed with a paid Apple Developer ID, so macOS blocks the first launch:
1. Double-click `Digitizer.app`. macOS says it *"cannot verify"* the app — click **Done**.
2. Open **System Settings → Privacy & Security**, scroll down, and click **Open Anyway** next to the message about Digitizer. Confirm with your password or Touch ID.

After that it opens normally. If macOS ever says the app is **"damaged"**, run this once in Terminal and try again:
```bash
xattr -dr com.apple.quarantine /Applications/Digitizer.app
```

Optional: `AccuracyTester-…-macOS-<chip>.zip` compares a digitized CSV against a reference CSV (same install steps).

Full guide: [macOS guide](https://github.com/RayanA07/digitizer_mac/blob/main/Digitizer/README_macOS.md) · [README](https://github.com/RayanA07/digitizer_mac#readme) · Project site: https://rayana07.github.io/LinePilot/

## New in this release
<!-- bullets -->

## Known limitations
- OCR can drop minus signs on negative tick labels and misread superscript / power-of-ten axes. Pass `--axis` or type the values in by hand in the app.
- Curves drawn in black or grey on charts with black axes are not reliably separable by the color-based extractor.
- Low-resolution figures are the main cause of wrong numbers; the app warns below 700 px.

---

## If you find LinePilot useful, please cite our paper

> Fengbo Ma, Rayan Akhtar, Aakash Joshi, Xiaoting Li, Haijian Sun, Zhen Xiang, Xianyan Chen, Yiping Zhao.
> **LinePilot Digitizer: Line-Plot Recovery with Manual and Automatic Calibration.** arXiv:2609.19377, 2026.
> https://arxiv.org/abs/2609.19377

```bibtex
@article{ma2026linepilot,
  title   = {LinePilot Digitizer: Line-Plot Recovery with Manual and Automatic Calibration},
  author  = {Ma, Fengbo and Akhtar, Rayan and Joshi, Aakash and Li, Xiaoting and
             Sun, Haijian and Xiang, Zhen and Chen, Xianyan and Zhao, Yiping},
  journal = {arXiv preprint arXiv:2609.19377},
  year    = {2026},
  doi     = {10.48550/arXiv.2609.19377}
}
```

The benchmark from the paper, **DigitizerBench**, is on Hugging Face: https://huggingface.co/datasets/LinePilot/DigitizerBench

⭐ Star or fork the repo, and [let us know how we did](https://github.com/RayanA07/LinePilot/issues) — bug reports, feature requests and example figures that trip it up are all welcome.

## Acknowledgment
This work was supported by the National Science Foundation through the Pathways to Open-Source Ecosystems (POSE) program, award No. 2518273. The authors gratefully acknowledge the support, guidance and collaboration of all members of the SpectraGuru™ development and stakeholder teams.

Full changelog: https://github.com/RayanA07/LinePilot/blob/main/CHANGELOG.md
