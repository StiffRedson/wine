from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas as pd
import collections
import sys


FILE_NAME = sys.argv[-1]
COLUMN_FILE = ["Категория", "Название", "Сорт", "Цена", "Картинка", "Акция"]
COLUMN_RENAME = {
                    "Категория":"category",
                    "Название":"name",
                    "Сорт":"sort",
                    "Цена":"price",
                    "Картинка":"img",
                    "Акция":"sale"
                }

def get_age():
    event1 = datetime.datetime(year=1920, month=12, day=31)
    event2 = datetime.datetime.now()
    age_winery = (event2.year - event1.year)
    return age_winery


def fetch_dict_wines():
    data_exel_df = pd.read_excel(f"{FILE_NAME}.xlsx",
                                sheet_name='Лист1',
                                usecols=COLUMN_FILE,
                                na_values=['N/A', 'NA'],
                                keep_default_na=False)

    data_exel_df.rename(columns=COLUMN_RENAME,
                        inplace=True)

    wine_dicts = data_exel_df.to_dict(orient="record")
    dict_of_lists = collections.defaultdict(list)
    for wine_description in wine_dicts:
        key_category = wine_description["category"]
        dict_of_lists[key_category].append(wine_description)
    return dict_of_lists


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    try:
        rendered_page = template.render(age_winery=get_age(), wines=fetch_dict_wines())
    except ValueError:
        print(f"No sale today\n{sys.exc_info()[1]}")
        COLUMN_FILE.remove("Акция")
        rendered_page = template.render(age_winery=get_age(), wines=fetch_dict_wines())
    except Exception:
        exit(sys.exc_info()[1])

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
