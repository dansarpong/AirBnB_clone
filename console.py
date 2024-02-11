#!/usr/bin/python3
""" Program that contains the entry point of the command interpreter """
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Class for the entry point of the command interpreter """

    prompt = '(hbnb) '
    dict_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ Function for EOF or Ctrl-D encountered """
        print("^D")
        return True

    def emptyline(self):
        """ Function for empty line or ENTER occurence """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.dict_classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.dict_classes[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """ Prints the string representation of an instance """
        args = shlex.split(line)
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dict_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            objs_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in objs_dict:
                print(str(objs_dict[key]))
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        args = shlex.split(line)
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dict_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            objs_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in objs_dict:
                del objs_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances """
        args = shlex.split(line)
        storage.reload()
        objs_dict = storage.all()
        if not line:
            print([str(obj) for obj in objs_dict.values()])
        elif args[0] in HBNBCommand.dict_classes:
            print([str(obj) for key, obj in objs_dict.items()
                   if args[0] in key])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance based on the class name and id """
        args = shlex.split(line)
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dict_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            storage.reload()
            objs_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in objs_dict:
                setattr(objs_dict[key], args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
