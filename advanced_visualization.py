import seaborn as sns
import matplotlib.pyplot as plt

def advanced_visuals(df):

    sns.pairplot(df[["Sales", "Quantity", "Unit Price"]])
    plt.show()

    sns.heatmap(
        df[["Sales", "Quantity", "Unit Price"]].corr(),
        annot=True
    )
    plt.title("Correlation Heatmap")
    plt.show()
