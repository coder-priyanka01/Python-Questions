# If two modules have functions with the same name and you import them both in same file how can you avoid conflicts when calling those functions?

import module1 as m1
import module2 as m2

m1.func()
m2.func()