import numpy as np


class Swarlet:
    def __init__(self):
	    self.wave = None
        self.timing_mean = 1.
        self.timing_std = 0.5
        self.amplitude_mean = 1.
        self.amplitude_std = 0.5

    def get_wave(self):
        return self.wave

def generate_stream(swarlets, num_samples):
	"""
	Parameters
	----------------
	swarlets: list of swarlet objects
	num_samples: how mnany swarlets to include

	Returns
	----------------
	ms: single stream of stitched swarlets
	"""
	pass 
