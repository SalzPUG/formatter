#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def formatter(formatString, *args, **kwargs):

    formatString = formatString.replace("{{", "-----INTERNAL(-----")
    formatString = formatString.replace("}}", "-----INTERNAL)-----")

    i = 0
    while True:
      match = re.search("\{([^}]*)\}", formatString)
      if match == None:
        break
      contentX = match.group(1)

      content = contentX.replace(":d", "")

      replacement = ""
      if content == "":
        replacement = args[i]
        i = i + 1
      elif re.match("\d+", content):
        replacement = args[int(content)]
      elif re.match("\w+", content):
	replacement = kwargs[content]

      if content != contentX and not isinstance(replacement, int):
        raise ValueError

      formatString = formatString[:match.start(0)] + str(replacement) + formatString[match.end(0):]

    formatString = formatString.replace("-----INTERNAL(-----", "{")
    formatString = formatString.replace("-----INTERNAL)-----", "}")

    return formatString

if __name__ == "__main__":
    import nose
    nose.main()
