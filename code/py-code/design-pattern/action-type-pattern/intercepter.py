#!/usr/bin/python
# coding=utf-8

"""
解释器模式

1. 解决 为领域专家和高级用户提供一种简单语言来解决他们的问题时，可以使用解释器模式

2. 解释器模式仅与内部DSL相关。因此，我们的目标是使用宿主语言提供的特性构建一种简单
    但有用的语言，在这里，宿主语言是Python。注意，解释器根本不处理语言解析，它假设我们已
    经有某种便利形式的解析好的数据，可以是抽象语法树（abstract syntax tree，AST）或任何其他
    好用的数据结构

"""