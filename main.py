from import_export import import_data, export_data
from data_cleaning import clean_data
from data_transformation import transform_data
from descriptive_statistics import descriptive_stats
from basic_visualization import basic_visuals
from advanced_visualization import advanced_visuals
from interactive_visualization import interactive_visual
from probability_analysis import probability_analysis
from kmeans_clustering import kmeans_model
from summary_insights import summary

df = import_data("Ecommerce_Sales_Data_2024_2025.csv")
print(df.columns)
print(df.columns.tolist())
df = clean_data(df)
df = transform_data(df)

descriptive_stats(df)
basic_visuals(df)
advanced_visuals(df)
interactive_visual(df)
probability_analysis(df)
kmeans_model(df)
print(df.columns)


export_data(df, "Ecommerce_Cleaned.csv")
summary()
