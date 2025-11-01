# --- Interactive Histogram Dashboard ---
# Create widgets for filtering
gender_dropdown = widgets.Dropdown(options=['All'] + sorted(df['Gender'].dropna().unique().tolist()), ...)
class_dropdown = widgets.Dropdown(options=['All'] + sorted(df['Class'].dropna().unique().tolist()), ...)
score_slider = widgets.IntSlider(value=0, min=0, max=100, step=5, ...)
output = widgets.Output()

# Define the function that updates the plot
def update_chart(change):
    with output:
        clear_output(wait=True)
        # (Filtering logic based on widget values)
        # (Plotting logic using plt.hist)
        plt.show()
        display(filtered_df.head(10))

# Link widgets to the update function
gender_dropdown.observe(update_chart, names='value')
class_dropdown.observe(update_chart, names='value')
score_slider.observe(update_chart, names='value')

# Display the interactive dashboard
filter_box = widgets.VBox([gender_dropdown, class_dropdown, score_slider])
display(filter_box, output)


# --- PDF Marksheet Generator ---
# Define the function to create a PDF
def generate_marksheet(student_id):
    student = df[df['student_id'] == student_id]
    # ... (ReportLab canvas drawing logic) ...
    c.save()
    print(f"✅ Marksheet saved as: {file_name}")

# Create widgets for PDF generation
student_dropdown = widgets.Dropdown(options=df['student_id'].tolist(), ...)
button = widgets.Button(description="Generate PDF")

# Define the button's click action
def on_button_click(b):
    student_id = student_dropdown.value
    generate_marksheet(student_id)
    file_name = f"student_{student_id}_marksheet.pdf"
    files.download(file_name) # Download the generated PDF

# Link button to the function and display
button.on_click(on_button_click)
display(student_dropdown, button)


# --- Data Export ---
# Save the modified DataFrame to a new CSV file
df.to_csv('students_with_gender.csv', index=False)

# Download the new CSV from Colab
from google.colab import files
files.download('students_with_gender.csv')
