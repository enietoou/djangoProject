import json
from dateutil import parser
import requests


def salary(salary: dict):
    if salary is None:
        return None

    salary_from = salary["from"]
    salary_to = salary["to"]
    avg_salary = {}
    if salary_to is None and salary_from is None:
        return None

    if salary_to is None or salary_from is None:
        avg_salary["value"] = salary_to or salary_from
    else:
        avg_salary["value"] = f"{(salary_from + salary_to) / 2:.2f}"

    avg_salary["currency"] = salary["currency"] if salary["currency"] is not None else "RUR"
    return avg_salary


def prepare_vacancy_from_hh(vacancy):
    formatted_vacancy = {
        "name": vacancy["name"],
        "employer": vacancy["employer"]["name"],
        "salary": salary(vacancy["salary"]),
        "area_name": vacancy["area"]["name"],
        "published_at": parser.parse(vacancy["published_at"])
    }
    url = f'https://api.hh.ru/vacancies/{vacancy["id"]}'
    response = requests.get(url)
    additional_info = json.loads(response.content.decode())

    formatted_vacancy["description"] = additional_info["description"]
    formatted_vacancy["key_skills"] = ", ".join([skill["name"] for skill in additional_info["key_skills"]])
    return formatted_vacancy


def get_vacancies_from_hh_api(profession):
    url = f"https://api.hh.ru/vacancies?text={profession}&period=1&per_page=10&order_by=publication_time&sort_order=desc"

    response = requests.get(url)
    if response.status_code == 200:
        vacancies_data = response.json()["items"]
        vacs = [prepare_vacancy_from_hh(vacancy_data) for vacancy_data in vacancies_data]
        return vacs
    else:
        None