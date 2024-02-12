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
        storage.reload()
        objs_dict = storage.all()
        if not line:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            key = args[0] + "." + args[1]
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(objs_dict[key], args[2], args[3])
        storage.save()

    def do_count(self, line):
        """ Counts the number of instances of a class """
        args = shlex.split(line)
        storage.reload()
        objs_dict = storage.all()
        count = 0
        for key, obj in objs_dict.items():
            if args[0] in key:
                count += 1
        print(count)

    def default(self, line):
        """ handle new ways of inputing data """
        val_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        line = line.strip()
        values = line.split(".")
        if len(values) != 2:
            cmd.Cmd.default(self, line)
            return
        class_name = values[0]
        command = values[1].split("(")[0]
        arg = ""
        try:
            inputs = values[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    arg = arg + " " + shlex.split(inputs[num])[0]
                else:
                    arg = arg + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            arg = ""
        arg = class_name + arg
        if (command in val_dict.keys()):
            val_dict[command](arg.strip())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
