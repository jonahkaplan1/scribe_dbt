import os
import src.dbt_logic as dbt_logic
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test",
        help="If you want to test",
    )

    args = parser.parse_args()

    if args.test:
        test = args.test
    else:
        test = True

    print("")
    print("Running scribe_dbt" + dbt_logic.get_version())
    print("")

    try:
        print('BINGO!')
    except KeyboardInterrupt:
        print("Interupted by user")


if __name__ == "__main__":
    main()
