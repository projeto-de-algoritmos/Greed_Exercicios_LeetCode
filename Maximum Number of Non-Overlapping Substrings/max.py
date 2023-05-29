class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # Primeiro, identificamos os intervalos válidos para cada caractere
        intervals = {}
        for i, char in enumerate(s):
            if char not in intervals:
                intervals[char] = [i, i]
            else:
                intervals[char][1] = i

        # Em seguida, expandimos os intervalos para atender às condições
        valid_intervals = []
        for interval in intervals.values():
            start, end = interval[0], interval[1]
            i = start
            while i <= end:
                if intervals[s[i]][0] < start:
                    start = intervals[s[i]][0]
                    i = start
                if intervals[s[i]][1] > end:
                    end = intervals[s[i]][1]
                i += 1
            valid_intervals.append([start, end])

        # Ordenamos os intervalos pelo fim em ordem crescente
        valid_intervals.sort(key=lambda x: x[1])

        # Construímos as substrings usando os intervalos válidos
        result = []
        prev_end = float('-inf')
        for interval in valid_intervals:
            start, end = interval[0], interval[1]
            if start > prev_end:
                result.append(s[start:end+1])
                prev_end = end

        return result