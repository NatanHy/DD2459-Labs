import random
from programs import is_member
from dataclasses import dataclass
from typing import List, Any
import pickle
import itertools

@dataclass
class TestCase:
    inputs : List[Any]

def verdict(lst, key):
    for elm in lst:
        if elm == key:
            return True
    return False

def random_test(num_tests):
    list_len = 10
    list_range = (-10, 10)
    key_range = (-10, 10)

    for _ in range(num_tests):
        random_list = [random.randint(*list_range) for _ in range(list_len)]
        random_key = random.randint(*key_range)

        test_case = TestCase([random_list, random_key])

        yield test_case

def make_test_case(y, list_len) -> TestCase:
    lst = y[:list_len]
    key = y[-1]
    test_case = TestCase([lst[:], key])

    return test_case

def pairwise_test(num_tests):
    list_len = 10
    list_element_typical_values = (-10, 10)
    key_typical_values = (-10, 10)
    list_element_default_values = list(range(0, list_len))
    key_default_value = (key_typical_values[0] + key_typical_values[1]) // 2

    default_values = list_element_default_values + [key_default_value]

    typical_values = [list(range(*list_element_typical_values)) for _ in range(list_len)]
    typical_values.append(list(range(*key_typical_values)))

    for i, l in enumerate(typical_values):
        l.remove(default_values[i])

    for _ in range(num_tests):
        for n in range(3):
            default_indices = itertools.combinations(range(0, list_len+1), n)

            if n == 0:
                yield make_test_case(default_values[:], list_len)
                continue

            for indices in default_indices:
                y = default_values[:]
                for i in indices:
                    y[i] = random.choice(typical_values[i])

                yield make_test_case(y, list_len)

def make_files():
    with open("random.pkl", "wb") as f:
        test_cases = []
        for test_case in random_test(10):
            test_cases.append(test_case)
        pickle.dump(test_cases, f)

    with open("pairwise.pkl", "wb") as f:
        test_cases = []
        for test_case in pairwise_test(1):
            test_cases.append(test_case)
        pickle.dump(test_cases, f)

with open("random.pkl", "rb") as f:
    test_cases : List[TestCase] = pickle.load(f)
    passed = 0
    total = len(test_cases)
    for i, case in enumerate(test_cases):
        print(f"TEST {i}: {case.inputs}")

    print(f"PASSED {passed}/{total}")