import sympy

with open("24/input.txt") as f:
    data = f.readlines()

# each hailstone provides 3 equations with 7 unknows (6 common, 1 hailstone-specific)
# (3 for rock original position, 3 for rock velocity, 1 for time of collision)
# 3 hailstones => 9 equations with 9 unknowns

vx, vy, vz = sympy.symbols('vx,vy,vz')
px, py, pz = sympy.symbols('px,py,pz', positive=True, integer=True)
t0, t1, t2 = sympy.symbols('t0,t1,t2', positive=True, integer=True)
equations = []

X, Y, Z = 0, 1, 2
for line, t in zip(data[:3], [t0, t1, t2]):
    position, velocity = line.strip().split(" @ ")
    p = [int(i) for i in position.split(", ")]
    v = [int(i) for i in velocity.split(", ")]

    equations.append(sympy.Eq(p[X] + v[X] * t, px + vx * t))
    equations.append(sympy.Eq(p[Y] + v[Y] * t, py + vy * t))
    equations.append(sympy.Eq(p[Z] + v[Z] * t, pz + vz * t))

res = sympy.solve(equations, [px, py, pz, vx, vy, vz, t0, t1, t2])[0]
print(sum(res[:3]))