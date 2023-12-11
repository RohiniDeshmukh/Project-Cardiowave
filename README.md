# Project-Cardiowave

<img width="951" alt="image" src="https://github.com/RohiniDeshmukh/Project-Cardiowave/assets/121260777/06b61558-3279-4527-8297-83a7f4d356f1">

## Installation

Before running Project Cardiowave, you need to install certain Python libraries that are essential for processing the ECG data.

### Prerequisites

Ensure you have Python installed on your system. Project Cardiowave uses Python 3.8 or newer.

### Installing biosppy

`biosppy` is a library that allows for easy ECG signal processing. Install it using pip:

```bash
pip install biosppy

import numpy as np
from biosppy.signals import ecg

# load raw ECG signal
signal = np.loadtxt('./examples/ecg.txt')

# process it and plot
out = ecg.ecg(signal=signal, sampling_rate=1000., show=True)


Installing neurokit
neurokit is another powerful library used for advanced biosignal processing. Install it using pip:

pip install neurokit2

import neurokit2 as nk

# Download example data
data = nk.data("bio_eventrelated_100hz")

# Preprocess the data (filter, find peaks, etc.)
processed_data, info = nk.bio_process(ecg=data["ECG"], sampling_rate=100)

# Compute relevant features
results = nk.bio_analyze(processed_data, sampling_rate=100)
