#!/usr/bin/env python

from mnist import MNIST
import random

mndata = MNIST('mnist') # local dir with uncompressed MNIST files

#images, labels = mndata.load_training()
# or
images, labels = mndata.load_testing()

index = random.randrange(0, len(images))  # choose an index ;-)
print(mndata.display(images[index]))

print(len(images))
print(len(labels))

