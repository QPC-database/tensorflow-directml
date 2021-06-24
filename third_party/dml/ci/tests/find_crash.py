#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""Finds crashes in the log files produced by the tests."""

import os

def find_crashes(log_content):
  lines = log_content.splitlines()
  test_count = {}

  for line in lines:
    if line.startswith('[ RUN      ] '):
      test_name = line[13:]
      if test_name not in test_count:
        test_count[test_name] = 1
      else:
        test_count[test_name] += 1
    elif (line.startswith('[  FAILED  ] ')
          or line.startswith('[  SKIPPED ] ')
          or line.startswith('[       OK ] ')):
      test_count[test_name] -= 1

      if test_count[test_name] == 0:
        del test_count[test_name]

  if test_count:
    print('The following tests crashed or hanged:')
    for test_name in test_count.keys():
      print(test_name.replace('\n', ''))
  else:
    print('All tests completed without crashing or hanging')
