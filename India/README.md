# India

This one was pretty fun, mainly because the program doesn't actually solves the challenge. The way I tried to solve it, would take too much to compute. What the program does is simply take a length (starting from 1 until it reaches the given string length (10000)) and search for each posible string within the given string, each time it finds one, it gets stored in a list and then it can check if the found string was already found. Every time it finishes the given string for a given lenght, the list is cleared, because those found substrings no longer matter, new found substrings will be of different lenght, and keeping the old strings will only result in an (even more) slower computing.

Fortunately, it was not necessary to compute so much. When I first fired the program (the only print was the final one that would output all the possible found substrings) I realized it would take some time, left it for an hour running and still no output. Then I decided to make it output something, in line 14, to see what was happening. The I saw how the first 2 lenghts, were pretty quick, almost instantaneous. For lenght 3 it would already take around 10 seconds, then almost a minute for the next lenghts. However I noticed something, the increase between each lenght from lenght 4 and up, was almost 10000, exactly the lenght of the given string, it could be no coincidence. So (because I didn't want to run the program again), I started checking the exact difference between each lenght. At first it seemed almost random, and thought I was wrong to assume it could be solved looking at that alone, but when I checked the difference between 6 and 7, and then 7 and 8 and so on, I realized something, it was decreasing every time by 1, from 99994. I let it continue for more minutes to see if the pattern was still there and it was!

All I had to do was to suppose that would keep going until it reached 1 for a string of length 10000 (wich of course makes sense), so I calculated the summation for all intergers between 1 and 99994 with the next formula:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/a512ec7bb8c0c3c26914cc13b68e5a6ddefad944)

With n=99994, the result is 4999450015. Adding to that number the number of substrings found by the program until length 6 (307447), the result is 4999757462.

## Answer

4999757462