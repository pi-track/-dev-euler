#!/usr/bin/env ruby

numbers = (1..999).to_a
total = 0
numbers.each do |number|
  ((number%3==0)|(number%5==0))? (total+=number):total
end
puts(total)
