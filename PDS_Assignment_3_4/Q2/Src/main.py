import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("diabetes.csv")

# a) Random sample of 25 observations and comparison with population statistics for Glucose
np.random.seed(42)  # Set seed for reproducibility
sample = data.sample(n=25)
sample_mean_glucose = sample['Glucose'].mean()
sample_max_glucose = sample['Glucose'].max()
population_mean_glucose = data['Glucose'].mean()
population_max_glucose = data['Glucose'].max()

# Create comparison plot
plt.figure(figsize=(10, 5))
plt.bar(['Population Mean', 'Sample Mean'], [population_mean_glucose, sample_mean_glucose], color=['blue', 'orange'])
plt.xlabel('Statistic')
plt.ylabel('Glucose Level')
plt.title('Comparison of Mean Glucose Levels between Population and Sample')
plt.savefig('plot_comparison_glucose.png', bbox_inches='tight')
plt.show()

# b) 98th percentile of BMI for sample and population comparison
print("Population Max Glucose:", population_max_glucose)
print("Sample Max Glucose:", sample_max_glucose)
sample_98th_percentile_bmi = np.percentile(sample['BMI'], 98)
population_98th_percentile_bmi = np.percentile(data['BMI'], 98)
plt.figure(figsize=(10, 5))
plt.bar(['Population 98th Percentile', 'Sample 98th Percentile'], [population_98th_percentile_bmi, sample_98th_percentile_bmi], color=['blue', 'orange'])
plt.xlabel('Statistic')
plt.ylabel('BMI')
plt.title('Comparison of 98th Percentile of BMI between Population and Sample')
plt.savefig('bmi_comparison_98.png', bbox_inches='tight')
plt.show()


bootstrap_means = []
bootstrap_stds = []
bootstrap_percentiles = []

for _ in range(500):
    bootstrap_sample = data.sample(n=150, replace=True)
    bootstrap_means.append(bootstrap_sample['BloodPressure'].mean())
    bootstrap_stds.append(bootstrap_sample['BloodPressure'].std())
    bootstrap_percentiles.append(np.percentile(bootstrap_sample['BloodPressure'], 50))

# Calculate population statistics for comparison
population_mean_bp = data['BloodPressure'].mean()
population_std_bp = data['BloodPressure'].std()
population_percentile_bp = np.percentile(data['BloodPressure'], 50)

# Create comparison plots
plt.figure(figsize=(10, 5))
plt.hist(bootstrap_means, bins=30, alpha=0.5, color='orange', label='Bootstrap Means')
plt.axvline(population_mean_bp, color='blue', linestyle='dashed', linewidth=2, label='Population Mean')
plt.xlabel('Blood Pressure')
plt.ylabel('Frequency')
plt.title('Comparison of Bootstrap Means with Population Mean')
plt.savefig('comparison_BP_frequency.png', bbox_inches='tight')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(bootstrap_stds, bins=30, alpha=0.5, color='orange', label='Bootstrap Standard Deviations')
plt.axvline(population_std_bp, color='blue', linestyle='dashed', linewidth=2, label='Population Standard Deviation')
plt.xlabel('Blood Pressure')
plt.ylabel('Frequency')
plt.title('Comparison of Bootstrap Standard Deviations with Population Standard Deviation')
plt.savefig('bp_population_comparison.png', bbox_inches='tight')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(bootstrap_percentiles, bins=30, alpha=0.5, color='orange', label='Bootstrap Percentiles')
plt.axvline(population_percentile_bp, color='blue', linestyle='dashed', linewidth=2, label='Population 50th Percentile')
plt.xlabel('Blood Pressure')
plt.ylabel('Frequency')
plt.title('Comparison of Bootstrap Percentiles with Population Percentile')
plt.savefig('percentiles.png', bbox_inches='tight')
plt.legend()
plt.show()