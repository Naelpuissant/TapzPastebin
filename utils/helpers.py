RED = "\033[91m"
GREEN = "\033[92m"
END = "\033[0m"


def steezy_print(text: str, status="success"):
    if status not in ["success", "error"]: raise ValueError
    color = GREEN if status == "success" else RED
    print(color + text + END)


def get_api_key():
    with open('.api_key', 'r') as f:
        return f.read()