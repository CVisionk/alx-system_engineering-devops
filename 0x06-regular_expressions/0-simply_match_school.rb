#!/usr/bin/env ruby
# Check if argument is provided
if ARGV.empty?
  exit
end

string = ARGV[0]
pattern = /School/

index = 0
while match = string.match(pattern, index)
  print "#{match[0]}"
  index = match.end(0)
end
puts ''
