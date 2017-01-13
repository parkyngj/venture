##############
# 6. Classes #
##############

# use the "class" keyword to contruct a class

class Human:
        #  a class attribute, shared by all instances of the class
        species = "H. sapiens"

        # basic initializer. this is called when a class is instantiated.
        # note that the double leading and trailing underscores denote objects or attributes that are used by python but that live in user-controlled namespaces.
        # methods (or objects/attributes) like: __init__, __str__, __repr__, etc. are called "magic methods" or "dunder methods"
        # shouldn't invent such names on your own
        def __init__(self, name):
            # assign the argument to the instance's name attribute
            self.name = name

            # initialize property
            self.age = 0

        # an instance method. all methods take "self" as the first argument
        def say(self, msg):
            print ("{name}: {message}".format(name = self.name, message = msg))

        def sing(self):
            return "I'm just a poor boy, nobody loves me~"

        # a class method is shared among all instances
        # they are called with the calling class as the first argument
        @classmethod
        def get_species(class):
            return class.species

        # a static method is called without a class or instance reference
        @staticmethod
        def grunt():
            return "*grunt*"

        # a property is just like a getter. It turns the method age() into a read-only attribute of the same name
        @property
        def age(self):
            return self._age

        # this allows the property to be set
        @age.setter
        def age(self, age):
            self._age = age

        # this allows the property to be deleted
        @age.deleter
        def age(self):
            del self._age

# when a python interpreter reads a source file it executes all its code
# this __name__ check makes sure this code block is only executed when this module is the main program

if __name__ == '__main__':
    s = Human(name='Sally')
    s.say('hi')                 # "Sally: hi"
    t = Human('Tim')
    t.say('hello')              # "Tim: hello"

    # call our class method
    s.say(s.get_species())      # "Sally: H. sapiens"
    # change the shared attribute
    Human.species = "H. neanderthalensis"
    s.say(s.get_species())          # => "Sally: H. neanderthalensis"
    t.say(t.get_species())          # => "Tim: H. neanderthalensis"

    # call the static method
    print(Human.grunt())            # => "*grunt*"
    print(s.grunt())                # => "*grunt*"

    # update the property for this instance
    s.age = 23
    # get the property
    s.say(s.age)                    # => 23
    t.say(t.age)                    # => 0
    # delete the property
    del s.age
    # s.age                         # => this would raise an AttributeError

####################################################
## 6.1 Multiple Inheritance
####################################################

# Another class definition
class Bat:

    species = 'Baty'

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # This class also has a say method
    def say(self, msg):
        msg = '... ... ...'
        return msg

    # And its own method as well
    def sonar(self):
        return '))) ... ((('

if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.fly)

# To take advantage of modularization by file you could place the classes above in their own files,
# say, human.py and bat.py

# to import functions from other files use the following format
# from "filename-without-extension" import "function-or-class"

# superhero.py
from human import Human
from bat import Bat

# Batman inherits from both Human and Bat
class Batman(Human, Bat):

    # Batman has its own value for the species class attribute
    species = 'Superhero'

    def __init__(self, *args, **kwargs):
        # Typically to inherit attributes you have to call super:
        #super(Batman, self).__init__(*args, **kwargs)
        # However we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instead we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass arguments,
        # with each parent "peeling a layer of the onion".
        Human.__init__(self, 'anonymous', *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # override the value for the name attribute
        self.name = 'Sad Affleck'

    def sing(self):
        return 'nan nan nan nan nan batman!'


if __name__ == '__main__':
    sup = Batman()

    # Instance type checks
    if isinstance(sup, Human):
        print('I am human')
    if isinstance(sup, Bat):
        print('I am bat')
    if type(sup) is Batman:
        print('I am Batman')

    # Get the Method Resolution search Order used by both getattr() and super().
    # This attribute is dynamic and can be updated
    print(Batman.__mro__)       # => (<class '__main__.Batman'>, <class 'human.Human'>, <class 'bat.Bat'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
    print(sup.get_species())    # => Superhero

    # Calls overloaded method
    print(sup.sing())           # => nan nan nan nan nan batman!

    # Calls method from Human, because inheritance order matters
    sup.say('I agree')          # => Sad Affleck: I agree

    # Call method that exists only in 2nd ancestor
    print(sup.sonar())          # => ))) ... (((

    # Inherited class attribute
    sup.age = 100
    print(sup.age)

    # Inherited attribute from 2nd ancestor whose default value was overridden.
    print('Can I fly? ' + str(sup.fly))
