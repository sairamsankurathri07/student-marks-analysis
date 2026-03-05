import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name":["Rahul","anita","kiran","sneha","arjun"],
    "Math":[78,85,90,66,88],
    "Science":[82,79,94,70,85],
    "English":[74,88,89,60,80],
}

df = pd.DataFrame(data)

df["Average"] = df[["Math","Science","English"]].mean(axis=1)

print("Students Data:\n")
print(df)

print("\nClass Average:",df["Average"].mean())

plt.bar(df["Name"],df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Students Average Marks")
plt.show()