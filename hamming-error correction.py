h = list(map(int, input("Enter 7 bits: ")))

p1 = h[0] ^ h[2] ^ h[4] ^ h[6]
p2 = h[1] ^ h[2] ^ h[5] ^ h[6]
p3 = h[3] ^ h[4] ^ h[5] ^ h[6]

error = p1 + 2 * p2 + 4 * p3

if error == 0:
    print("No error")
else:
    print("Error at position:", error)
    h[error - 1] = 1 - h[error - 1]

print("Corrected code:", *h)