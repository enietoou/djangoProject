import math
import pandas as pd

valute_csv = "currency.csv"

def convert_salary_to_rub(currency_df):
    def _inner(row):
        if row["salary_currency"] == "RUR" or row.isna()["salary_currency"] or row.isna()["salary"]:
            return row

        published_at = row["published_at"].normalize().replace(day=1).tz_localize(None)
        curr_in_month = currency_df.loc[published_at]
        rate = curr_in_month[row["salary_currency"]]

        if math.isnan(rate):
            row["salary"] = math.nan
            return row

        row["salary"] = math.floor(rate * row["salary"])
        return row

    return _inner


def process_csv(input_csv, output_csv):
    df_currency = pd.read_csv(valute_csv, index_col='date', parse_dates=["date"])
    result_csv = pd.read_csv(input_csv, parse_dates=["published_at"], low_memory=False)

    result_csv["salary"] = result_csv[["salary_from", "salary_to"]].mean(axis=1)

    result_csv = result_csv.apply(convert_salary_to_rub(df_currency), axis=1)
    result_csv = result_csv[["name", "salary", "area_name", "published_at"]]
    result_csv["published_at"] = result_csv["published_at"].apply(lambda date: date.strftime("%Y-%m-%dT%T%z"))
    result_csv.to_csv(output_csv, index=False)


def main():
    process_csv("python_vacancies.csv",
                "python_vacancies_rub.csv")

    process_csv("vacancies.csv",
                "vacancies_rub.csv")


if __name__ == "__main__":
    main()