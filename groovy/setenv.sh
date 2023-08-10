#!/bin/bash

#
# Groovy warning due to incorrect JAVA_HOME:
#
# WARNING: An illegal reflective access operation has occurred
# WARNING: Illegal reflective access by org.codehaus.groovy.reflection.CachedClass (file:/usr/share/groovy/lib/groovy-2.4.21.jar) to method java.lang.Object.finalize()
# WARNING: Please consider reporting this to the maintainers of org.codehaus.groovy.reflection.CachedClass
# WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
# WARNING: All illegal access operations will be denied in a future release
#
# Solution: set JAVA_HOME to parent directory of $(which java)
#

java_path=$(which java)
java_home=${java_path%/bin/java}
echo Setting JAVA_HOME=$java_home
export JAVA_HOME=$java_home

