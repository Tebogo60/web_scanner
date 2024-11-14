import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


def canConnect(url):
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False


def searchBarCode(barcode):
    url = "https://barcode-list.com/barcode/EN/Search.htm?barcode=" + barcode

    if canConnect(url):
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html.parser")
        result = soup.find("p").text
        print(result)

        table = soup.find("table")
        readTable(table)

    else:
        print("Could not connect to url!")


def readTable(html_table):
    table_data = []

    for row in html_table.find_all("tr"):
        columns = row.find_all(["td", "th"])
        column_data = [col.text.strip() for col in columns]

        if column_data:
            table_data.append(column_data)

    try:
        printTable(table_data)
    except IndexError:
        print("Product Unavailable!")


def printTable(data):
    table = PrettyTable()

    if data:
        table.field_names = data[1]
        for row in data[2:]:
            table.add_row(row)

    print(table)


def prompting():
    enter_input = input("Enter barcode: ")
    searchBarCode(enter_input)


prompting()
