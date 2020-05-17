#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import re
import sre_yield

def convert(f):
  for line in f:
    patterns = list(sre_yield.AllStrings( \
                      re.sub(r'([()*+?$\\.])', \
                      '\\\\\g<1>', \
                      line).strip()))
    if len(patterns) > 20:
      print('ERROR: Too many patterns are generated from the line:\n  %s' % line, file=sys.stderr)
      sys.exit(1)
    print('\n'.join(patterns))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('filename', \
                      nargs='?', \
                      type=argparse.FileType(), \
                      default=sys.stdin)
  args = parser.parse_args()
  with args.filename as f:
    convert(f)

