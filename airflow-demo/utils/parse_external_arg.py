import sys

DEFAULT_VAR = "test123"

def extract_parameters() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    return DEFAULT_VAR

def print_something(test_var: str = DEFAULT_VAR) -> None:
    print(test_var)

if __name__ == "__main__":
    # External argument
    # python utils/parse_external_arg.py var123
    new_var = extract_parameters()
    print_something(new_var)

    print("===")

    # Internal argument
    tmp_var = "123"
    print_something(tmp_var)

    print("===")

    # No input -> Use default argument
    print_something()
