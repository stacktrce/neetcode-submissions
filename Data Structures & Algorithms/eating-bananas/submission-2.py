import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r  # r funktioniert auf jeden Fall, also unser sicherer Startwert

        while l <= r:
            k = (l + r) // 2  # Wir testen eine mittlere Geschwindigkeit k

            # Wie viele Stunden braucht Koko mit Geschwindigkeit k?
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                # Koko schafft es! k ist eine gültige Lösung.
                # Aber vielleicht geht es noch langsamer -> links weitersuchen
                res = k
                r = k - 1
            else:
                # Koko braucht zu lange -> sie muss schneller essen -> rechts weitersuchen
                l = k + 1

        return res