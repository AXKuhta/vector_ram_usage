import plotly
import psutil
import os
import time
from subprocess import PIPE

def run_test(n):
	p = psutil.Popen(f"vec_ram.exe {n}", stdout=PIPE, stdin=PIPE)
	
	p.stdout.read(2)

	memory = p.memory_info()

	p.stdin.write(b"\n")

	return memory.rss, memory.vms


series_rss = []
series_vms = []

for i in range(0, 64*1024*1024, 1*1024*1024):
	rss, vms = run_test(i)

	series_rss.append(rss)
	series_vms.append(vms)

	print(i)


plot_rss = plotly.graph_objects.Scatter(y=series_rss, name="bytes rss")
plor_vms = plotly.graph_objects.Scatter(y=series_vms, name="bytes vms")

fig = plotly.graph_objects.Figure(data=[plot_rss, plor_vms])
fig.write_html("memory.html")

os.system("memory.html")
