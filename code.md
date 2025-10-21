# Student Exam Scores Analysis

## 📁 Project Files
- `student_exam_scores.ipynb` - Main Jupyter notebook with data analysis
- `student_exam_scores.csv` - Dataset containing student exam information

## 🛠️ Technologies Used
- **Python 3**
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **Google Colab** - Cloud-based Jupyter notebook environment

## 📊 Dataset Structure
The dataset contains the following columns:
- `student_id` - Unique identifier for each student
- `hours_studied` - Number of hours studied
- `sleep_hours` - Hours of sleep
- `attendance_percent` - Attendance percentage
- `previous_scores` - Previous exam scores
- `exam_score` - Current exam score

## 🔧 Code Commands & Functions

### 1. Data Upload & Import
```python
# Upload file to Google Colab
from google.colab import files
uploaded = files.upload()

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_exam_scores.csv")

# Display first few rows
df.head()

# Display entire dataset
df

# Check for empty dataset
if df.empty:
    print("The file is empty!")
else:
    print("The file has data.")

# Check for missing values
print(df.isnull().sum())


