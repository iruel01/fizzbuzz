#!/usr/bin/ruby
start = ARGV[0].to_i
tail = ARGV[1].to_i

start.upto(tail) do |i|
    mod5 = i % 5 == 0
    mod3 = i % 3 == 0

    puts case
        when (mod3 and mod5) then 'fizzbuzz'
        when mod5 then 'fizz'
        when mod3 then 'buzz'
    end
end
