import getch


def wait_for_key(prompt='Press [Enter] to Continue:'):

    print(prompt, end="", flush=True)

    getch.getch()

    print()
