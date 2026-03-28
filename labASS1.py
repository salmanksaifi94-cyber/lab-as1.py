# Name='salman'
# Roll_n0=2501840005
# labAss=1



# AERT – Algorithmic Efficiency & Recursion Toolkit
# ============================================

# PART A: Stack ADT
# -----------------------------

class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# -----------------------------
# PART B: Factorial (Recursive)
# -----------------------------

def factorial(n):
    if n < 0:
        return "Invalid input (negative number)"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# -----------------------------
# Fibonacci (Naive + Call Counter)
# -----------------------------

naive_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# -----------------------------
# Fibonacci (Memoized + Call Counter)
# -----------------------------

memo_calls = 0

def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]


# -----------------------------
# PART C: Tower of Hanoi
# -----------------------------

def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        stack.push(move)
        return

    hanoi(n - 1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    stack.push(move)

    hanoi(n - 1, auxiliary, source, destination, stack)


# -----------------------------
# PART D: Recursive Binary Search
# -----------------------------

def binary_search(arr, key, low, high, stack):
    if low > high:
        return -1

    mid = (low + high) // 2
    stack.push(mid)  # store mid index in stack

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1, stack)
    else:
        return binary_search(arr, key, mid + 1, high, stack)


# -----------------------------
# MAIN FUNCTION (All Test Cases)
# -----------------------------

def main():

    print("===== PART A: Stack ADT =====")
    stack = StackADT()
    stack.push(10)
    stack.push(20)
    print("Top element:", stack.peek())
    print("Stack size:", stack.size())
    print("Popped:", stack.pop())
    print()

    print("===== PART B: Factorial =====")
    for n in [0, 1, 5, 10]:
        print(f"Factorial({n}) =", factorial(n))
    print()

    print("===== Fibonacci Comparison =====")
    for n in [5, 10, 20, 30]:
        global naive_calls, memo_calls

        naive_calls = 0
        memo_calls = 0

        print(f"\nFibonacci({n})")

        result_naive = fib_naive(n)
        print("Naive Result:", result_naive)
        print("Naive Calls:", naive_calls)

        result_memo = fib_memo(n, memo={})
        print("Memoized Result:", result_memo)
        print("Memoized Calls:", memo_calls)

    print()

    print("===== PART C: Tower of Hanoi (N=3) =====")
    hanoi_stack = StackADT()
    hanoi(3, "A", "B", "C", hanoi_stack)
    print("Total moves stored in stack:", hanoi_stack.size())
    print()

    print("===== PART D: Recursive Binary Search =====")
    arr = [1, 3, 5, 7, 9, 11, 13]

    for key in [7, 1, 13, 2]:
        bs_stack = StackADT()
        index = binary_search(arr, key, 0, len(arr) - 1, bs_stack)
        print(f"Search {key} → Index:", index)
        print("Mid indices visited:", bs_stack.stack)
        print()

    # Empty array test
    empty_arr = []
    bs_stack = StackADT()
    index = binary_search(empty_arr, 5, 0, len(empty_arr) - 1, bs_stack)
    print("Search in empty array → Index:", index)


if __name__ == "__main__":
    main()