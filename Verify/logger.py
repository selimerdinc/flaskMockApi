from colorama import Fore, Style

class Log:
    @staticmethod
    def test_pass(test_name):
        print(Fore.GREEN + f"\n{test_name} : PASSED" + Style.RESET_ALL)