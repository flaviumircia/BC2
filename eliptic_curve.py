# Elliptic curve parameters (y^2 = x^3 - ax + b)
a = 3
b = 139
p = 1217  # Field size (prime number)


def point_addition_modified(p, q, a, b, p_mod):
    if p == "O":
        return q
    if q == "O":
        return p

    x1, y1 = p
    x2, y2 = q

    if p != q:
        s = ((y2 - y1) * pow(x2 - x1, -1, p_mod)) % p_mod
    else:
        s = ((3 * pow(x1, 2) - a) * pow(2 * y1, -1, p_mod)) % p_mod

    x3 = (pow(s, 2) - x1 - x2) % p_mod
    y3 = (s * (x1 - x3) - y1) % p_mod

    return (x3, y3)



def find_scalar(G, H, a, b, p):
    current_point = G
    scalar = 1

    while current_point != H:
        scalar += 1
        current_point = point_addition_modified(current_point, G, a, b, p)

    return scalar


def is_point_on_curve(G, a, b, p):
    x, y = G
    if G == "O":
        return True  # The point at infinity is on the curve

    left_side = (y ** 2) % p
    right_side = ((x ** 3) - a * x + b) % p

    return left_side == right_side

def count_points(a, b, p):
    count = 1  # Initialize with the point at infinity

    for x in range(p):
        for y in range(p):
            if (y**2) % p == (x**3 - a * x + b) % p:
                count += 1

    return count

values = [(940, 253), (3, 816), (192, 847)]
for value in values:
    print(is_point_on_curve(value, a, b, p))

print(find_scalar((192,847),(160,665),a,b,p))

print(count_points(a,b,p))