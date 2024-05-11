#!/usr/bin/env ruby
# A regular expression that is matching and outputs School

# Check if argument is provided
if ARGV.empty?
  exit
end
puts ARGV[0].scan(/\[(?:from|to|flags):\S+\]\/).join
