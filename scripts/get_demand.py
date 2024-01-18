import pandas as pd

def demand(csv_file: str, salary_output_csv: str, count_output_csv: str,
        salary_html_table: str, count_html_table: str):
    df = pd.read_csv(csv_file, parse_dates=["published_at"], low_memory=False)

    df["year"] = df["published_at"].apply(lambda x: x.year)

    count_by_year = df.groupby("year").count()[["name"]]
    count_by_year.columns = ["count"]
    count_by_year.to_csv(count_output_csv)
    count_by_year.to_html(count_html_table)

    df = df[~(df["salary"].isna()) & (df["salary"] < 100_000_000)]

    salary_by_year = df.groupby("year")["salary"].mean().reset_index()
    salary_by_year.to_csv(salary_output_csv, index=False, float_format=lambda x: f"{x:.2f}")

    salary_by_year.to_html(salary_html_table, index=False, float_format=lambda x: f"{x:.2f}")


def main():
    demand("python_vacancies_rub.csv",
            "result_files/demand/python_dynamic_salary_by_year.csv",
            "result_files/demand/python_dynamic_count_by_year.csv",
           "result_files/demand/python_dynamic_salary_by_year.html",
           "result_files/demand/python_dynamic_count_by_year.html")

    demand("vacancies_rub.csv",
              "result_files/demand/dynamic_salary_by_year.csv",
              "result_files/demand/dynamic_count_by_year.csv",
           "result_files/demand/dynamic_salary_by_year.html",
           "result_files/demand/dynamic_count_by_year.html")


if __name__ == "__main__":
    main()
