# España

This was a pretty easy one, it can even by easily calculated by hand. One must just suppose the amount of pages needed will be N digits long, calculate the amount of effective space per page (characters in title - 1 for the / - 2 * N)
and divide the characters of the book by the characters per page, then see if that number is N digits long, if not, just repeat for N+1. It would have been more fun if the page number didn't incluide leading zeroes, or maybe with big enough numbers, calculating by hand would take several hours.

The only thing the program does, is guessing a number of pages (starting from 1) and checking if the math holds up, if not, add a page and repeat.

## Answer

112