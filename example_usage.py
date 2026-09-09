from client import ShorPeriodFinding

def main():
    print("=== Testing Shor's Period Finding Kernel ===")
    shor = ShorPeriodFinding()
    # N=15, a=7 -> 7^4 = 1 mod 15 -> r=4
    # phase = 64 for 8 qubits (64/256 = 1/4)
    r = shor.find_period(a=7, N=15, measured_phase=64, n_qubits=8)
    print(f"Extracted period r={r} for base 7 mod 15")
    assert r == 4
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
