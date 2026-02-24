import random
from programs import is_member
from dataclasses import dataclass
from typing import List, Any
import pickle
import itertools

import multiprocessing as mp

def run_tests(test_cases, q):
    for i, case in enumerate(test_cases):
        try:
            res = is_member(*case.inputs)
        except Exception:
            res = None

        expected = verdict(*case.inputs)

        if res != expected:
            q.put(i, res)
            break


def run_with_timeout(test_cases, timeout=1):
    q = mp.Queue()

    p = mp.Process(target=run_tests, args=(test_cases, q))
    p.start()
    p.join(timeout)

    if p.is_alive():
        p.terminate()
        p.join()
        return "Timeout"  # timeout result

    return q.get() if not q.empty() else "Not found"

@dataclass
class TestCase:
    inputs : List[Any]

def verdict(lst, key):
    for elm in lst:
        if elm == key:
            return True
    return False

def random_test(num_tests):
    list_len = 100
    list_range = (-50, 50)
    key_range = (-50, 50)

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
    list_len = 100
    list_element_typical_values = (-50, 50)
    key_typical_values = (-50, 50)
    list_element_default_values = list(range(0, list_len))
    key_default_value = (key_typical_values[0] + key_typical_values[1]) // 2

    default_values = list_element_default_values + [key_default_value]

    typical_values = [list(range(*list_element_typical_values)) for _ in range(list_len)]
    typical_values.append(list(range(*key_typical_values)))

    for i, l in enumerate(typical_values):
        if default_values[i] in l:
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
        for test_case in random_test(1000):
            test_cases.append(test_case)
        pickle.dump(test_cases, f)

    with open("pairwise.pkl", "wb") as f:
        test_cases = []
        for test_case in pairwise_test(10):
            test_cases.append(test_case)
        pickle.dump(test_cases, f)

def eval_test_cases(file_name):
    with open(file_name, "rb") as f:
        test_cases : List[TestCase] = pickle.load(f)
        
    res = run_with_timeout(test_cases)
        
    return res

if __name__ == "__main__":
    # make_files()
    random_until_fail = eval_test_cases("random.pkl")
    pairwise_until_fail = eval_test_cases("pairwise.pkl")

    print(random_until_fail)
    print(pairwise_until_fail)
