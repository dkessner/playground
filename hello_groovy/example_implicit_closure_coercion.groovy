#!/usr/bin/env groovy

// Groovy performs implicit closure coercion to single abstract method types

import java.awt.event.ActionListener

listeners = []

def addListener(ActionListener al) {listeners << al}

addListener {println "Hello, world!"}

listeners << ({println "Hello again!"} as ActionListener)

ActionListener a = {println "Hello #3!"}
listeners << a

listeners*.actionPerformed()

