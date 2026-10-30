data = input("Enter 4-bit data: ")

d1 = int(data[0])
d2 = int(data[1])
d3 = int(data[2])
d4 = int(data[3])

p1 = d1 ^ d2 ^ d4
p2 = d1 ^ d3 ^ d4
p3 = d2 ^ d3 ^ d4

h1 = p1
h2 = p2
h3 = d1
h4 = p3
h5 = d2
h6 = d3
h7 = d4

print("Original Data:", data)
print("Parity Bits:", p1, p2, p3)

print("Hamming Code:")
print(h1, h2, h3, h4, h5, h6, h7)