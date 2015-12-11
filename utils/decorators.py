#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""This module gather the customed decorators of astrobject"""

__all__ = ["_autogen_docstring_inheritance"]


#####################################
# == Stoolen from Matplotlib     == #
#####################################
from matplotlib import docstring
def _autogen_docstring_inheritance(base,source_inheritance="Unknown"):
    """Autogenerated wrappers will get their docstring from a base function
    with an addendum."""
    msg ="\n\n[ This function is inheriting %s ]"%source_inheritance
    addendum = docstring.Appender(msg, '\n\n')
    return lambda func: addendum(docstring.copy_dedent(base)(func))




def make_method(obj):
    """Decorator to make the function a method of *obj*.

    In the current context::
      @make_method(Axes)
      def toto(ax, ...):
          ...
    makes *toto* a method of `Axes`, so that one can directly use::
      ax.toto()
    COPYRIGHT: from Yannick Copin
    """

    def decorate(f):
        setattr(obj, f.__name__, f)
        return f

    return decorate
