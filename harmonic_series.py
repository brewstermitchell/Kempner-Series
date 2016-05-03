#!/usr/bin/env python3
# (c) Brewster Mitchell 2016
#  Increment Kempner Series (modified harmonic) to just under 80, which should be the point where the series ends.
#  Displays total count of terms dropped (every term with denominator 9) and count of terms not dropped.

integer_increment = 0
harmonic = 0
count_no_drop = 0
count_drop = 0


while harmonic < 80:
  integer_increment += 1
  str_integer = str(integer_increment)
  if '9' in str_integer :
    count_drop += 1
  else:
    count_no_drop += 1
    harmonic += 1 / integer_increment

print('Final sum: %s', str(harmonic))
print('Number of terms dropped: %s', str(count_drop))
print('Number of terms not dropped: %s', str(count_no_drop))
exit(0)