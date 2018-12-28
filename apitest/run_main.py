import os

from cmq.tlib.run import run_cases_by_htmlrunner, load_modules


def run():
    path = os.path.join(os.getcwd(), 'cases_config.txt')
    ls = load_modules(path)
    run_cases_by_htmlrunner(ls, {}, os.getcwd())


if __name__ == '__main__':
    run()
