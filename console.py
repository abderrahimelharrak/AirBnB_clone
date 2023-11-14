#!/usr/bin/python3
"""Method of Command Interpreter"""
import cmd
import shlex
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def do_create(self, args):
        """Creating a new instance of BaseModel, save it and prints the id
           Usage: creating <class name>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new__creation = eval(args[0] + '()')
            models.storage.save()
            print(new__creation.id)

    def do_show(self, args):
        """Printing the string representation of a specific instance
           Usage: showing class name and id
        """
        strs = args.split()
        if len(strs) == 0:
            print("** class name missing **")
        elif strs[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(strs) == 1:
            print("** instance id missing **")
        else:
            obje = models.storage.all()
            key__value = strs[0] + '.' + strs[1]
            if key__value in obje:
                print(obje[key__value])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deleting an instance
           Usage: destroying class name and id
        """
        args = args.split()
        object_s = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key__find = args[0] + '.' + args[1]
            if key__find in object_s.keys():
                object_s.pop(key__find, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        """Printing a string representation of all instances
           Usage: all class names
        """
        args = args.split()
        object_s = models.storage.all()
        new__list = []

        if len(args) == 0:
            for obje in object_s.values():
                new__list.append(obje.__str__())
            print(new__list)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obje in object_s.values():
                if obje.__class__.__name__ == args[0]:
                    new__list.append(obje.__str__())
            print(new__list)

    def do_update(self, args):
        """updating an instance
           Usage updating class name id attribute name "attribute value"
        """
        object_s = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key__find = args[0] + '.' + args[1]
            obj = object_s.get(key__find, None)

            if not obje:
                print("** no instance found **")
                return

            setattr(obje, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        """Checking if stdin user typed class name and id."""
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Checkling class id"""
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """Finding the name class."""
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    x = args[0] + '.' + args[1]
                    return x
                else:
                    print("** class doesn't exist **")
                    return None

    def do_quit(self, args):
        """Quit Command To Exit The Program"""
        return True

    def do_EOF(self, args):
        """Handling end of file"""
        return True

    def emptyline(self):
        """No execute anything when user
           pressing enter an empty line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

