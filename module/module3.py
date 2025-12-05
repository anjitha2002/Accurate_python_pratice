from module import module1, module2, module2 as mod

module1.msg()
module2.add(2, 5)
module2.sub(2, 5)
module2.mul(2, 5)
module2.div(2, 5)

from module.module2 import sub
sub(2,5)


# when the module has a long name we can short it as by
mod.add(2,5)
mod.sub(2,5)


#if importing module that have attributes with same name
from module.module1 import add
from module.module2 import add as a
add(2,5)
a(2,5)

module1.square(3)


from module.module1 import square as squ
squ(3)






