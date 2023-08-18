# -*- coding: utf-8 -*-
"""Intelligent Monitor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cGqn-4S1IL8tTBiwlI0a3dlXC9xLxQVg
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulated data generation
num_components = 10
num_data_points = 1000000
time_seconds = np.arange(1, num_data_points + 1)
cpu_usage = np.random.uniform(0, 100, (num_components, num_data_points))
memory_utilization = np.random.uniform(512, 8192, (num_components, num_data_points))
network_traffic = np.random.randint(50, 200, (num_components, num_components, num_data_points))

# Simulated alerts generation
num_alerts = 500
alert_indices = np.random.choice(num_data_points, num_alerts, replace=False)
alerts = np.zeros(num_data_points, dtype=int)
alerts[alert_indices] = np.random.choice([0, 1, 2], num_alerts, p=[0.7, 0.2, 0.1])

# Visualization: CPU Usage for Component 1
plt.figure(figsize=(10, 5))
plt.plot(time_seconds, cpu_usage[0], label='Component 1')
plt.xlabel('Time (seconds)')
plt.ylabel('CPU Usage (%)')
plt.title('CPU Usage for Component 1')
plt.legend()
plt.grid(True)
plt.show()

# Visualization: Memory Utilization for Component 1
plt.figure(figsize=(10, 5))
plt.plot(time_seconds, memory_utilization[0], label='Component 1')
plt.xlabel('Time (seconds)')
plt.ylabel('Memory Utilization (MB)')
plt.title('Memory Utilization for Component 1')
plt.legend()
plt.grid(True)
plt.show()

# Visualization: Network Traffic between Component 1 and Component 2
plt.figure(figsize=(10, 5))
plt.plot(time_seconds, network_traffic[0, 1], label='Component 1 to Component 2')
plt.xlabel('Time (seconds)')
plt.ylabel('Network Traffic (packets/second)')
plt.title('Network Traffic between Component 1 and Component 2')
plt.legend()
plt.grid(True)
plt.show()

# Alert Analysis
critical_alerts = np.sum(alerts == 2)
warning_alerts = np.sum(alerts == 1)
informational_alerts = np.sum(alerts == 0)

print(f"Number of Critical Alerts: {critical_alerts}")
print(f"Number of Warning Alerts: {warning_alerts}")
print(f"Number of Informational Alerts: {informational_alerts}")

# Evaluation: Percentage Improvement Compared to Baseline
baseline_cpu_usage = np.mean(cpu_usage, axis=0)
baseline_memory_utilization = np.mean(memory_utilization, axis=0)
baseline_network_traffic = np.mean(network_traffic, axis=(0, 1))

intelligent_monitor_cpu_improvement = (np.mean(baseline_cpu_usage) - np.mean(cpu_usage)) / np.mean(baseline_cpu_usage) * 100
intelligent_monitor_memory_improvement = (np.mean(memory_utilization) - np.mean(baseline_memory_utilization)) / np.mean(baseline_memory_utilization) * 100
intelligent_monitor_network_improvement = (np.mean(network_traffic) - np.mean(baseline_network_traffic)) / np.mean(baseline_network_traffic) * 100

print(f"IntelligentMonitor CPU Improvement: {intelligent_monitor_cpu_improvement:.2f}%")
print(f"IntelligentMonitor Memory Improvement: {intelligent_monitor_memory_improvement:.2f}%")
print(f"IntelligentMonitor Network Improvement: {intelligent_monitor_network_improvement:.2f}%")