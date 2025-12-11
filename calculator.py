def add(a, b):
    return a + b

def test():
    assert add(2, 3) == 5
    print("✅ Calculator test passed!")

if __name__ == "__main__":
    test()
    print(f"2 + 3 = {add(2, 3)}")
