import pandas as pd
from collections import Counter
import numpy as np

def count_skills(row):
    return Counter(np.concatenate(row) if isinstance(row, np.ndarray) else row).most_common(20)


def skills(csv_file_name: str, by_year_csv: str, by_year_file_html: str):
    df = pd.read_csv(csv_file_name,
                     parse_dates=["published_at"],
                     low_memory=False)

    df = df[~df["key_skills"].isna()]
    df["key_skills"] = df["key_skills"].apply(lambda x: x.split("\n"))
    df["year"] = df["published_at"].apply(lambda x: x.year)

    skills_by_year = df.groupby("year")["key_skills"].agg(lambda x: x).apply(count_skills)
    skills_by_year.to_csv(by_year_csv)

    skills_by_year = skills_by_year.apply(lambda x: ", ".join([f"{skill}: {count}" for (skill, count) in x]))
    skills_by_year.reset_index().to_html(by_year_file_html, index=False)


def main():
    skills("vacancies.csv",
           "result_files/skills/skill_by_year.csv",
           "result_files/skills/skill_by_year.html")

    skills("python_vacancies.csv",
           "result_files/skills/python_skill_by_year.csv",
           "result_files/skills/python_skill_by_year.html")


if __name__ == "__main__":
    main()
