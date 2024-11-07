class SuperStr(str):
    def is_repeatance(self, s):
        if not s:
            return False
        repeated = len(self) % len(s) == 0
        if repeated:
            return self == s * (len(self) // len(s))
        return False

    def is_palindrom(self):
        cleaned_str = self.lower()
        return cleaned_str == cleaned_str[::-1]


st1 = SuperStr("abcabcabc")
print(st1.is_repeatance("abc"))
print(st1.is_repeatance("ab"))

st2 = SuperStr("Аргентина манит негра")
print(st2.is_palindrom())

st3 = SuperStr("")
print(st3.is_repeatance("a"))
print(st3.is_palindrom())