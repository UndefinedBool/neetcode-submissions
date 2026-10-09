class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s
    def decode(self, s: str) -> List[str]:
        r1 = []
        r2 = ""
        done = 1
        num = 0
        tens = 0
        counter = 0
        for i in s:
            if done == 1 and i != "#":
                num = num * 10 + int(i)
                tens += 1
                continue
            elif done == 1 and i == "#":
                done = 2
                if num == 0:
                    done = 1
                    s = ""
                    r1.append(r2)
                    tens = 0
                    counter = 0
                    r2 = ""
                    num = 0
                continue
            if done == 2:
                r2 += i
                counter += 1
                if counter == num:
                    done = 1
                    s = ""
                    r1.append(r2)
                    tens = 0
                    counter = 0
                    r2 = ""
                    num = 0
        return r1