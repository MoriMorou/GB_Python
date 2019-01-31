# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех
# предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
# предприятий, чья прибыль ниже среднего.

from collections import namedtuple


def create_company (items, companies):
    Company= namedtuple('Company', ['name', 'q1', 'q2', 'q3', 'q4'])
    item = 0
    while item < items:
        name = input("Input company name ")
        profit_YTD = [float(profit) for profit in input("Input profit for each quarter ").split()]
        companies.append(Company(name, *profit_YTD))
        item += 1


def get_avg_profit(items, companies):
    spam = 0
    for company in companies:
        for profit in company[1:]:
            spam += profit
            # print(spam / items)
    return spam / items


def get_high_company(companies, all_avg_profit):
    for company in companies:
        if sum(company[1:]) > all_avg_profit:
            print(company.name)


def get_lower_company(companies, all_avg_profit):
    for company in companies:
        if sum(company[1:]) < all_avg_profit:
            print(company.name)


if __name__ == '__main__':
    items = int(input("Input the number of a companies "))
    companies = []
    if items > 0:
        create_company(items, companies)
        avg_profit = get_avg_profit(items, companies)
        print("Companies with annual profits above average: ")
        get_high_company(companies, avg_profit)
        print("Companies with annual profits below average: ")
        get_lower_company(companies, avg_profit)
    else:
        print("Error, wrong number. Please try again")
