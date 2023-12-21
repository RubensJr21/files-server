#!/usr/bin/env python
from scripts.Menu import Menu

# https://www.youtube.com/watch?v=Jp5inslWuKg&ab_channel=T%C3%A9oMeWhy

import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

def main():
    menu = Menu()
    menu.execute()
    return 0

if __name__ == '__main__':
    main()

# https://www.shellscriptx.com/p/echo.html
# https://desenvolvimentoaberto.org/2014/02/03/executar-comandos-shell-em-python-linux/