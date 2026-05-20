def maximize_reach_exact(budget, costs, reaches):
    n = len(costs)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + reaches[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    max_reach = dp[n][budget]
    selected_users_list = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_users_list.append(i - 1)
            w -= costs[i - 1]

    selected_users_list.reverse()
    
    return max_reach, selected_users_list


def is_within_budget(selection, costs, budget):
    total_cost = sum(costs[i] for i in selection)
    return total_cost <= budget


def maximize_reach_greedy(budget, costs, reaches):
    n = len(costs)
    users_info = []

    for i in range(n):
        ratio = reaches[i] / costs[i] if costs[i] > 0 else float('inf')
        users_info.append({'id': i, 'cost': costs[i], 'reach': reaches[i], 'ratio': ratio})

    users_info.sort(key=lambda x: x['ratio'], reverse=True)

    reach = 0
    current_cost = 0
    selected_users = []

    for user in users_info:
        if current_cost + user['cost'] <= budget:
            current_cost += user['cost']
            reach += user['reach']
            selected_users.append(user['id'])

    return reach, selected_users