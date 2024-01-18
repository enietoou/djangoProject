import pandas as pd

def geography(csv_file: str, salary_by_city_csv: str,
              vacs_by_city_csv: str, salary_by_city_html: str,
              vacs_by_city_file_html: str):
    df = pd.read_csv(csv_file, low_memory=False)

    vacs_by_city = (df.groupby("area_name").count()[["name"]]
                                         .sort_values(ascending=False, by="name"))
    vacs_by_city.columns = ["count"]
    vacs_by_city["percent"] = (vacs_by_city["count"] / len(df)) * 100

    vacs_by_city.to_csv(vacs_by_city_csv, float_format=lambda x: f"{x:.5f}")
    vacs_by_city.to_html(vacs_by_city_file_html, float_format=lambda x: f"{x:.5f}")

    df = df[~(df["salary"].isna()) & (df["salary"] < 100_000_000)]

    salary_by_city = df.groupby("area_name")["salary"].mean().sort_values(ascending=False).reset_index()
    salary_by_city = salary_by_city[salary_by_city["area_name"].isin(vacs_by_city.reset_index()["area_name"])]

    salary_by_city.to_csv(salary_by_city_csv, float_format=lambda x: f"{x:.2f}", index=False)
    salary_by_city.to_html(salary_by_city_html, float_format=lambda x: f"{x:.2f}", index=False)


def main():
    geography("vacancies_rub.csv",
              "result_files/geography/salary_by_city.csv",
              "result_files/geography/vacs_by_city.csv",
              "result_files/geography/salary_by_city.html",
              "result_files/geography/vacs_by_city.html")

    geography("python_vacancies_rub.csv",
              "result_files/geography/python_salary_by_city.csv",
              "result_files/geography/python_vacs_by_city.csv",
              "result_files/geography/python_salary_by_city.html",
              "result_files/geography/python_vacs_by_city.html")


if __name__ == "__main__":
    main()