import json
from dateutil import parser
import requests

return_message = {
    'salary': 'Не указан',
    'employer': 'Не указана',
    'area_name': 'Не указан',
    'description': 'Не указано',
    'key_skills': 'Не указаны',
}

def salary(salary: dict):
    if salary is None:
        return return_message['salary']

    salary_from = salary["from"]
    salary_to = salary["to"]
    formatted_salary = ''
    if salary_to is None and salary_from is None:
        return return_message['salary']

    if salary_to is None or salary_from is None:
        sal = salary_to or salary_from
        formatted_salary += str(sal)
    else:
        formatted_salary += f"{salary_from} - {salary_to}"

    currency = salary["currency"] if salary["currency"] is not None else "RUR"
    return formatted_salary + " " + currency


def prepare_vacancy_from_hh(vacancy):
    formatted_vacancy = {
        "name": vacancy["name"],
        "employer": vacancy["employer"]["name"] if vacancy["employer"]["name"] is not None else return_message['employer'],
        "salary": salary(vacancy["salary"]),
        "area_name": vacancy["area"]["name"] if vacancy["area"]["name"] is not None else return_message['area_name'],
        "published_at": parser.parse(vacancy["published_at"])
    }
    url = f'https://api.hh.ru/vacancies/{vacancy["id"]}'
    response = requests.get(url)
    additional_info = json.loads(response.content.decode())

    formatted_vacancy["description"] = additional_info["description"] if additional_info["description"] is not None else return_message['description']

    formatted_vacancy["key_skills"] = ", ".join([skill["name"] for skill in additional_info["key_skills"]])
    formatted_vacancy["key_skills"] = formatted_vacancy["key_skills"] if formatted_vacancy["key_skills"] is not None else return_message['key_skills']
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