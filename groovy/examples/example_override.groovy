import groovy.transform.Immutable

// @Immutable overrides == operator (equals())

@Immutable
class Money {
    int amount
    String currency

    // implement + operator
    Money plus(Money other) {
        if (null == other) return this
        if (other.currency != currency) {
            throw new IllegalArgumentException(
            "cannot add $other.currency to $currency")
        }
        return new Money(amount + other.amount, currency)
    }
}


Money buck = new Money(1, 'USD')
assert buck
assert buck == new Money(1, 'USD')
assert buck + buck == new Money(2, 'USD')
