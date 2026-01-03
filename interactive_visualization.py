import plotly.express as px

def interactive_visual(df):

    fig = px.scatter(
        df,
        x="Sales",
        y="Quantity",
        color="Category",
        title="Interactive Sales vs Quantity"
    )

    fig.show()
