class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(rem):
            # 1. Basisfall: Restbetrag ist 0 -> 0 Münzen nötig
            if rem == 0:
                return 0
            
            # 2. Schon berechnet? Direkt aus dem Notizblock holen
            if rem in memo:
                return memo[rem]

            # 3. Lokales Minimum für DIESEN Restbetrag auf Unendlich setzen
            res = float('inf')

            for coin in coins:
                if rem - coin >= 0:
                    res = min(res, 1 + dfs(rem - coin))

            # 4. Erst NACH der Schleife speichern und zurückgeben!
            memo[rem] = res
            return res

        ans = dfs(amount)
        return ans if ans != float('inf') else -1