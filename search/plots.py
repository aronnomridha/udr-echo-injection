
import numpy as np
import matplotlib.pyplot as plt

def plot_snr_heatmap(results_path):
    data = np.load(results_path, allow_pickle=True)

    dt_vals = []
    gamma_vals = []
    snr_vals = []

    for key in data:
        parts = key.split("_")
        dt = int(parts[1].replace("us", ""))
        gamma = int(parts[3])
        snr = data[key].item()["max_snr"]
        dt_vals.append(dt)
        gamma_vals.append(gamma)
        snr_vals.append(snr)

    dt_vals = np.array(dt_vals)
    gamma_vals = np.array(gamma_vals)
    snr_vals = np.array(snr_vals)

    plt.figure(figsize=(6,5))
    scatter = plt.scatter(dt_vals, gamma_vals, c=snr_vals, cmap='plasma', s=100, edgecolor='k')
    plt.colorbar(scatter, label="Max SNR")
    plt.xlabel("Delay Δt [µs]")
    plt.ylabel("Damping γ × 100")
    plt.title("UDR Echo Grid Search SNR Heatmap")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("snr_heatmap.pdf")
    plt.show()

if __name__ == "__main__":
    plot_snr_heatmap("grid_search_results.npz")
