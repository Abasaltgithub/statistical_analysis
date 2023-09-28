import matplotlib.pyplot as plt
import numpy as np

# Data
post_titles = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M"
]

likes = [15, 13, 42, 2, 8, 33, 5, 19, 21, 7, 30, 5, 36]
impressions = [1626, 1234, 570, 349, 283, 282, 242, 72, 54, 41, 30, 3, 1]

# Create an array of post indices for positioning bars side by side
post_indices = np.arange(len(post_titles))

# Set the width of each bar
bar_width = 0.35

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot Likes
likes_bar = ax.bar(post_indices - bar_width / 2, likes,
                   bar_width, color='skyblue', label='Likes')
ax.set_xlabel('Post Titles', fontsize=14, fontweight='bold')
ax.set_ylabel('Likes', color='skyblue', fontsize=14, fontweight='bold')
ax.tick_params(axis='y', labelcolor='skyblue')

# Create a second y-axis on the right side for Impressions
ax2 = ax.twinx()
impressions_bar = ax2.bar(post_indices + bar_width / 2, impressions,
                          bar_width, color='lightcoral', label='Impressions')
ax2.set_ylabel('Impressions', color='lightcoral',
               fontsize=14, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='lightcoral')

# Center the x-tick labels between the bars
ax.set_xticks(post_indices)
ax.set_xticklabels(post_titles, rotation=0, ha='center',
                   fontsize=12, fontweight='bold')

# Add labels and title
ax.set_title('Likes vs. Impressions for Each Post',
             fontsize=16, fontweight='bold')

# Increase the size and make the numbers bold for tick labels
ax.tick_params(axis='both', which='major', labelsize=12)
for tick in ax.get_xticklabels():
    tick.set_fontweight('bold')
for tick in ax.get_yticklabels():
    tick.set_fontweight('bold')

# Set the impression y-axis tick labels to bold and larger
for tick in ax2.get_yticklabels():
    tick.set_fontweight('bold')
    tick.set_fontsize(12)

# Create a best-fit legend
legends = [likes_bar, impressions_bar]
labels = ['Likes', 'Impressions']
ax.legend(legends, labels, loc="upper left", bbox_to_anchor=(0.3, 1))

# Show the plot
plt.tight_layout()
plt.show()
