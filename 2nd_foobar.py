
visited =[]
queue = []
output =[]
path = []

def find_cases(src:int):
    cases = []
    i = int(src/8)
    j = src%8
    if i-2>=0 and j-1>=0:
        cases.append(src-17)
    if i-2>=0 and j+1<8:
        cases.append(src-15)
    if i-1>=0 and j-2>=0:
        cases.append(src-10)
    if i-1>=0 and j+2<8:
        cases.append(src -6)
    if i+1<8 and j-2>=0:
        cases.append(src+6)
    if i+1<8 and j+2<8:
        cases.append(src + 10)
    if i+2<8 and j-1>=0:
        cases.append(src+15)
    if i+2<8 and j+1<8:
        cases.append(src+17)      
    return cases

def solution(src, dest):
    steps =0
    visited.append(src)
    queue.append(src)
    while True:        
        subd = []
        demo = []
        demo.append(queue[0])
        subd += find_cases(queue[0])
        if dest in subd:
            demo.append(dest)
            output.append(demo)
            break
        for i in subd:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                demo.append(i)
        queue.pop(0)
        output.append(demo)
    
    track = dest
    path.append(dest)
    while track!=src:
        for i in output:
            if track in i:
                track = i[0]
                path.append(track)
                steps+=1
    return steps

                
print(solution(19,36))    







"""
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle. 
 The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(0, 1)
Output:
    3

Input:
solution.solution(19, 36)
Output:
    1

-- Java cases --
Input:
Solution.solution(19, 36)
Output:
    1

Input:
Solution.solution(0, 1)
Output:
    3

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""
