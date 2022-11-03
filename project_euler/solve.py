import argparse
import importlib
import sys
import time

from project_euler.util.answers import answer_list


argparser = argparse.ArgumentParser()
argparser.add_argument("problem_number", help="The project euler problem number to run the solution for.", type=int)
args = argparser.parse_args()
try:
    problem_number_module = importlib.import_module(f"project_euler.solutions.s{args.problem_number:04}")
    print(f"solution {args.problem_number}")
    start_time = time.process_time_ns()
    your_answer = problem_number_module.get_answer()
    total_time = time.process_time_ns() - start_time
    print(f"time taken: {total_time / 1000000000:.3f}s")
    correct_answer = answer_list[args.problem_number]
    print(f"your answer:    {your_answer}")
    print(f"correct answer: {correct_answer}")
    if your_answer == correct_answer:
        print("✅ you got it!")
    else:
        print("❌ back to the drawing board")
        sys.exit(1)
except ModuleNotFoundError:
    print(f"couldn't find solution to problem number {args.problem_number}")
    sys.exit(1)