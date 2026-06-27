import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib


# Load Processed Dataset
df = pd.read_csv("dataset/processed_data.csv")

print("=" * 50)
print("Customer Segmentation Started")
print("=" * 50)

# Features for K-Means
features = [
    "Customer_Lifetime_Value",
    "Purchase_Frequency",
    "Revenue",
    "Profit",
    "Product_View_Count",
    "Wishlist_Count",
    "Cart_Count",
    "Engagement_Score",
    "Shopping_Intent_Score"
]

X = df[features]

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means Model

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

# Save Model & Scaler
joblib.dump(
    kmeans,
    "machine_learning/trained_models/kmeans.pkl"
)

joblib.dump(
    scaler,
    "machine_learning/trained_models/scaler.pkl"
)

# Cluster Centers
centers_scaled = pd.DataFrame(
    kmeans.cluster_centers_,
    columns=features
)

print("\nCluster Centers (Scaled Values):")
print(centers_scaled)

centers_original = pd.DataFrame(
    scaler.inverse_transform(
        kmeans.cluster_centers_
    ),
    columns=features
)

print("\nCluster Centers (Original Values):")
print(centers_original)

# Business Segment Labels
cluster_revenue = centers_original["Revenue"]

sorted_clusters = cluster_revenue.sort_values()

cluster_mapping = {
    sorted_clusters.index[0]: "Silver",
    sorted_clusters.index[1]: "Gold",
    sorted_clusters.index[2]: "Platinum"
}

df["Customer_Segment_ML"] = (
    df["Cluster"].map(cluster_mapping)
)

# Cluster Summary
print("\nCluster Counts:")
print(df["Cluster"].value_counts())

print("\nCustomer Segment Distribution:")
print(df["Customer_Segment_ML"].value_counts())

# Revenue Analysis
print("\nRevenue By Segment:")
print(
    df.groupby(
        "Customer_Segment_ML"
    )["Revenue"]
    .mean()
    .sort_values(
        ascending=False
    )
)

# Shopping Time Analysis
print("\nShopping Time Preference:")
print(
    pd.crosstab(
        df["Customer_Segment_ML"],
        df["Shopping_Period"]
    )
)

# Gender Analysis
print("\nGender Distribution:")
print(
    pd.crosstab(
        df["Customer_Segment_ML"],
        df["Gender"]
    )
)

# Country Analysis
print("\nTop Countries By Segment:")
print(
    pd.crosstab(
        df["Customer_Segment_ML"],
        df["Country"]
    )
)

# Save Segmented Dataset
df.to_csv(
    "dataset/segmented_customers.csv",
    index=False
)

print("\nSegmented Dataset Saved")
print("dataset/segmented_customers.csv")

print("\nKMeans Model Saved")
print("machine_learning/trained_models/kmeans.pkl")

print("\nScaler Saved")
print("machine_learning/trained_models/scaler.pkl")

print("\nCustomer Segmentation Completed Successfully")