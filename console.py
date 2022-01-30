import cmd, sys
"""Defines a class """


class HBNBCommand(cmd.Cmd):
    """Command console class"""
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        """End of file and exits the console"""
        EOF(*parse(arg))

    def do_help(self, arg):
        """display help functions"""
        help(*parse(arg))

    def do_quit(self, arg):
        """quits the command interpreter"""
        self.close()
        quit()
        return True


    if __name__ == '__main__':
            HBNBCommand().cmdloop()
