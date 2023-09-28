import matplotlib.pyplot as plt

# Data
categories = [
    'Alteration in Sense of Smell (Age > 40)',
    'Highest Prevalence of Smell Alterations (Age > 80)',
    'Phantom Odor Perception (Age > 40)',
    'Phantom Odors More Likely in Women (Age 40-60)',
    'Measurable Smell Dysfunction',
    'Anosmia/Severe Hyposmia'
]
# Replace None with a numerical value or omit it
percentages = [23, 32, 6.5, None, 12.4, 3]

# Remove data points with no percentage values
categories_filtered = [cat for cat, percent in zip(
    categories, percentages) if percent is not None]
percentages_filtered = [
    percent for percent in percentages if percent is not None]

# Create a vertical bar plot
plt.figure(figsize=(8, 6))
bars = plt.bar(categories_filtered, percentages_filtered, color='skyblue')
# plt.xlabel('Data')
plt.ylabel('Percentage (%)')
plt.title('Percentage Data on Smell Alterations')

# Add percentage labels to the bars
for i, bar in enumerate(bars):
    height = percentages_filtered[i]
    plt.text(bar.get_x() + bar.get_width() / 2, height +
             0.5, f'{height}%', color='black', ha='center')

# Adjust the rotation angle of x-axis labels for better readability
plt.xticks(rotation=15, ha='right')

plt.tight_layout()  # Ensures all labels are visible
plt.show()
