import threading
import subprocess
import re
import time

condition_load = threading.Event()


# Função da thread de "load"
def loading_thread():
    while not condition_load.is_set():
        for char in "|/-\\":
            if condition_load.is_set():
                break
            print("\rAguardando o Nextcloud concluir a instalação {}".format(char), end="", flush=True)
            time.sleep(0.2)


# Inicie a thread de "load"
load_thread = threading.Thread(target=loading_thread)


def wait_installation():
    load_thread.start()
    while True:
        try:
            statusOutCommand = subprocess.check_output(
                "docker-compose exec -u www-data nextcloud php occ status", shell=True
            ).decode("utf-8")
            if (re.search(" *- installed: (.*)", statusOutCommand).group(1).strip() == "true"):
                condition_load.set()
                print("\r                                               ", end="", flush=True)
                print("\rO Nextcloud foi instalado com sucesso! \u2705")
                return True
            else:
                time.sleep(1)
        except subprocess.CalledProcessError:
            time.sleep(3)

# https://www.compart.com/en/unicode/U+2705#:~:text=Unicode%20Character%20%E2%80%9C%E2%9C%85%E2%80%9D%20(U%2B2705)
# https://stackoverflow.com/questions/44060516/multiple-stdout-w-flush-going-on-in-python-threading