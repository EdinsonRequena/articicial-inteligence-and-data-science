"""
Main moudle
Alumno: @edinsonrequena
"""

from anom import palindrome_lam
from classic import palindrome_def
from cli import cli_def


def main():

    palindrome_lam(cli_def())
    palindrome_def(cli_def())


if __name__ == '__main__':

    main()
