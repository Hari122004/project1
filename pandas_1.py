import pandas as pd

data = {
    ("Sales", "2023"): [100, 200],
    ("Sales", "2024"): [150, 250],
    ("Profit", "2023"): [20, 40],
    ("Profit", "2024"): [30, 60]
}

df = pd.DataFrame(data, index=["Product A", "Product B"])
print(df)