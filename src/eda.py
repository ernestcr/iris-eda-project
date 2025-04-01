def plot_histograms(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Set the style of seaborn
    sns.set(style="whitegrid")

    # Create histograms for each feature
    features = df.columns[:-1]  # Exclude the species column
    plt.figure(figsize=(12, 8))
    
    for feature in features:
        plt.subplot(2, 2, features.tolist().index(feature) + 1)
        sns.histplot(df[feature], bins=20, kde=True)
        plt.title(f'Histogram of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

def plot_scatter(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Set the style of seaborn
    sns.set(style="whitegrid")

    # Create scatter plots for each pair of features
    plt.figure(figsize=(12, 8))
    sns.pairplot(df, hue='species', markers=["o", "s", "D"])
    plt.suptitle('Scatter Plot of Iris Features', y=1.02)
    plt.show()

def summary_statistics(df):
    return df.describe()