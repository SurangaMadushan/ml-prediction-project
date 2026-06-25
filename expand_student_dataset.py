import pandas as pd
import numpy as np
import os

# Load original small dataset
input_path = "data/student_performance.csv"
df = pd.read_csv(input_path)

# Repeat and slightly perturb the data to create a larger practice dataset
expanded_rows = []

np.random.seed(42)

for _ in range(15):   # 20 rows x 15 = around 300 rows
    temp = df.copy()

    # add small random noise to score columns
    for col in ["math score", "reading score", "writing score"]:
        noise = np.random.randint(-5, 6, size=len(temp))
        temp[col] = temp[col] + noise
        temp[col] = temp[col].clip(lower=0, upper=100)

    expanded_rows.append(temp)

expanded_df = pd.concat(expanded_rows, ignore_index=True)

# shuffle rows
expanded_df = expanded_df.sample(frac=1, random_state=42).reset_index(drop=True)

# save expanded dataset
os.makedirs("data", exist_ok=True)
output_path = "data/student_performance_expanded.csv"
expanded_df.to_csv(output_path, index=False)

print("Expanded dataset created successfully!")
print("Saved at:", output_path)
print("Shape:", expanded_df.shape)
print(expanded_df.head())