import csv 
import pandas as pd 

df = pd.read_csv('HCAI Publications-Table1.csv')
sorted_df = df.sort_values(by=["YEAR", "AUTHORS"], ascending=[False, True])

print(sorted_df.head())

markdown_lines = {}
for _, row in sorted_df.iterrows():
    authors = row["AUTHORS"]
    title = row["PUPLICATION TITLE"]
    year = row["YEAR"]
    conference = row["CONFERENCE / JOURNAL"]
    url = row["URL"]
    if year not in markdown_lines.keys():
        markdown_lines[year] = {}
    if conference not in markdown_lines[year].keys():
        markdown_lines[year][conference] = []
    markdown_line = f"- {authors} ({year}). **{title}**. *{conference}*. [{url}]({url})"
    markdown_lines[year][conference].append(markdown_line)

# markdown_output = "\n".join(markdown_lines)

# Save to a markdown file
with open("publications.md", "w", encoding="utf-8") as f:
    for y in sorted(markdown_lines.keys(), reverse=True):
        f.write(f"# {y}\n")
        for c in sorted(markdown_lines[y].keys()):
            f.write(f"# {c}\n")
            markdown_output = "\n".join(markdown_lines[y][c])
            f.write(markdown_output)
            print(y, c, len(markdown_lines[y][c]))
            if len(markdown_lines[y][c]) == 1:
                f.write("\n")