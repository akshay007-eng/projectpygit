A Python Project based on a week's training in Python Programming.

#TOPIC - IMPLEMENTATION OF GOLDEN RATIO AND GOLDEN ANGLE USING FIBONACCI SERIES IN PYTHON

# 1. "The Fibonacci Sequence"
The sequence of Fibonacci numbers is 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, etc. .The next value in the list is found by adding together the preceding two values. For example, 13 = 8 + 5, 21 = 13 + 8, 34 = 21 + 13, etc. Mathematically, we can define the sequence with a recurrence relation:

F(n+1) = F(n) + F(n-1)
and two initial 'seed values', F(0) = 0 and F(1) = 1.

# 2. "The Golden Ratio"
The ratio of successive elements of the sequence, i.e. F(n+1) / F(n). It turns out that this ratio tends towards a fixed value, as the Fibonacci numbers get larger. Moreover, this particular value is very well-known to mathematicians through the ages. It is known as the golden ratio, and is given by
The Golden Ratio is found in a special type of rectangle. When a rectangle is placed next to a square, as shown, they make a second rectangle. The Golden Ratio occurs when the two rectangles are similar, which means that the ratio of their side lengths is that same, a/b = (a+b)/a. This ratio is the Golden Ratio.

#3. "Binet Formula"
There is actually a simple mathematical formula for computing the nth Fibonacci number, which does not require the calculation of the preceding numbers. It features the Golden Ratio:
F(n) = 1/root(5) ( phi^ n - ( 1 - phi )^n)
This is called Binet's formula.

#4. "The Golden Angle"
The Fibonacci sequence and the Golden Ratio turn up unexpectedly in many places across the natural world. For example, sunflowers, which have opposing spirals of seeds, use the Fibonacci sequence to efficiently distribute their seeds in the most compact space.
the ratio of neighbouring elements in the Fibonacci sequence approaches the famous Golden Ratio:
     phi = (1 + root(5))/2   
i.e., 34/21 = 1.6190..., 55/34 = 1.6176..., 89/55 = 1.6182..., etc.
If we split a circle up into two parts in the ratio 1:1.618..., then angle subtended by the smaller part is called the Golden Angle.
The smaller part of the circle is the fraction
 f = 1/ ( 1 + phi ) = 1/ (phi)^2 ~ = 0.381966...
The Golden Angle is f x 360 degrees.

#5. "Chosmospirals"
A beautiful image like the pattern in sunflower seeds may be generated with a simple algorithm, which draws a filled circles using a loop.
Here "a" is an angle, which we may choose. Rather wonderfully, if we choose a = f x 360 degrees, i.e. the Golden Angle, then the arrangement of circles turns out be very closely-packed: the circles are close together but do not overlap. This turns out to be an excellent arrangement for (e.g.) seeds in a sunflower head. 

#6. "Fibonacci Plot"
Approach of plotting Fibonacci Fractal
Each number in the series represent the length of the sides of a square. The square of side length 0 does not exist. So we start from square of side length 1. The next square is also of side length 1.
We first construct the two squares of dimension 1 side by side as shown in the image below.
Then taking the joint length of the two squares we construct a third square below the two squares of dimension 1. Now the square is of the dimension 2
Again taking the 2 squares of dimension 1, 2 respectively we construct the fourth square of dimension 3
Although we continued this process for a small number of iterations but this process continues till infinity.
After we complete drawing the squares we start with the innermost smallest square. Then we draw continuous quadrants within the squares with the side of each square as the radius.
