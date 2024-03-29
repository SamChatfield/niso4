import random

from individual import Individual
from initialisation import growth


def branch_replacement(ind, max_depth, mutation_rate=1.0, growth_p_early_terminal=0.1):
    if random.random() > mutation_rate:
        return None
    # Choose the index of the subtree to replace
    repl_idx = random.randrange(len(ind.expression))
    new_expr = growth(1, max_depth, growth_p_early_terminal)[0].expression
    assert new_expr is not None

    new_ind = Individual(ind.expression.replace_subtree(repl_idx, new_expr))
    assert new_ind.expression is not None

    return new_ind


MUTATION_METHODS = {
    'none': lambda i: i,
    'branch_replacement': branch_replacement
}
