class ShorPeriodFinding:
    """
    Arithmetic and Continued Fractions kernel for Shor's Order Finding.
    Finds integer r such that a^r = 1 (mod N).
    Converts phase estimate s/2^n to convergent p/q to identify r.
    """
    def continued_fraction(self, numerator, denominator):
        cf = []
        n, d = numerator, denominator
        while d != 0:
            a = n // d
            cf.append(a)
            n, d = d, n - a * d
        return cf

    def convergents(self, cf):
        convs = []
        p_prev, p_curr = 0, 1
        q_prev, q_curr = 1, 0
        for a in cf:
            p_next = a * p_curr + p_prev
            q_next = a * q_curr + q_prev
            convs.append((p_next, q_next))
            p_prev, p_curr = p_curr, p_next
            q_prev, q_curr = q_curr, q_next
        return convs

    def find_period(self, a, N, measured_phase, n_qubits):
        denom = 1 << n_qubits
        cf = self.continued_fraction(measured_phase, denom)
        for p, q in self.convergents(cf):
            if q > 0 and pow(a, q, N) == 1:
                return q
        return None
