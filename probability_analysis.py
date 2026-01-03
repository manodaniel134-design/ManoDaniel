import seaborn as sns
import matplotlib.pyplot as plt

def probability_analysis(df):

    sns.kdeplot(df["Sales"], fill=True)
    plt.title("Probability Distribution of Sales")
    plt.xlabel("Sales")
    plt.show()
