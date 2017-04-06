from cmd import Cmd
import sys

parameters = sys.argv[1:]

class MyPrompt(Cmd):

    def do_start(self):
        """Start"""
        print(parameters)

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit