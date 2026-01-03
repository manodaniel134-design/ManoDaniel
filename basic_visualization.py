import matplotlib.pyplot as plt

def basic_visuals(df):

    # Bar chart for Category
    df["Category"].value_counts().plot(kind="bar")
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.show()

    # Sales distribution
    plt.hist(df["Sales"], bins=20)
    plt.title("Sales Distribution")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.show()
