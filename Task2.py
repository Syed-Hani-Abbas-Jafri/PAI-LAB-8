import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", keep_default_na=False)
d2 = df[df["scenario"] == "02_MonthlySales"].copy()

plt.figure(figsize=(9, 5))
for company, group in d2.groupby("school_type"):
    plt.plot(
        group["study_hours"],
        group["exam_score"],
        marker="o",
        label=company
    )
plt.title("Monthly Revenue Trends (Jan - Jun 2023)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.legend()
plt.tight_layout()
plt.show()