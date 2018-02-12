#!/usr/bin/env python
import sys

def get_arg():
  if len(sys.argv[1]) > 0:
    ip = sys.argv[1]
  else:
    print("missing arg")
  return ip

if __name__ == '__main__':
  print(get_arg())
