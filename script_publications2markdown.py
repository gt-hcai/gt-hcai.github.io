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
    if not isinstance(url, float):
        markdown_line = f"- {authors} ({year}). **{title}**. *{conference}*. [{url}]({url})"
    else:
        markdown_line = f"- {authors} ({year}). **{title}**. *{conference}*"
    markdown_lines[year][conference].append(markdown_line)

# markdown_output = "\n".join(markdown_lines)

# Save to a markdown file
with open("_pages/publications.md", "w", encoding="utf-8") as f:
    f.write("---\n")
    f.write("permalink: /publications/\n")
    f.write("title: \"Publications\"\n")
    f.write("excerpt: \"\"\n")
    f.write("last_modified_at: 2026-05-12T11:59:26-04:00\n")
    f.write("toc: true\n")
    f.write("layout: single\n")
    f.write("---\n")
    f.write("\n")
    f.write("On this page, we present a selection of publications by members of the HCAI working group. Feel free to visit the authors' pages for complete lists.\n")
    f.write("\n")
    for y in sorted(markdown_lines.keys(), reverse=True):
        f.write(f"\n\n# {y}\n")
        for c in sorted(markdown_lines[y].keys()):
            f.write(f"\n\n## {c}\n")
            markdown_output = "\n".join(markdown_lines[y][c])
            f.write(markdown_output)
            print(y, c, len(markdown_lines[y][c]))
            # if len(markdown_lines[y][c]) == 1:
            #     f.write("\n")