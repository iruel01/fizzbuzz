#!/usr/bin/env python2.7


def fizzbuzz(start, end):

    for i in range(start, end):

        mod5 = i % 5 == 0
        mod3 = i % 3 == 0

        if mod3 and mod5:
            print 'fizbuzz'
        elif mod5:
            print 'fizz'
        elif mod3:
            print 'buzz'


def main():
    fizzbuzz(1, 1000)

main()
