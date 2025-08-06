# UDR Echo Injection Toolkit (v2.0)

This repository provides tools to generate, inject, and analyze gravitational wave echo signals predicted by the **Unified Distortion Relativity (UDR)** theory. It supports direct injection into real LIGO O4 strain data and includes a template bank for use in search pipelines.

## 🔬 Features

- UDR-consistent echo waveform generator
- Injection into GW150914 Hanford strain (O4)
- Template bank over delay & damping factors
- Ready for PyCBC or matched-filtering pipelines

## 📦 Files

- `udr_echo_template.py`: Generates UDR echo signals
- `inject_udr_echo.py`: Injects echo into LIGO O4 data
- `udr_echo_v2.0_bank.hdf5`: Bank of precomputed waveforms

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/udr-echo-injection.git
cd udr-echo-injection
pip install -r requirements.txt
python inject_udr_echo.py
```
