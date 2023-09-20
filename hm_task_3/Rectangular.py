class Rectangular:
    def __init__(self, a_len, b_len):
        self.a_len = a_len
        self.b_len = b_len

    def sq_rect(self):
        return self.a_len * self.b_len

    def per_rect(self):
        return (self.a_len + self.b_len) * 2


rec1 = Rectangular(2, 3)
print(rec1.sq_rect(), rec1.per_rect())