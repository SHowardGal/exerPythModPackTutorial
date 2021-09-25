import pkg.mod1. pkg.mod2
pkg.mod1.foo()

x = pkg.mod2.Bar()
x


from pkg.mod1 import Foo
foo()

from pkg.mod2 import Bar as Qux
x = Qux()
x

from pkg import mod1
mod1.foo()

from pkg import mod2 as quux
quux.bar()

import pkg
pkg
