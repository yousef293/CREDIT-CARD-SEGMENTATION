
# CUST_ID: Credit card holder ID
# 
# BALANCE: Monthly average balance (based on daily balance averages)
# 
# BALANCE_FREQUENCY: Ratio of last 12 months with balance
# 
# PURCHASES: Total purchase amount spent during last 12 months
# 
# ONEOFF_PURCHASES: Total amount of one-off purchases
# 
# INSTALLMENTS_PURCHASES: Total amount of installment purchases
# 
# CASH_ADVANCE: Total cash-advance amount
# 
# PURCHASES_ FREQUENCY: Frequency of purchases (Percent of months with at least one purchase)
# 
# ONEOFF_PURCHASES_FREQUENCY: Frequency of one-off-purchases PURCHASES_INSTALLMENTS_FREQUENCY: Frequency of installment purchases
# 
# CASH_ADVANCE_ FREQUENCY: Cash-Advance frequency
# 
# AVERAGE_PURCHASE_TRX: Average amount per purchase transaction
# 
# CASH_ADVANCE_TRX: Average amount per cash-advance transaction
# 
# PURCHASES_TRX: Average amount per purchase transaction
# 
# CREDIT_LIMIT: Credit limit
# 
# PAYMENTS: Total payments (due amount paid by the customer to decrease their statement balance) in the period
# 
# MINIMUM_PAYMENTS: Total minimum payments due in the period.
# 
# PRC_FULL_PAYMEN: Percentage of months with full payment of the due statement balance
# 
# TENURE: Number of months as a customer


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import MiniBatchKMeans
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


class K_means_model:
    def __init__(self):
        self.cluster_names = {
     0: "Low Spender",
     1: "Average Spender",
     2: "High Spender"
     
}
    def dataproces(self, data):
        # Create DataFrame
        df = pd.DataFrame(data)

        # Fill missing values with column means
        df = df.fillna(df.mean(numeric_only=True))

        # Keep only numeric columns (important for scaling)
        numeric_df = df.select_dtypes(include=[np.number])

        # Scale numeric data
        self.scaler = StandardScaler()
        self.X = self.scaler.fit_transform(numeric_df)

        # Optional: Return the scaled DataFrame
        scaled_df = pd.DataFrame(self.X, columns=numeric_df.columns)

        # Convert NumPy types to native Python types
        scaled_df = scaled_df.astype(object).applymap(lambda x: x.item() if hasattr(x, 'item') else x)

        return scaled_df.to_dict(orient="records")
        

# ## Elbow Method
    def applying_elbow(self):



        distortions=[]
        for k in range(1,11):
            kmean=KMeans(n_clusters=k,max_iter=100,random_state=42)
            kmean.fit(self.X)
            distortions.append(kmean.inertia_ /self.X.shape[0])



        plt.figure(figsize=(8,6))
        plt.plot(range(1,11),distortions,marker='o',linestyle='-')
        plt.xlabel("NUMBER OF CLUSTERS K")
        plt.ylabel("'DISTORTIONS")
        plt.title("Elbow  Method for optimal k")
        plt.grid()
        plt.show()
        return distortions

# ### K=2 IS THE OPTIMAL NUMBER

    def train_model(self):
        optimal_k=3
        self.kmeans=KMeans(n_clusters=optimal_k,max_iter=100,random_state=42)
        cluster_labels = self.kmeans.fit_predict(self.X)

    # Evaluate cluster quality
        
        


        pca=PCA(n_components=None)

        x_scaled=pca.fit_transform(self.X)
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(pca.explained_variance_ratio_) + 1), 
                 pca.explained_variance_ratio_, 'o-')
        plt.xlabel('Number of Components')
        plt.ylabel('Explained Variance Ratio')
        plt.title('Choosing th Right Component Number for PCA')
        plt.grid()
        plt.show()




        fig = plt.figure(figsize=(10, 8))



        plt.scatter(
            x_scaled[:, 0],  
            x_scaled[:, 1],
            c=cluster_labels,
            cmap='viridis'
        )

        plt.colorbar()

        plt.show()
        return cluster_labels
    ###############################################################################################

    def evaluate_model(self):
        if not hasattr(self, 'kmeans') or not hasattr(self, 'X'):
            raise ValueError("Model is not trained. Call dataproces() and train_model() first.")
        
        score = silhouette_score(self.X, self.kmeans.labels_)
        return round(score, 4)
    #######################################################################################
    
    def prediction(self, input_dict):
 
     df = pd.DataFrame(input_dict)  # Convert dict to DataFrame
 
     # Fill missing values
     df = df.fillna(df.mean(numeric_only=True))
 
     # Convert numpy types to native Python
     df = df.applymap(lambda x: x.item() if hasattr(x, 'item') else x)
 
     # Standardize using the existing scaler (you should load the trained one)
     scaled = self.scaler.transform(df)
        
    
        # Predict cluster
     cluster_id = self.kmeans.predict(scaled)[0]
     cluster_name = self.cluster_names.get(cluster_id, "Unknown") 
     output={
         "cluster_id": int(cluster_id),
         "cluster_name": cluster_name
        }
     return output
''' ''
fro m sklearn.metrics import silhouette_score

labels = kmeans.labels_
score = silhouette_score(X, labels)
print("Silhouette Score:", score)


kmeans = MiniBatchKMeans(n_clusters=2, random_state=42, batch_size=300, max_iter=10)
centroid_history = []

# Run manual iterations to track centroids
for i in range(10):
    kmeans.partial_fit(X)
    centroid_history.append(kmeans.cluster_centers_.copy())

# Plot data points
plt.scatter(x_scaled[:, 0], x_scaled[:, 1], c='lightgray', s=30, label='Data')

# Plot centroid movement
colors = ['red', 'blue']
for cluster_id in range(2):
    x = [c[cluster_id][0] for c in centroid_history]
    y = [c[cluster_id][1] for c in centroid_history]
    plt.plot(x, y, marker='x', color=colors[cluster_id], label=f'Centroid {cluster_id}')
    plt.scatter(x, y, s=80, marker='x',c=colors[cluster_id], alpha=0.6)

plt.title("Centroid Movement (2 Clusters)")
plt.legend()
plt.grid(True)
plt.show()
'''

