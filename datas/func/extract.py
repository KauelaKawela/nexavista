import re
from datas.func import helper_func

def extract_links(file_links):
    try:
        with open(file_links, "r", encoding="utf-8") as fl:
            return [
                match.group(1).strip()
                for line in fl
                if (match := re.search(r"(https?://[^\s\"')><]*[^\s\"')><.,;])", line))
            ]
    except FileNotFoundError as e:
        print(f"{clr.mn}║\n║\n╚════════════╝ '{file_links}' {clr.k}link dosyası bulunamadı!{clr.r}")
        helper_func.error_log_write(e)
        sys.exit()
