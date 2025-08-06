
# UDR Echo Injection Toolkit (v2.0)

This repository provides tools to generate, inject, and analyze gravitational wave echo signals predicted by the **Unified Distortion Relativity (UDR)** theory. It supports direct injection into real LIGO O4 strain data and includes a full search pipeline to scan for echoes in the distortion-tail framework.

## 🔬 Features

- UDR-consistent echo waveform generator
- Injection into GW150914 Hanford strain (O4)
- Template bank over delay & damping factors (Δt, γ)
- Matched-filter pipeline and heatmap visualizations

## 📦 Files

- `udr_echo_template.py`: Generates UDR echo signals based on mass, spin, distortion delay
- `inject_udr_echo.py`: Injects echo into LIGO O4 data (e.g., GW150914)
- `udr_echo_v2.0_bank.hdf5`: Bank of precomputed waveforms

## 🔍 Search Pipeline (`search/`)

- `matched_filter.py`: FFT-based matched filtering
- `run_grid_search.py`: Runs search over template bank
- `analyze_results.py`: Prints high-SNR matches
- `plots.py`: Creates SNR heatmaps from search results

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/udr-echo-injection.git
cd udr-echo-injection
pip install -r requirements.txt
python inject_udr_echo.py
python search/run_grid_search.py
python search/analyze_results.py
python search/plots.py
```

## 📚 Requirements

- `gwpy`
- `numpy`
- `matplotlib`
- `h5py`

Install with:

```bash
pip install -r requirements.txt
```

## 📄 License

MIT License. Free for academic and non-commercial use.
