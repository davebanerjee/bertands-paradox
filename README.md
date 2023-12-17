# Bertrand's Paradox

According to Wikipedia,
> The Bertrand paradox is a problem within the classical interpretation of probability theory. Joseph Bertrand introduced it in his work Calcul des probabilités (1889) as an example to show that the principle of indifference may not produce definite, well-defined results for probabilities if it is applied uncritically when the domain of possibilities is infinite.
> 
> The Bertrand paradox is generally presented as follows: Consider an equilateral triangle inscribed in a circle. Suppose a chord of the circle is chosen at random. What is the probability that the chord is longer than a side of the triangle?
>
> Bertrand gave three arguments (each using the principle of indifference), all apparently valid yet yielding different results:
>
> The "random endpoints" method: Choose two random points on the circumference of the circle and draw the chord joining them. To calculate the probability in question imagine the triangle rotated so its vertex coincides with one of the chord endpoints. Observe that if the other chord endpoint lies on the arc between the endpoints of the triangle side opposite the first point, the chord is longer than a side of the triangle. The length of the arc is one third of the circumference of the circle, therefore the probability that a random chord is longer than a side of the inscribed triangle is 1/3.
>
> The "random radial point" method: Choose a radius of the circle, choose a point on the radius and construct the chord through this point and perpendicular to the radius. To calculate the probability in question imagine the triangle rotated so a side is perpendicular to the radius. The chord is longer than a side of the triangle if the chosen point is nearer the center of the circle than the point where the side of the triangle intersects the radius. The side of the triangle bisects the radius, therefore the probability a random chord is longer than a side of the inscribed triangle is 1/2.
>
> The "random midpoint" method: Choose a point anywhere within the circle and construct a chord with the chosen point as its midpoint. The chord is longer than a side of the inscribed triangle if the chosen point falls within a concentric circle of radius half the radius of the larger circle. The area of the smaller circle is one fourth the area of the larger circle, therefore the probability a random chord is longer than a side of the inscribed triangle is 1/4.

## Code

To better illustrate how each approach answers a distinct, separate problem, I wrote a Python script that generates chords according to the method outlined in each of the three approaches. By inspection, one can notice that the approaches differ slightly in their distributions of chords. For example, the density of chords near the center of the circle in Figure 6 is significantly lower than in Figure 4 and 5.

![](/assets/chord_generation_1.png)

![](/assets/chord_generation_2.png)

![](/assets/chord_generation_3.png)
