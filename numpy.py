import numpy as np
import pandas as pd

np.random.seed(42)

num_students = 10

names = [f"Student_{i}" for i in range(1, num_students + 1)]
marks = np.random.randint(40, 100, size=num_students)
attendance = np.random.randint(50, 101, size=num_students)
iq = np.random.normal(loc=100, scale=15, size=num_students).astype(int)

df = pd.DataFrame({
    "Name": names,
    "Marks": marks,
    "Attendance (%)": attendance,
    "IQ": iq
})

sample_data = df.sample(n=3)
shuffled_df = df.sample(frac=1)
random_marks = np.random.choice(marks, size=5)

print("\nFull Dataset:\n")
print(df)

print("\nRandom Sample:\n")
print(sample_data)

print("\nShuffled Dataset:\n")
print(shuffled_df)

print("\nRandom Marks Selection:\n")
print(random_marks)

df.to_csv("student_dataset.csv", index=False)
print("\nDataset saved as student_dataset.csv")