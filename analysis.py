
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("dataset.csv")

# 1. Explore the dataset
print("Dataset shape:", df.shape)
print("\nFirst five rows:")
print(df.head())

# 2. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 3. Calculate averages
print("\nAverage popularity:", df["popularity"].mean())
print("Average energy:", df["energy"].mean())
print("Average danceability:", df["danceability"].mean())

# 4. Average song duration in minutes
average_duration = df["duration_ms"].mean() / 60000
print("Average song duration:", round(average_duration, 2), "minutes")

# 5. Bar chart: Top 5 genres by record count
genre_counts = df["track_genre"].value_counts().head(5)
genre_counts.plot(kind="bar")
plt.title("Top 5 Genres by Number of Records")
plt.xlabel("Genre")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.show()

# 6. Histogram: Distribution of popularity
df["popularity"].plot(kind="hist", bins=20)
plt.title("Distribution of Song Popularity")
plt.xlabel("Popularity Score")
plt.ylabel("Number of Tracks")
plt.tight_layout()
plt.show()

sns.histplot(data=df, x="energy", bins=20)
plt.title("Distribution of Song Energy")
plt.xlabel("Energy")
plt.ylabel("Number of Tracks")
plt.show()
