import numpy as np
from args.args import *
from utils.utils import initialize_pulse, propagate_pulse
from visualization.visualize_graphs import plot_temporal_profile, plot_spectral_profile
from scipy.fftpack import fft, fftshift

lambda_0 = args.lambda_0

# Derived parameters and initial conditions
T_max = 5 * args.T0
dt = 2 * T_max / args.N
T = np.linspace(-T_max, T_max, args.N)
domega = 2 * np.pi / (args.N * dt)
omega = np.fft.fftshift(np.fft.fftfreq(args.N, d=dt)) * 2 * np.pi
num_steps = int(args.L / args.dz)

# Initialize pulse
A0 = initialize_pulse(T, args.P0, args.T0, args.C)

# Propagate pulse
A_out = propagate_pulse(A0.copy(), omega, args.dz, num_steps, args.alpha, args.beta2, args.gamma)

# Compute spectra for input and output
A_freq_in = np.abs(fftshift(fft(A0))) / args.N
A_freq_out = np.abs(fftshift(fft(A_out))) / args.N

# Convert to wavelength domain for plotting
c = 3e8  # Speed of light (m/s)
omega_safe = np.where(omega == 0, 1e-10, omega) # Prevent division by zero err
lambda_vals = np.fft.fftshift(2 * np.pi * c / omega_safe + lambda_0)

# Plot results
plot_temporal_profile(T, A0, A_out)
plot_spectral_profile(lambda_vals, A_freq_in, A_freq_out)
