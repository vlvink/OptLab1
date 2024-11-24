from matplotlib import pyplot as plt
import numpy as np


def plot_temporal_profile(T: np.ndarray,
                          A: np.ndarray,
                          A0: np.ndarray) -> None:
    '''
    Displays the temporal profile of the graph
    :param T: Temporal grid (time points) for the simulation
    :param A: Current amplitude of the pulse
    :param A0: Initial Pulse
    :return:
    '''
    plt.plot(T * 1e12, np.abs(A0) ** 2, label="Input")
    plt.plot(T * 1e12, np.abs(A) ** 2, label="Output")
    plt.xlabel("Time (ps)")
    plt.ylabel("Intensity |A(z, T)|^2")
    plt.legend()
    plt.title("Temporal Profile")
    plt.tight_layout()
    plt.savefig('additional_data/temporal_profile.png')
    plt.show()


def plot_spectral_profile(lambda_vals: np.ndarray,
                          A_freq_in: np.ndarray,
                          A_freq_out: np.ndarray) -> None:
    '''
    Displays the spectral profile of the graph
    :param lambda_vals: Wavelength values
    :param A_freq_in: Spectrum (Fourier transform) of the pulse at the input
    :param A_freq_out: Spectrum (Fourier transform) of the pulse at the output
    :return:
    '''
    plt.plot(lambda_vals * 1e9, np.abs(A_freq_in) ** 2, label="Input")
    plt.plot(lambda_vals * 1e9, np.abs(A_freq_out) ** 2, label="Output")
    plt.xlim(1549.8, 1550.2)
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Spectral Power |A(z, λ)|^2")
    plt.xlim(1549.8, 1550.2)
    plt.legend()
    plt.title("Spectral Profile")
    plt.tight_layout()
    plt.savefig('additional_data/spectral_profile.png')
    plt.show()