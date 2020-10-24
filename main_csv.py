from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import collections
import csv
import sys
import os


FILE_NAME = sys.argv[-1]


def get_age():
    event1 = datetime.datetime(year=1920, month=12, day=31)
    event2 = datetime.datetime.now()
    age_winery = (event2.year - event1.year)
    return age_winery


def fetch_dict_wines():
    os.system(f"xlsx2csv {FILE_NAME}.xlsx {FILE_NAME}.csv")
    data_exel_df = pandas.read_csv(f"{FILE_NAME}.csv",
                                    dtype={ "Категория":str,
                                            "Название":str,
                                            "Сорт":str,
                                            "Цена":int,
                                            "Картинка":str,
                                            "Акция":str },
                                    na_values=['N/A', 'NA'],
                                    keep_default_na=False)

    data_exel_df.rename(columns={"Категория":"category",
                                 "Название":"name",
                                 "Сорт":"sort",
                                 "Цена":"price",
                                 "Картинка":"img",
                                 "Акция":"sale"},
                        inplace=True)

    wine_dicts = data_exel_df.to_dict(orient="record")
    dict_of_lists = collections.defaultdict(list)
    for wine_description in wine_dicts:
        key_category = wine_description["category"]
        dict_of_lists[key_category].append(wine_description)
    return dict_of_lists


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(age_winery=get_age(), wines=fetch_dict_wines())

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
