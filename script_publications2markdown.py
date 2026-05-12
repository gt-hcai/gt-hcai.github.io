import csv 
import pandas as pd 

df = pd.read_csv('HCAI Publications-Table1.csv')
sorted_df = df.sort_values(by=["YEAR", "AUTHORS"], ascending=[False, True])

print(sorted_df.head())

markdown_lines = []
for _, row in sorted_df.iterrows():
    authors = row["AUTHORS"]
    title = row["PUPLICATION TITLE"]
    year = row["YEAR"]
    conference = row["CONFERENCE / JOURNAL"]
    url = row["URL"]
    markdown_line = f"- {authors} ({year}). **{title}**. *{conference}*. [{url}]({url})"
    markdown_lines.append(markdown_line)

markdown_output = "\n".join(markdown_lines)

# Save to a markdown file
with open("publications.md", "w", encoding="utf-8") as f:
    f.write(markdown_output)