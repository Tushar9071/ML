import sweetviz as sv
import pandas as pd

# Load the dataset
df = pd.read_csv('./Data Set/train.csv')
print(df.head())

# Generate the report
report = sv.analyze(df)

# Save the report to an HTML file
report.show_html("sweetviz_report.html")  # Opens in your browser
