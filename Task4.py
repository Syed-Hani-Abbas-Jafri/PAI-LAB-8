import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv", keep_default_na=False)
d4 = df[df["scenario"] == "04_CustAgeDist"].copy()
d4["age"] = d4["prep_course"].astype(int)
d4["gender"] = d4["study_hours"]

plt.figure(figsize=(8, 5))
sns.histplot(
    data=d4,
    x="age",
    hue="gender",
    bins=5,
    kde=True
)
plt.title("Customer Age Distribution by Gender")
plt.xlabel("Age")
plt.ylabel("Customer Count")
plt.tight_layout()
plt.show()