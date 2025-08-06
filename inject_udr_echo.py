
import numpy as np
import matplotlib.pyplot as plt
from gwpy.timeseries import TimeSeries
from udr_echo_template import udr_echo_template

# Parameters
gps_time = 1126259462.4  # GW150914
duration = 4             # seconds
sample_rate = 4096       # Hz
mass = 65                # solar masses
spin = 0.68              # dimensionless
delta_t = 0.3e-3         # 0.3 ms
gamma = 0.9
h0 = 1e-22
tau = 0.001              # 1 ms envelope
N_echoes = 5

# Download O4 strain data (LIGO Hanford)
print("Fetching strain data from GWOSC...")
strain = TimeSeries.fetch_open_data('H1', gps_time - duration/2, gps_time + duration/2, sample_rate=sample_rate)

# Generate time array
t = np.linspace(-duration/2, duration/2, int(duration * sample_rate))

# Generate echo waveform centered at t = 0
print("Generating UDR echo waveform...")
echo = udr_echo_template(t, M=mass, a=spin, delta=delta_t, gamma=gamma, h0=h0, tau=tau, N_echoes=N_echoes)

# Align echo with real strain data
echo_timeseries = TimeSeries(echo, times=strain.times)

# Inject into real strain
print("Injecting echo into real strain...")
strain_injected = strain + echo_timeseries

# Plot
plt.figure(figsize=(10, 5))
plt.plot(strain.times.value, strain.value, label='Original Strain', alpha=0.6)
plt.plot(strain_injected.times.value, strain_injected.value, label='With UDR Echo Injection', linewidth=1.2)
plt.xlabel("Time [s]")
plt.ylabel("Strain")
plt.title("Injection of UDR Echo into GW150914 (Hanford, O4 Data)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("udr_echo_injection_plot.pdf")
plt.show()
