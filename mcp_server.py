import sys
import json
from client import ShorPeriodFinding

shor = ShorPeriodFinding()

def handle_call(name, arguments):
    if name == "find_period":
        a = arguments["a"]
        N = arguments["N"]
        phase = arguments["phase"]
        n_q = arguments.get("num_qubits", 8)
        r = shor.find_period(a, N, phase, n_q)
        return {"period": r}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
