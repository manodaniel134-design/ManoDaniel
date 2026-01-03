from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def kmeans_model(df):

    # Use existing numerical columns
    X = df[["Sales", "Quantity"]]

    kmeans = KMeans(n_clusters=3, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X)

    plt.scatter(df["Sales"], df["Quantity"], c=df["Cluster"])
    plt.xlabel("Sales")
    plt.ylabel("Quantity")
    plt.title("K-Means Clustering (Sales vs Quantity)")
    plt.show()
