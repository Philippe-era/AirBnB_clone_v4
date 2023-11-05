#!/usr/bin/python3
"""The HBNB CONSOLE DEFINED AND IMPLEMENETED"""
import cmd
from shlex import split
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
class HBNBCommand(cmd.Cmd):
    """How the HBNB INTEPRETER MUST WORK ACTUALLY."""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }
    def emptyline(self):
        """ALL THE EMPTY SPACES WILL BE IGNORED IN THIS CONTEXT"""
        pass
    def do_quit(self, line):
        """EXITS THE PROGRAM"""
        return True
    def do_EOF(self, line):
        """EOF EXITED IN THE SHOW WE CHECKING"""
        print("")
        return True
    def do_create(self, line):
        """Usage: WE WILL USE THE DO CREATE FUNCTION
        """
        try:
            if not line:
                raise SyntaxError()
            list_created = line.split(" ")
            kwargs = {}
            for initial in range(1, len(list_created)):
                key, value = tuple(list_created[initial].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value
            if kwargs == {}:
                obj_created = eval(list_created[0])()
            else:
                obj_created = eval(list_created[0])(**kwargs)
                storage.new(obj_created)
            print(obj_created.id)
            obj_created.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
    def do_show(self, line):
        """Displays in instances
        Exceptions:
            SyntaxError: when info is invalid
            NameError:no name present
            IndexError: no identity number present
            KeyError: yeah no valid information present
        """
        try:
            if not line:
                raise SyntaxError()
            list_created = line.split(" ")
            if list_created[0] not in self.__classes:
                raise NameError()
            if len(list_created) < 2:
                raise IndexError()
            objects = storage.all()
            key = list_created[0] + '.' + list_created[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
    def do_destroy(self, line):
        """Deletes everything unneccesary
        Exceptions:
            SyntaxError: no argument presetn
            NameError: no object present 
            IndexError: no id given in the context
            KeyError: id is invalid 
        """
        try:
            if not line:
                raise SyntaxError()
            list_created = line.split(" ")
            if list_created[0] not in self.__classes:
                raise NameError()
            if len(list_created) < 2:
                raise IndexError()
            objects = storage.all()
            key = list_created[0] + '.' + list_created[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
    def do_all(self, line):
        """Usage: we will use the do all class
"""
        if not line:
            o = storage.all()
            print([o[k].__str__() for k in o])
            return
        try:
            args = line.split(" ")
            if args[0] not in self.__classes:
                raise NameError()
            o = storage.all(eval(args[0]))
            print([o[k].__str__() for k in o])
        except NameError:
            print("** class doesn't exist **")
    def do_update(self, line):
        """updates as information is present
        Exceptions:
            SyntaxError: no argument present
            NameError: object without a name
            IndexError: no id index
            KeyError: no valid key
            AttributeError: attribute absent
            ValueError: no value
        """
        try:
            if not line:
                raise SyntaxError()
            list_created = split(line, " ")
            if list_created[0] not in self.__classes:
                raise NameError()
            if len(list_created) < 2:
                raise IndexError()
            objects = storage.all()
            key = list_created[0] + '.' + list_created[1]
            if key not in objects:
                raise KeyError()
            if len(list_created) < 3:
                raise AttributeError()
            if len(list_created) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[list_created[2]] = eval(list_created[3])
            except Exception:
                v.__dict__[list_created[2]] = list_created[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")
    def count(self, line):
        """count how times classes appeared
        """
        counter_num = 0
        try:
            list_created = split(line, " ")
            if list_created[0] not in self.__classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == list_created[0]:
                    counter_num += 1
            print(counter_num)
        except NameError:
            print("** class doesn't exist **")
    def strip_clean(self, args):
        """string will be returned to its original place
        Args:
            args: inputs number of valid arguements
        Return:
            returns string of argumetns
        """
        list_store = []
        list_store.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_string = args[1][args[1].find('(')+1:args[1].find(')')]
            list_store.append(((new_string.split(", "))[0]).strip('"'))
            list_store.append(my_dict)
            return list_store
        new_string = args[1][args[1].find('(')+1:args[1].find(')')]
        list_store.append(" ".join(new_string.split(", ")))
        return " ".join(i for i in list_store)
    def default(self, line):
        """return valid information required
        """
        list_created = line.split('.')
        if len(list_created) >= 2:
            if list_created[1] == "all()":
                self.do_all(list_created[0])
            elif list_created[1] == "count()":
                self.count(list_created[0])
            elif list_created[1][:4] == "show":
                self.do_show(self.strip_clean(list_created))
            elif list_created[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(list_created))
            elif list_created[1][:6] == "update":
                args = self.strip_clean(list_created)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
