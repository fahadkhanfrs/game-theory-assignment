strategies = ['C', 'D']
payoff_matrix = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1)
}

def is_pure_nash(profile, payoff_matrix):
    """Checking if a profile is a pure Nash equilibrium."""
    for i, player in enumerate([1, 2]):
        current_action = profile[i]
        other_action = profile[1 - i]
        for alt_action in strategies:
            if alt_action == current_action:
                continue
            alt_profile = list(profile)
            alt_profile[i] = alt_action
            alt_profile = tuple(alt_profile)
            # Comparing payoffs
            if payoff_matrix[alt_profile][i] > payoff_matrix[profile][i]:
                return False
    return True

pure_nash_equilibria = []
for s1 in strategies:
    for s2 in strategies:
        profile = (s1, s2)
        if is_pure_nash(profile, payoff_matrix):
            pure_nash_equilibria.append(profile)

print("Pure Nash Equilibria:", pure_nash_equilibria)
