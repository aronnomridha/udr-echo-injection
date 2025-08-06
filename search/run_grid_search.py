
import h5py
import numpy as np
from gwpy.timeseries import TimeSeries
from matched_filter import matched_filter

def run_grid_search(strain_path, template_bank_path, output_path):
    strain = TimeSeries.read(strain_path).value

    with h5py.File(template_bank_path, "r") as f:
        waveforms = f["waveforms"]
        results = {}
        for key in waveforms:
            template = waveforms[key][:]
            snr_series, max_snr, idx = matched_filter(strain, template)
            results[key] = {
                "max_snr": float(max_snr),
                "peak_index": int(idx)
            }

    # Save results as .npz
    np.savez(output_path, **results)
    print(f"Saved grid search results to {output_path}")

if __name__ == "__main__":
    run_grid_search("strain_injected.txt", "udr_echo_v2.0_bank.hdf5", "grid_search_results.npz")
