
import numpy as np
import h5py
from scipy.signal import fftconvolve
from gwpy.timeseries import TimeSeries

def matched_filter(strain, template, psd=None, sample_rate=4096):
    '''
    Perform basic matched filtering of strain against template.

    Parameters:
    - strain      : ndarray, time-domain strain data
    - template    : ndarray, time-domain template
    - psd         : ndarray or None, power spectral density
    - sample_rate : sampling rate in Hz

    Returns:
    - snr_time_series : ndarray
    - max_snr         : float
    - peak_index      : int
    '''
    # Whiten both signals (optional if not already done)
    strain = strain - np.mean(strain)
    template = template - np.mean(template)

    # Normalize template
    norm = np.sqrt(np.sum(template**2))
    template /= norm

    # Perform FFT-based cross-correlation
    snr_series = fftconvolve(strain, template[::-1], mode='same')
    snr_series /= np.std(snr_series)  # crude whitening for SNR

    max_snr = np.max(np.abs(snr_series))
    peak_index = np.argmax(np.abs(snr_series))

    return snr_series, max_snr, peak_index

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # Load strain and template
    strain = TimeSeries.read("strain_injected.txt").value  # example: injected strain
    with h5py.File("udr_echo_v2.0_bank.hdf5", "r") as f:
        template = f["waveforms/dt_300us_gamma_90"][:]

    snr, max_snr, idx = matched_filter(strain, template)

    print(f"Max SNR = {max_snr:.2f} at index {idx}")

    # Plot SNR time series
    plt.plot(snr)
    plt.title("Matched Filter SNR Time Series")
    plt.xlabel("Time Index")
    plt.ylabel("SNR")
    plt.grid(True)
    plt.savefig("matched_filter_snr_plot.pdf")
    plt.show()
