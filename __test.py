#!/usr/bin/env python
# -*-   encoding : utf8   -*-

import state
import state_machine

class A_state(state.State):

    def __init__(self):
        self._set_func_outside()

    def a_only_func(self):
        print('a only function')

    def next(self):
        return B_state()

class B_state(state.State):

    def __init__(self):
        self._set_func_outside()

    def b_only_func(self):
        print('b only function')

    def next(self):
        return C_state()

class C_state(state.State):

    def __init__(self):
        self._set_func_outside()

    def c_only_func(self):
        print('c only function')

    def next(self):
        return self

if __name__ == '__main__':
    kkk = state_machine.StateMachine(A_state())
    kkk.a_only_func()
    kkk.next()
    kkk.b_only_func()
    kkk.next()
    kkk.c_only_func()
    kkk.next()
    kkk.c_only_func()
