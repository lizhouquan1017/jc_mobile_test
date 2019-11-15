
import unittest
from BeautifulReport import BeautifulReport
from os import path
from tomorrow import threads

parent_path = path.dirname(path.dirname(__file__))
casepath = path.join(parent_path, "debug_case")
reportpath = path.join(parent_path, "reports")

print(parent_path)
print(casepath)


def add_case(case_path=casepath, rule="test_05_purchaseorder_module.py"):

    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover


# @threads(2)
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html', description='jxc_test', log_path='reports')


if __name__ == "__main__":
    cases = add_case()
    print(cases)
    for i in cases:
        print(i)
        run(i)
