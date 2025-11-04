import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

p = sp.Symbol('p', real=True)

# Initialize G(i,j)
G = [[None for j in range(4)] for i in range(5)]
for j in range(3):
    G[4][j] = sp.Integer(1)
for i in range(4):
    G[i][3] = sp.Integer(0)
G[4][3] = sp.Integer(4)

# Compute G recursively
for i in reversed(range(4)):
    for j in reversed(range(3)):
        num = 4*p*G[i+1][j] + G[i][j+1]*((1-p)*G[i+1][j] - G[i][j+1])
        den = G[i+1][j] + 4*p - G[i][j+1]*(1+p)
        G[i][j] = sp.simplify(num / den)

# Transition probabilities
P_next_i1j = [[None for j in range(3)] for i in range(4)]
P_next_ij1 = [[None for j in range(3)] for i in range(4)]

for i in range(4):
    for j in range(3):
        Gij = G[i][j]
        G_ip1_j = G[i+1][j]
        G_i_jp1 = G[i][j+1]
        denom = G_ip1_j + 4*p - G_i_jp1*(1+p)
        W = sp.simplify(p*(4 - G_i_jp1) / denom)
        P_next_i1j[i][j] = sp.simplify(W**2)
        P_next_ij1[i][j] = sp.simplify((1 - W)*(1 + W - p + p*W))

# Probability of visiting (3,2)
H = [[None for j in range(4)] for i in range(5)]

for i in range(5):
    for j in range(4):
        if i == 3 and j == 2:
            H[i][j] = sp.Integer(1)
        elif i == 4 or j == 3:
            H[i][j] = sp.Integer(0)
        else:
            H[i][j] = sp.Symbol(f"H{i}{j}")  # placeholder

# Backward recursion
for i in reversed(range(4)):
    for j in reversed(range(3)):
        if not (i == 3 and j == 2):
            H[i][j] = sp.simplify(
                P_next_i1j[i][j]*H[i+1][j] + P_next_ij1[i][j]*H[i][j+1]
            )

# Substitute until H(0,0) is purely in terms of p
changed = True
while changed:
    changed = False
    for i in range(4):
        for j in range(3):
            expr = H[i][j]
            if any(isinstance(arg, sp.Symbol) and str(arg).startswith("H") for arg in expr.free_symbols):
                for ii in range(4):
                    for jj in range(3):
                        sym = sp.Symbol(f"H{ii}{jj}")
                        if sym in expr.free_symbols:
                            expr = expr.subs(sym, H[ii][jj])
                            changed = True
                H[i][j] = sp.simplify(expr)

H_0_0 = sp.simplify(H[0][0])
print("Probability of visiting (3,2) =", H_0_0)

# Convert to a numeric function for plotting
f = sp.lambdify(p, H_0_0, 'numpy')

# Evaluate for p in [0,1]
p_vals = np.linspace(0, 1, 200)
y_vals = [float(f(val)) for val in p_vals]

plt.figure(figsize=(7, 4))
plt.plot(p_vals, y_vals)
plt.xlabel('p')
plt.ylabel('Probability of visiting (3,2)')
plt.title('Probability of visiting (3,2) as a function of p')
plt.grid(True)
plt.show()


# Compute derivative of H(0,0) with respect to p and find stationary points
dH_dp = sp.diff(H_0_0, p)

print("Derivative of H =", dH_dp)

# Solve dH/dp = 0 for p in [0,1]
critical_points = sp.solve(sp.Eq(dH_dp, 0), p)

print("Critical points =", critical_points)

# Filter real solutions within [0,1]
critical_points = [sp.N(cp) for cp in critical_points if cp.is_real and 0 <= cp <= 1]

print("Critical points =", critical_points)

# Evaluate H_0_0 at those points to find the maximum
values = [(cp, float(H_0_0.subs(p, cp))) for cp in critical_points]

print("Values =", values)

