#!/usr/bin/env python
# -*-   encoding : utf8   -*-

class StateMachine:
    def __init__(self, init_state):
        self.current_state = init_state
        self.__get_func_outside(self.current_state)

    def __get_func_outside(self, obj_state):
        if not hasattr(obj_state, '_Only_Func_list'):
            raise AttributeError("obj_state ({}) ".format(str(obj_state)) +\
                                 "error, without _Only_Func_list")
        if obj_state._Only_Func_list:
            for func in obj_state._Only_Func_list:
                obj_state_func = getattr(obj_state, func)
                setattr(self, func, obj_state_func)

    def __del_func_outside(self, obj_state):
        if not hasattr(obj_state, '_Only_Func_list'):
            raise AttributeError("obj_state ({}) ".format(str(obj_state)) +\
                                 "error, without _Only_Func_list")
        if obj_state._Only_Func_list:
            for func in obj_state._Only_Func_list:
                obj_state_func = getattr(obj_state, func)
                delattr(self, func)

    def next(self):
        self.__del_func_outside(self.current_state)
        self.current_state = self.current_state.next()
        self.__get_func_outside(self.current_state)
