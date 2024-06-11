import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import pingouin as pg
from scipy.stats import f_oneway
from scipy.stats import shapiro
from scipy.stats import levene
from scipy.stats import friedmanchisquare
from scipy.stats import ttest_rel
from scipy.stats import wilcoxon
import seaborn as sns

df = pd.read_csv('phonem_demo.csv')

phonem_list = df.values.flatten()


#DESCRIPTIVE STATISTICS AND VISUALIZATION
print("\n########################### DESCRIPTIVE STATISTICS ###########################\n")

# Calculate the frequencies of appearance of each phoneme
phonem_counts = {}
for phonem in phonem_list:
    phonem_counts[phonem] = phonem_counts.get(phonem, 0) + 1

# Calculate mean, median, and standard deviation of appearance
appearance_values = list(phonem_counts.values())
mean_appearance = np.mean(appearance_values)
median_appearance = np.median(appearance_values)
std_appearance = np.std(appearance_values)

# Calculate modus of appearance
mod_count = 0
mod = ""
print("Frequencies of appearance of each phoneme:")
for phonem, count in phonem_counts.items():
    print(f"{phonem}: {count}")
    if count > mod_count:
        mod_count = count
        mod = phonem

# Print results
print("\nMean appearance:", mean_appearance)
print("Median appearance:", median_appearance)
print("Standard deviation of appearance:", std_appearance)
print("Modus of appearance:", mod, ", appeared ", mod_count, " times")


# Prepare data for visualization
phonem_names = list(phonem_counts.keys())
counts = list(phonem_counts.values())

# Plotting the pie chart for the distribution of phonemes
plt.figure(figsize=(10, 6))
plt.pie(counts, labels=phonem_names, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Phonemes')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.close()

# Plotting the barplot of mean value of appearance and error bar of standard deviation
plt.figure(figsize=(6, 6))
plt.bar(' ', mean_appearance, yerr=std_appearance, capsize=10, color='skyblue', edgecolor='black')
plt.title('Bar Plot of Phoneme mean value with standard deviation')
plt.xlabel(' ')
plt.ylabel('Mean value')
plt.show()
plt.close()

# Plotting the histogram for frequencies with line representing median
plt.bar(phonem_names, counts, width=1.0, alpha=0.7, label='Frequencies')
plt.axhline(y=median_appearance, color='b', linestyle='--', label='Median of appearance')
plt.xlabel('Phonems')
plt.ylabel('Number of appearances')
plt.title('Frequencies of appearances of phonems')
plt.legend()
plt.show()
plt.close()


#INFERENTIAL STATISTICS
print("\n########################### INFERENTIAL STATISTICS ###########################\n")

df = pd.read_csv('phonem_demo.csv')

phonem_list2 = df.values.flatten()
# Calculate the frequencies of appearance of each phoneme
phonem_counts2 = {}
for phonem in phonem_list2:
    phonem_counts2[phonem] = phonem_counts2.get(phonem, 0) + 1

appearance_values2 = list(phonem_counts2.values())

# Shapiro-Wilk Test for normality
stat1, p1 = shapiro(appearance_values)
print('Shapiro-Wilk Test: Statistics=%.3f, p=%.3f' % (stat1, p1))
if p1 > 0.05:
    print("appearance_values data is normally distributed.\n")
else:
    print("appearance_values data is not normally distributed.\n")

stat2, p2 = shapiro(appearance_values2)
print('Shapiro-Wilk Test: Statistics=%.3f, p=%.3f' % (stat2, p2))
if p2 > 0.05:
    print("appearance_values2 data is normally distributed.\n")
else:
    print("appearance_values2 data is not normally distributed.\n")

data = pd.DataFrame({'Data1': appearance_values, 'Data2': appearance_values2, 'Data3': appearance_values})
spher, W, chi2, dof, pval = pg.sphericity(data)
print("\nMauchly's test for sphericity: chi2=%.3f, p=%.3f" % (chi2, pval))
if pval > 0.5:
    print("Data is spherical.\n")
else:
    print("Data is not spherical.\n")

stats, pval_levene = levene(appearance_values, appearance_values2, appearance_values)
print("Levene test for homogeneity: statistics=%.3f, p=%.3f" % (stats, pval_levene))
if pval_levene > 0.5:
    print("Data is homogeneous.\n")
else:
    print("Data is not homogeneus.\n")

if p1 > 0.5 and p2 > 0.5 and pval > 0.5 and pval_levene > 0.5:
    print("Data is suitable for ANOVA parametric statistical test.")
else:
    print("Data is not suitable for ANOVA parametric statistical test.")