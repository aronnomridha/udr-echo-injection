
import numpy as np

def analyze_snr_results(results_path, threshold=5.0):
    data = np.load(results_path, allow_pickle=True)
    recovered = []

    for key in data:
        max_snr = data[key].item()["max_snr"]
        if max_snr >= threshold:
            recovered.append((key, max_snr))

    recovered.sort(key=lambda x: -x[1])
    print(f"Templates with SNR >= {threshold}:")
    for key, snr in recovered:
        print(f"{key}: SNR = {snr:.2f}")

if __name__ == "__main__":
    analyze_snr_results("grid_search_results.npz", threshold=5.0)
