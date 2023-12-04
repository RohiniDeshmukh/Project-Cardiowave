from flask import Flask, render_template, jsonify
import requests
import numpy as np

app = Flask(__name__)

# Download the ECG data file
url = "https://cs666.org/data/ecg.txt"
r = requests.get(url, allow_redirects=True)
open("ecg.txt", "wb").write(r.content)  # Save the content in binary mode

# Load the dataset using biosppy library
from biosppy.signals import ecg
# signal, mdata = ecg.ecg(signal=np.loadtxt('ecg.txt'), sampling_rate=1000., show=False)
# Load the dataset using biosppy library
signal = np.loadtxt('ecg.txt')
out = ecg.ecg(signal=signal, sampling_rate=1000., show=False)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/get_data')
# def get_data():
#     python_data = {"message": "Hello from Python!"}
#     return jsonify(python_data)

@app.route('/ecg_data')
def ecg_data_route():
    # Convert NumPy arrays to lists for JSON serialization
    ecg_data = {
        "signal": out['filtered'].tolist(),  # Filtered ECG signal
        "rpeaks": out['rpeaks'].tolist(),   # R-peak location indices
        # You can add other data from the `out` dict here
        "templates_ts": out['templates_ts'].tolist(),  # ECG template waveform timestamps
        "templates": out['templates'].tolist(),        # ECG template waveforms
        "heart_rate_ts": out['heart_rate_ts'].tolist(),# Heart rate time-series
        "heart_rate": out['heart_rate'].tolist() 
    }
    return jsonify(ecg_data)

if __name__ == '__main__':
    app.run(debug=True)
