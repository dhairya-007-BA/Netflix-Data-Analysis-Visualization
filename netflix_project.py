import pandas as pd
# Load the dataset
df=pd.read_csv("netflix_data.csv")
# Display firt 5 rows 
df.head()
#Check Data types and missing values
df.info()
#Summary statistics of numerical coloumns
df.describe()
#Check Missing values
df.isnull().sum()

# Creating Visualizations
import matplotlib.pyplot as plt

content_counts = df ['type'].value_counts() #count the number of TV shows and Movies

plt.figure(figsize=(6,4)) # Create a figure with a size of 6 inches and 4 inches tall
content_counts.plot(kind='bar',color=['Red','blue']) # Plotting bar chart with red and blue colour
plt.title("Number of Movies VS. TV shows on Netflix") #Add labels and Titles
plt.xlabel("Content Type") #add X line label as Content type
plt.ylabel("Count") # Add Y lable as Count
plt.show() # Show tha bar chart

# Rename the column to match your script
df.rename(columns={'releaseYear': 'release_year'}, inplace=True)

# Check for missing or infinite values in release_year
print(df['release_year'].isna().sum())  # Count NaN values
print(df['release_year'][df['release_year'] == float('inf')])  # Check for infinite values

# Handle missing values (choose ONE method: dropna or fillna)
df['release_year'].fillna(df['release_year'].median(), inplace=True)

# Convert to integer safely
df['release_year'] = df['release_year'].astype(int)

# Netflix Content Release Over the Years
yearly_trend = df.groupby('release_year')['title'].count()

# Plot the trend
plt.figure(figsize=(10,5))
yearly_trend.plot(kind='line', color='green')
plt.title("Netflix Content Released Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Releases")
plt.show()

#Analysing most common Genre on Netflix

from collections import Counter #Counter is a built in fuction and it is used to count the number of times each genre appears
# Check correct column name
print(df.columns)  # Ensure 'genres' is the correct column

# Split and count genres
genre_list = df['genres'].str.split(',').explode()  # selects the genre column, splits the comma seperated genre into a list
genre_counts = Counter(genre_list) #Split and Count genre

# Convert to DataFrame for visualization
genre_df = pd.DataFrame(genre_counts.items(), columns=['Genre', 'Count']).sort_values(by='Count', ascending=False)

# Plot bar chart
plt.figure(figsize=(12,6))
plt.barh(genre_df['Genre'].head(10), genre_df['Count'].head(10), color='purple')
plt.gca().invert_yaxis()  # Invert y-axis for better visualization
plt.title("Top 10 Most Common Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

#Analyzing Ratings Distributions
print(df.columns)
rating_counts = df['imdbAverageRating'].round(1).value_counts().sort_index() # df['rating'] selects the rating column from the DataFrame. .value_counts() counts how many times each rating appears in the dataset.

plt.figure(figsize=(12,7))
rating_counts.plot(kind='bar',color='orange')
plt.title("Distribution of Content Ratings on Netflix")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(ticks=range(0, len(rating_counts), 5), labels=rating_counts.index[::5], rotation=45, ha='right') #modifies the X-axis labels in your bar chart to improve readability.
plt.show()
