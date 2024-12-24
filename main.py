import argparse
from src.app.module import parse_logs


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        required=False,
        type=str,
        default="config",
    )
    args = parser.parse_args()
    config = {"REPORT_SIZE": 1000, "REPORT_DIR": "./reports", "LOG_DIR": "./log"}
    with open(args.config, "r") as f:
        for line in f:
            key, value = line.split(":", maxsplit=1)
            match key:
                case "REPORT_SIZE":
                    config["REPORT_SIZE"] = int(value.strip())
                case "REPORT_DIR":
                    config["REPORT_DIR"] = value.strip()[1:-1]
                case "LOG_DIR":
                    config["LOG_DIR"] = value.strip()[1:-1]
                case "APP_LOGS":
                    config["APP_LOGS"]
    return config


if __name__ == "__main__":
    config = get_config()
    parse_logs(config)
