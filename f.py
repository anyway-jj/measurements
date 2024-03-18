import plotly.express as px
import pandas as pd
import numpy as np

def get_values(setup_number):
	file = open("measurements.txt")
	lines = file.readlines()
	for i in range(len(lines)):
		line = lines[i].split(' ')
		if int(line[0]) == setup_number:
			voltage_arr.append(float(line[2]))

voltage_arr = []
a = int(input("Enter installation number: "))
get_values(a)
measurements_arr = np.arange(1, len(voltage_arr)+1, 1)

pd.options.plotting.backend = "plotly"
df = pd.DataFrame(dict(Measurement=measurements_arr, Voltage=voltage_arr))
fig = px.line(df, x="Measurement", y="Voltage")
fig.update_xaxes(tickvals=measurements_arr)
fig.show()