# 📘 Student Exam Scores Dashboard — Code Reference

This file contains only the executable code used in the **Student Exam Scores Analytical Dashboard Notebook**.

---

## 1️⃣ Setup
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CSV_PATH = "/content/student_exam_scores_updated.csv"
df = pd.read_csv(CSV_PATH, dtype=str, keep_default_na=False)
df.head()
```

---

## 2️⃣ Attendance-Based Performance
```python
df['Attendance Marks'] = pd.to_numeric(df['Attendance Marks'], errors='coerce').fillna(0)
df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0)

plt.figure()
plt.scatter(df['Attendance Marks'], df['Total'])
plt.title('Attendance Marks vs Total Marks')
plt.xlabel('Attendance Marks')
plt.ylabel('Total Marks')
plt.tight_layout()
plt.show()

df[['Attendance Marks', 'Total']].corr()
```

---

## 3️⃣ Gender-Specific Insights
```python
if 'Gender' in df.columns:
    df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0)
    gender_summary = df.groupby('Gender').agg({'Total':'mean','Attendance Marks':'mean','Percentage':'mean'}).round(2)
    print(gender_summary)
    gender_summary.plot(kind='bar', title='Average Scores by Gender', figsize=(7,4))
    plt.ylabel('Average Score')
    plt.tight_layout()
    plt.show()
```

---

## 4️⃣ Histograms
```python
numeric_cols = ['Total', 'Attendance Marks', 'Percentage']
for col in numeric_cols:
    if col in df.columns:
        plt.figure()
        pd.to_numeric(df[col], errors='coerce').dropna().plot(kind='hist', bins=20, title=f'Distribution of {col}')
        plt.xlabel(col)
        plt.tight_layout()
        plt.show()
```

---

## 5️⃣ Lists: Above Average, Below Average, Fail, No Attendance
```python
avg_total = pd.to_numeric(df['Total'], errors='coerce').mean()
df['Total'] = pd.to_numeric(df['Total'], errors='coerce')

above_avg = df[df['Total'] > avg_total]
below_avg = df[(df['Total'] <= avg_total) & (df['Total'] > 0)]
failed = df[df['Grade'] == 'F'] if 'Grade' in df.columns else pd.DataFrame()
no_attendance = df[(df['Attendance Marks'] == 0) | (df['Attendance Marks'].isna())]

print('Average Total:', round(avg_total, 2))
print('\nAbove Average Students:', len(above_avg))
print('\nBelow Average Students:', len(below_avg))
print('\nFailed Students:', len(failed))
print('\nDid not attend any class:', len(no_attendance))
```

---

## 6️⃣ Yearly Registration Trends & Gender-Based Registration
```python
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
year_counts = df['Year'].value_counts().sort_index()

plt.figure()
year_counts.plot(kind='bar', title='Yearly Student Registrations', figsize=(6,4))
plt.xlabel('Year')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.show()

current_year = df['Year'].max()
gender_year = df[df['Year'] == current_year].groupby('Gender').size()
print(f'Number of students by gender registered in {int(current_year)}:')
print(gender_year)
```
---


##  7️⃣ As a developer, I want to create a script that generates a dashboard displaying the top-performing and most frequently attending students, so I can easily interpret the data.

```python



# 7.1 Top-performing students (by Total marks)
top_performers_cols = ['student_id', 'Total']
if 'Percentage' in df.columns:
    df['Percentage'] = pd.to_numeric(df['Percentage'], errors='coerce').fillna(0)
    top_performers_cols.append('Percentage')

top_performers = (
    df.sort_values('Total', ascending=False)
      .head(TOP_N)[top_performers_cols]
)

print(f"\n🏆 Top {TOP_N} Performing Students (by Total marks):")
print(top_performers)

plt.figure()
plt.bar(top_performers['student_id'], top_performers['Total'])
plt.title(f'Top {TOP_N} Performing Students (by Total Marks)')
plt.xlabel('Student ID')
plt.ylabel('Total Marks')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 7.2 Most frequently attending students (by Attendance Marks)
top_attendance = (
    df.sort_values('Attendance Marks', ascending=False)
      .head(TOP_N)[['student_id', 'Attendance Marks']]
)

print(f"\n📚 Top {TOP_N} Most Frequently Attending Students:")
print(top_attendance)

plt.figure()
plt.bar(top_attendance['student_id'], top_attendance['Attendance Marks'])
plt.title(f'Top {TOP_N} Most Frequently Attending Students')
plt.xlabel('Student ID')
plt.ylabel('Attendance Marks')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


```
---
