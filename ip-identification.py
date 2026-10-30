ip = input("Enter IP: ").split(".")

if len(ip) != 4 or any(not x.isdigit() or int(x) > 255 for x in ip):
    print("Invalid IP")
else:
    n = int(ip[0])

    if n == 0 or n == 127:
        print("Reserved IP")
    elif n < 128:
        print("Class A, Mask: 255.0.0.0")
    elif n < 192:
        print("Class B, Mask: 255.255.0.0")
    elif n < 224:
        print("Class C, Mask: 255.255.255.0")
    elif n < 240:
        print("Class D - Multicast")
    else:
        print("Class E - Reserved")