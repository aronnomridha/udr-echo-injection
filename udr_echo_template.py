
import numpy as np

def udr_echo_template(t, M, a, delta=0.3e-3, gamma=0.9, f0=None, h0=1e-22, tau=0.001, N_echoes=5, phi=0):
    '''
    Generate a UDR echo waveform for given physical parameters.

    Parameters:
    - t        : time array [s]
    - M        : final black hole mass [solar masses]
    - a        : dimensionless spin (0 < a < 1)
    - delta    : echo delay time [s] (can be derived from distortion profile)
    - gamma    : damping factor per echo
    - f0       : base frequency [Hz] (computed from QNM if None)
    - h0       : base echo amplitude
    - tau      : Gaussian envelope width [s]
    - N_echoes : number of echoes
    - phi      : initial phase [rad]

    Returns:
    - h_echo : time-domain strain array
    '''
    if f0 is None:
        # Use dominant (l=2, m=2, n=0) QNM frequency approximation from Berti et al.
        # f0 [Hz] ≈ (1 - 0.63 * (1 - a)**0.3) / (2 * π * M)
        # Convert M from solar masses to seconds: 1 M_sun ≈ 4.925e-6 s
        M_sec = M * 4.925e-6
        f0 = (1 - 0.63 * (1 - a)**0.3) / (2 * np.pi * M_sec)

    h_echo = np.zeros_like(t)
    for n in range(1, N_echoes + 1):
        t_shifted = t - n * delta
        envelope = np.exp(-t_shifted**2 / (2 * tau**2))
        oscillation = np.cos(2 * np.pi * f0 * t_shifted + phi)
        h_echo += h0 * gamma**n * envelope * oscillation

    return h_echo
