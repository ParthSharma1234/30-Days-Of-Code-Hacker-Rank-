#!/bin/python3

import math
import os
import random
import re
import sys




S = input().strip()
try:
    integer_value =int(S)
    print(integer_value)
except ValueError:
    print('Bad String')