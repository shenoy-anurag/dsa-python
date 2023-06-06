from typing import Any, Dict, List, Callable, Text

import termcolor
import numpy as np


PASSED = 'Passed'
FAILED = 'Failed'


class TestCase:
    def __init__(self, test_case: Dict, expected_output: Any) -> None:
        self.input = test_case
        self.output = expected_output

    def compare(self, output, strict=False):
        if strict:
            if output == self.output:
                return PASSED
        else:
            if isinstance(self.output, list):
                is_same = self.compare_lists(output=output)
                return PASSED if is_same else FAILED
            elif isinstance(self.output, tuple):
                is_same = self.compare_tuples(output=output)
                return PASSED if is_same else FAILED
            elif isinstance(self.output, str):
                return PASSED if self.output == output else FAILED
            else:
                return PASSED if self.output == output else FAILED

    def compare_lists(self, output):
        # We have to assume strict=False
        expected_op_set = set(self.output)
        program_op_set = set(output)
        return expected_op_set == program_op_set

    def compare_tuples(self, output):
        # We have to assume strict=False
        expected_op_set = set(self.output)
        program_op_set = set(output)
        return expected_op_set == program_op_set


class TestCasesChecker:
    def __init__(self, test_cases, expected_outputs) -> None:
        self.tests = []
        self.add_test_cases(test_cases=test_cases,
                            expected_outputs=expected_outputs)
        # list containing tuples of the form: (Passed or Failed, Input, Expected Output, Submission Output)
        self.outputs = []

    def add_test_cases(self, test_cases, expected_outputs):
        for (t, o) in zip(test_cases, expected_outputs):
            test_case = TestCase(test_case=t, expected_output=o)
            self.tests.append(test_case)

    def add_new_test_case(self, test_case, expected_output):
        test = TestCase(test_case=test_case, expected_output=expected_output)
        self.tests.append(test)

    def check_code_against_test_cases(self, tests: List[TestCase], fn: Callable, strict_checking=False):
        self.outputs = []
        for i in range(len(tests)):
            test = tests[i]
            output = fn(**test.input)
            result = test.compare(output, strict=strict_checking)
            self.outputs.append([result, test.input, test.output, output])

    def run_test_cases(self, fn, strict_checking=False):
        self.check_code_against_test_cases(
            tests=self.tests, fn=fn, strict_checking=strict_checking)
        return self.outputs


class DisplayResults:
    COLOR_PASSED = "#2cbb5d"
    COLOR_FAILED = "#e64541"

    BORDER = "----------------------------------------------------------------------"
    THICK_BORDER = "======================================================================"
    MINI_BORDER = "---------"

    INPUT = "Input"
    OUTPUT = "Output"
    EXPECTED = "Expected"

    def __init__(self, results: List[List[Any]]) -> None:
        self.results = results

    def display_single_result(self, result):
        output_str = ""
        passed_or_failed, given_input, expected_output, output = result
        if passed_or_failed == PASSED:
            output_str += termcolor.colored(PASSED, 'green') + "\n"
        else:
            output_str += termcolor.colored(FAILED, 'red') + "\n"
        # output_str += self.MINI_BORDER + "\n"
        output_str += self.BORDER + "\n"
        output_str += self.INPUT + ":\n"
        output_str += str(given_input) + "\n"
        output_str += self.OUTPUT + ":\n"
        output_str += str(output) + "\n"
        output_str += self.EXPECTED + ":\n"
        output_str += str(expected_output) + "\n"
        output_str += self.BORDER + "\n"
        return output_str

    def display_results(self):
        output_to_print = ''
        output_to_print += self.BORDER + "\n"
        for i in range(len(self.results)):
            result = self.results[i]
            output_to_print += self.display_single_result(result=result)
        return output_to_print

    def __str__(self) -> str:
        output_to_print = self.display_results()
        return output_to_print


def run_all_test_cases(fn: Callable, test_cases: List[Dict], expected_outputs: List[Any], strict_checking: bool = False) -> DisplayResults:
    tests_runner = TestCasesChecker(
        test_cases=test_cases, expected_outputs=expected_outputs)
    # strict_checking is True because the order of values within the list matters.
    results = tests_runner.run_test_cases(
        fn=fn, strict_checking=strict_checking)

    dr = DisplayResults(results=results)
    return dr


def check_all_passed(dr: DisplayResults):
    results = [r[0] for r in dr.results]
    # print(results)
    passed = [PASSED for _ in range(len(results))]
    # print(passed)
    bool_results = np.isin(np.array(passed), results).tolist()
    # print(bool_results)
    return all(bool_results)


def message_all_passed():
    output_str = ''
    output_str += DisplayResults.THICK_BORDER + "\n"
    output_str += termcolor.colored("All Test Cases Passed!", 'green') + "\n"
    output_str += DisplayResults.THICK_BORDER + "\n"
    return output_str
