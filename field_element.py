class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            prime = prime - 1
            error = f"Num {num} not in field range 0 to {prime}"
            raise ValueError(error)
        self.num = num
        self.prime = prime

    
    def __repr__(self):
        return f"FieldElement_{self.prime}({self.num})"

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
