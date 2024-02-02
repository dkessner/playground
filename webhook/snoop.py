#!/usr/bin/env python
#
# snoop.py
#

import inspect


from sapiopylib.rest.WebhookService import AbstractWebhookHandler, WebhookConfiguration, WebhookServerFactory
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult
from sapiopylib.rest.DataMgmtService import DataMgmtServer


def print_dir(what):
    print("dir(" + what.__name__ + "):", dir(what), sep='\n', end='\n\n')



def print_members(what):
    members = inspect.getmembers(what)
    print("members of ", what.__name__)
    for (key, value) in members:
        print(key, "\n", value, "\n")



#######

print("names in global scope")
print("dir():", dir(), sep='\n', end='\n\n')
#print("globals():", globals(), sep='\n', end='\n\n')

classes = [globals()[name] for name in dir() if inspect.isclass(globals()[name])]
print("classes in global scope:")
for c in classes:
    print("  ", c)
print()

for c in classes:
    #print_dir(c)
    #print_members(c)
    print("** class " + c.__name__)
    #print(c.__doc__)
    print(inspect.getdoc(c))
    print()
    print("** source code")
    print(inspect.getsource(c))
    print("*" * 40)


