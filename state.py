#!/usr/bin/env python
# -*-   encoding : utf8   -*-

class State:
    _Only_Func_list = []
    def next(self):
        raise NotImplementedError()
    def _set_func_outside(self, exclude_list=[]):
        self._Only_Func_list = []
        exc_list = exclude_list.copy() + \
                ['next', '_set_func_outside']
        for attr_str in dir(self):
            attr = getattr(self, attr_str)
            if attr_str[:2] != '__' and \
                    attr_str not in exc_list and \
                    hasattr(attr, '__call__'):
                    # 第一项表示 该 attribute 并非private，
                    # 第二项表示 该 attribute 并非保留命令
                    # 第三项表示 该 attribute 是function
                self._Only_Func_list.append(attr_str)
    def __init__(self):
        self._set_func_outside()

### example code ###
class __test_state(State):
    def __init__(self):
        self._set_func_outside()
    def test_only_func(self):
        print('test code')
