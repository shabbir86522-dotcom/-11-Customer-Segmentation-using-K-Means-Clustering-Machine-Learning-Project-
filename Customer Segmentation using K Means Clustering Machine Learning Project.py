import pandas as pd
from sklearn.cluster import KMeans

data = {
    "AnnualIncome": [15,18,20,25,30,35,40,45,50,55,60,65,70,75,80],
    "SpendingScore": [39,81,6,77,40,76,6,94,3,72,14,99,25,85,30]
}

df = pd.DataFrame(data)

X = df[["AnnualIncome", "SpendingScore"]]

model = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = model.fit_predict(X)

print("Customer Segments:\n")
print(df)

while True:
    income = float(input("\nEnter Annual Income: "))
    score = float(input("Enter Spending Score: "))

    customer = pd.DataFrame({
        "AnnualIncome": [income],
        "SpendingScore": [score]
    })

    cluster = model.predict(customer)

    print("Customer belongs to Cluster:", cluster[0])

    again = input("\nCheck another customer? (yes/no): ").lower()

    if again != "yes":
        print("Thank You!")
        break