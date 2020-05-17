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
        self.env = Environment(loader=FileSystemLoader('./report_generator/templates/'))

    def for_descriptive(self, data, summary, unique_filename, distr_summary, confidence_mean, confidence_variance):
        template = self.env.get_template("descriptive_stat_temp.html")

        template_vars = {"title": "Descriptive Statistics",
                         "descriptive_stat_table": data.to_html(),
                         "assets_dir": 'file://' + self.ASSETS_DIR,
                         "unique_filename": unique_filename,
                         "summary": summary,
                         "confidence_mean": confidence_mean,
                         "confidence_mean_formula": f"file://{self.ROOT}/report_generator/img/ci_mean.png",
                         "confidence_variance_formula": f"file://{self.ROOT}/report_generator/img/ci_variance.png",
                         "confidence_variance": confidence_variance,
                         "distr_summary": distr_summary}
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

    def for_friedman(self, chi, critical, p, df, df_ranges, n, k, p_value, alpha):
        template = self.env.get_template("friedman_report.html")
        template_vars = {"title": "Friedman test",
                         "rang_table": df_ranges.to_html(),
                         "default_table": df.to_html(),
                         "n": n,
                         "k": k,
                         "Chi": chi,
                         "critical": critical,
                         "p": p,
                         "chi2_img": f"file://{self.ROOT}/report_generator/img/chi2_r.png",
                         "friedman_stat": f"file://{self.ROOT}/report_generator/img/friedman_stat.png",
                         "n_img": f"file://{self.ROOT}/report_generator/img/n.png",
                         "k_img": f"file://{self.ROOT}/report_generator/img/k.png",
                         "R_m": f"file://{self.ROOT}/report_generator/img/R_m.png",
                         "p_value": p_value,
                         "alpha": alpha,
                         }
        self.generate_pdf(template, template_vars, 'Friedman')

    def for_student(self, stat, critical, df, n, k, p_value, alpha, test, is_independent, expected):
        template = self.env.get_template("student_report.html")
        template_vars = {"title": "Friedman test",
                         "default_table": df.to_html(),
                         "n": n,
                         "k": k,
                         "test": test,
                         "is_independent": is_independent,
                         "critical": critical,
                         "stat": stat,
                         "p_value": p_value,
                         "alpha": alpha,
                         "expected": expected,
                         "welch_stat": f"file://{self.ROOT}/report_generator/img/welch_stat.png",
                         "n_img": f"file://{self.ROOT}/report_generator/img/n.png",
                         "m_img": f"file://{self.ROOT}/report_generator/img/m.png",
                         }
        self.generate_pdf(template, template_vars, 'Student')

    def for_mann_whitney(self, stat, critical, n1, n2, p_value, alpha, expected, accepted):
        template = self.env.get_template("mann_whitney_report.html")
        template_vars = {"title": "Mann-Whitney test",
                         # "var_1": var_1.to_html(),
                         # "var_2": var_2.to_ntml(),
                         "n1": n1,
                         "n2": n2,
                         "critical": critical,
                         "stat": stat,
                         "p_value": p_value,
                         "alpha": alpha,
                         "expected": expected,
                         "accepted": accepted,
                         "mann_stat": f"file://{self.ROOT}/report_generator/img/mann_stat.png",
                         "mann_norm": f"file://{self.ROOT}/report_generator/img/mann_norm.png",
                         "U":f"file://{self.ROOT}/report_generator/img/U.png",
                         "n_img": f"file://{self.ROOT}/report_generator/img/n.png",
                         "m_img": f"file://{self.ROOT}/report_generator/img/m.png",
                         "R_i": f"file://{self.ROOT}/report_generator/img/R_i.png",
                         }
        self.generate_pdf(template, template_vars, 'Mann-Whitney')

    def generate_pdf(self, template, template_vars, name):

        self.env = Environment(loader=FileSystemLoader('./report_generator'))

        html_out = template.render(template_vars)

        unique_filename = str(uuid.uuid4())

        HTML(string=html_out).write_pdf(f"{name}-{unique_filename}.pdf", presentational_hints=True)
