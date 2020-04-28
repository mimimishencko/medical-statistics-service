from __future__ import print_function
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import uuid
import os
import pathlib


class ReportGen:
    def __init__(self):
        self.ROOT = str(pathlib.Path().absolute())
        self.ASSETS_DIR = os.path.join(self.ROOT, 'assets').strip()
        self.env = Environment(loader=FileSystemLoader('./data_methods'))

    def for_descriptive(self, data, summary, unique_filename, distr_summary):
        template = self.env.get_template("descriptive_stat_temp.html")

        template_vars = {"title": "Descriptive Statistics",
                         "descriptive_stat_table": data.to_html(),
                         "assets_dir": 'file://' + self.ASSETS_DIR,
                         "unique_filename": unique_filename,
                         "summary": summary,
                         "distr_summary": distr_summary}
        print('file://' + self.ASSETS_DIR+'/histogram-'+template_vars["unique_filename"]+'.jpg')
        self.generate_pdf(template, template_vars, 'descriptive')

    def for_wilcoxon(self, rang_table, n, w_obs, w_cr, alpha):
        template = self.env.get_template("test_report.html")

        template_vars = {"title": "Wilcoxon test",
                         "rang_table": rang_table.to_html(),
                         "n": n,
                         "W_obs": w_obs,
                         "W_cr": w_cr,
                         "alpha": alpha,
                         }
        self.generate_pdf(template, template_vars, 'Wilcoxon')

    def for_friedman(self, chi, critical, p, df, df_ranges, n, k):
        template = self.env.get_template("friedman_report.html")
        template_vars = {"title": "Friedman test",
                         "rang_table": df_ranges.to_html(),
                         "default_table": df.to_html(),
                         "n": n,
                         "k": k,
                         "Chi": chi,
                         "critical": critical,
                         "p": p,
                         "chi2_img": f"file://{self.ROOT}/data_methods/img/chi2_r.png"
                         }
        print(template_vars["chi2_img"])
        self.generate_pdf(template, template_vars, 'Friedman')

    def generate_pdf(self, template, template_vars, name):

        self.env = Environment(loader=FileSystemLoader('./data_methods'))

        html_out = template.render(template_vars)

        unique_filename = str(uuid.uuid4())

        HTML(string=html_out).write_pdf(f"{name}-{unique_filename}.pdf", presentational_hints=True)
