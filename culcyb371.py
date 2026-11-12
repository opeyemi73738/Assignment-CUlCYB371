import pandas as pd

ds = {
    "student_id": ["CIS001", "CIS002", "CIS003", "CIS004",],
    "student_department": ["Mass Communication", "English", "Psychology", "Nursing"],
    "student_level": [100, 400, 200, 500],
    "attendance(%)": [85, 92, 78, 88],
    "average_score": [50, 72, 95, 81]
}

df = pd.DataFrame(ds)
print(df)
