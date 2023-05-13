
def number = 0;
new File("Ball.java").eachLine { line ->
    number++;
    println "$number: $line"
}
