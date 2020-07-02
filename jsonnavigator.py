
class JsonNavigatorAll(object):
    pass


class JsonNavigator(object):
    """
    Given a list(tuple) of elements to grab, go through the parsed json data structure and fetch appropriate parts

    the elements here are called the navigation path and the kind of navigation is determined by the type
    of the navigation element. Thus:
    a string - will assume we have a dictionary and will try to fetch the key of that dictionary that matches the string
    a number - will assume a list and try to fetch nth element of the list
    a slice - will assume a list and try to fetch a slice of the list
    a tuple - only 2-element tuples are allowed will assume a list of dicts, and try to fetch those,
        who have a key, value pair that matches tuple's contents
    ellipsis `...` will match all elements of a list, or dict (useful to just go one nesting level deeper)
    """
    # define constants
    ALL = JsonNavigatorAll()

    def __init__(self, grey_mass):
        self.grey_mass = grey_mass

    def navigate(self, *path):
        """
        Fetch elements that fulfill criteria expressed by path
        :param path: the navigation path
        :return: subset of the parsed json tree
        """
        subtree = self.grey_mass
        try:
            for arg in path:
                if isinstance(arg, (str, int, slice)):
                    subtree = subtree[arg]
                elif arg is ...:
                    raise NotImplementedError('temporary')
                # idea: morph the subtree into a special object, that is capable of parallel navigation in its elements
                else:
                    raise NotImplementedError
        except KeyError:
            return None
        except TypeError as e:
            if 'unhashable type' not in e.args[0]:
                raise
            else:
                return None

        return subtree
