#!/usr/bin/env python3
""" Program that contains the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Class for the entry point of the command interpreter """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """ Function for EOF or Ctrl-D encountered """
        print("^D")
        return True

    def emptyline(self):
        """Function for empty line or ENTER occurence"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
