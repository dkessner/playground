# Notes on Groovy + Processing

Make sure `CLASSPATH` includes the Processing libraries.
```
export CLASSPATH=".:$HOME/local/processing-4.0a3/core/library/*"
```

## Java version  

Ubuntu + Java 11 error:
```
Caught: java.lang.UnsupportedClassVersionError: processing/core/PApplet
has been compiled by a more recent version of the Java Runtime (class
file version 61.0), this version of the Java Runtime only recognizes
class file versions up to 55.0
```

Solution: 

1) Update to latest Java version (19)
```
sudo apt install openjdk-19-jdk
sudo update-alternatives --config java
sudo update-alternatives --config javac
```

2) Make sure `JAVA_HOME` is set correctly.
```
export JAVA_HOME=/usr
```


