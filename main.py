import argparse
from pathlib import Path
from src.app.module import read_file, get_latest

def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        required=False,
        type=Path,
        default=Path.joinpath(Path.cwd(), "config.py"),
    )
    args = parser.parse_args()
    print(args.config)

if __name__ == '__main__':
    get_config()
    file = get_latest()
    print(file)
    read_file(file)