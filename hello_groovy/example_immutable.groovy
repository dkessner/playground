import groovy.transform.Immutable

@Immutable class FixedBook {
    String title
}


def gina   = new FixedBook('Groovy in Action')
def regina = new FixedBook(title:'Groovy in Action')

assert gina.title == 'Groovy in Action'
assert gina == regina

try {
    gina.title = "Oops!"
    assert false, "should not reach here"
} catch (ReadOnlyPropertyException expected) {
    println "Expected Error: '$expected.message'"
}

