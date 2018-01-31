#!usr/bin/env ruby
x,y = 1,2
total = 0
while (x<4e6 && y<4e6)
  (x%2==0)? total+=x:nil
  (y%2==0)? total+=y:nil
  x,y = y,x+y
end

puts total
