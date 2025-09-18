def dynamic_programming():    
    memo = dict()

    f(subproblem_id):
        if subproblem is base case:
            return result directly

        if subproblem in memo:
            return cached result

        memo[subproblem_id] = recurrence relation

        return memo[subproblem_id]

    return f(initial subproblem)