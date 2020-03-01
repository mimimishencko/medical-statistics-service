
from __future__ import print_function
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import uuid
import os


def generate_pdf(data, summary, unique_filename):
    ROOT = '/Users/anastasia/Desktop/math_stat_methods/src'
    ASSETS_DIR = os.path.join(ROOT, 'assets')

    env = Environment(loader=FileSystemLoader('./data_methods'))
    template = env.get_template("descriptive_stat_temp.html")

    template_vars = {"title" : "Descriptive Statistics",
                     "descriptive_stat_table": data.to_html(),
                     "assets_dir": 'file://' + ASSETS_DIR,
                     "unique_filename": unique_filename,
                     "summary": summary}

    html_out = template.render(template_vars)

    unique_filename = str(uuid.uuid4())

    HTML(string=html_out).write_pdf(f"{unique_filename}.pdf", presentational_hints=True)



