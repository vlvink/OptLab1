import numpy as np
from scipy.fftpack import fft, ifft


def initialize_pulse(T: np.ndarray,
                     P0: float,
                     T0: float,
                     C: float) -> np.ndarray:
    '''
    Generate the initial pulse shape based on a hyperbolic secant profile.
    :param T: Temporal grid (time points) for the simulation
    :param P0: Peak power of the pulse in watts
    :param T0: Initial pulse width parameter in seconds
    :param C: Frequency modulation constant
    :return: Pulse with given parameters
    '''
    return np.sqrt(P0) * np.cosh(T / T0) ** -1 * np.exp(-1j * C * T ** 2 / (2 * T0 ** 2))


def propagate_pulse(A: np.ndarray,
                    omega: np.ndarray,
                    dz: float,
                    num_steps: int,
                    alpha: float,
                    beta2: float,
                    gamma: float) -> np.ndarray:
    '''
    Propagate the pulse along the fiber using the split-step Fourier method.
    :param A: Current amplitude of the pulse
    :param omega: Array of angular frequency components
    :param dz: Propagation step size along the fiber
    :param num_steps: Total number of propagation steps
    :param alpha: Attenuation coefficient in the fiber
    :param beta2: Group velocity dispersion (GVD) coefficient in ps^2/km
    :param gamma: Nonlinearity coefficient in 1/(W*km)
    :return: Propagated pulse
    '''
    for _ in range(num_steps):
        A_freq = fft(A)
        A_freq *= np.exp((0.5j * beta2 * omega ** 2 - alpha / 2) * dz)
        A = ifft(A_freq)

        A *= np.exp(1j * gamma * np.abs(A) ** 2 * dz)

    return A
