# -*- coding: UTF-8 -*-
import re

str = "This is a cute dog"
ret = re.match('(.*) is (.*)', str, re.M|re.I)

print(ret.group())
print(ret.group(1))
print(ret.group(2))
