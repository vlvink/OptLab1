import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--P0", type=float, default=50e-3, help="Peak power in watts (default: 50 mW)")
parser.add_argument("--alpha", type=float, default=0.046052, help="Attenuation coefficient in 1/km (default: 0.046052)")
parser.add_argument("--beta2", type=float, default=-21.6321, help="Dispersion coefficient (GVD) in ps^2/km (default: -21.6321)")
parser.add_argument("--gamma", type=float, default=1.6215, help="Nonlinearity coefficient in 1/(W*km) (default: 1.6215)")
parser.add_argument("--L", type=float, default=100, help="Fiber length in km (default: 100)")
parser.add_argument("--lambda_0", type=float, default=1550e-9, help="Central wavelength in meters (default: 1550 nm)")
parser.add_argument("--T0", type=float, default=100e-12 / 2.63, help="Initial pulse width parameter T0 in seconds (default calculated for 100 ps)")
parser.add_argument("--C", type=float, default=-1, help="Frequency modulation constant (default: -1)")
parser.add_argument("--dz", type=float, default=0.1, help="Propagation step size in km (default: 0.1)")
parser.add_argument("--N", type=int, default=1024, help="Number of time samples (default: 1024)")

args = parser.parse_args()