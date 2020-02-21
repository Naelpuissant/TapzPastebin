import click
import requests
from utils.helpers import get_api_key, steezy_print

@click.command()
@click.argument('paste')
@click.option('--api_key', help='Set your api key')
def pastebin(paste, api_key):
    """ 
    PASTE: your file or your text 
    
    You can set your API KEY in a .api_key file
    """
    if not api_key:
        api_key = get_api_key()

    try:
        paste = open(paste, 'r').read()
    except FileNotFoundError:
        pass

    data = {
        "api_dev_key": api_key,
        "api_option": "paste",
        "api_paste_code": paste,
    }
    
    res = requests.post("https://pastebin.com/api/api_post.php", data=data)

    if len(res.text) == 8:
        steezy_print("[+] Success !")
        id = res.text.split("/")[-1]
        print(f"https://pastebin.com/raw/{id}")
    else:
        steezy_print(f"[x] {res.text} !", status="error")


if __name__ == '__main__':
    pastebin()