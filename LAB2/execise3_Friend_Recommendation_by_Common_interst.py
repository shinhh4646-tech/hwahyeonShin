import numpy

interests = ["Music", "Sports", "Tech", "Fashion", "Travel", "Food"]

matrix = numpy.array([[10, 0, 8, 2, 5, 7], [9, 1, 7, 3, 6, 8],[2, 9, 1, 8, 3, 0] 
])


def similarity(user_a, user_b):
    dot_product = numpy.dot(user_a, user_b)
    norm_a = numpy.linalg.norm(user_a)
    norm_b = numpy.linalg.norm(user_b)
    
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)

def friends(target_id, matrix, k=1):
    similarities = []
    
    for i in range(len(matrix)):
        if i != target_id:
            sim = similarity(matrix[target_id], matrix[i])
            similarities.append((i, sim))
            
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:k]


def recommend(target_id, matrix, interests_list, k=1):
    similar_friends = friends(target_id, matrix, k)
    recommendations = []
    
    for item_idx in range(len(interests_list)):
        
        if matrix[target_id][item_idx] == 0:
            weighted_sum = 0
            sim_sum = 0
            
            for friend_id, sim in similar_friends:
                friend_score = matrix[friend_id][item_idx]
                weighted_sum += friend_score * sim
                sim_sum += sim
                
            if sim_sum > 0:
                predicted_score = round(weighted_sum / sim_sum, 2)
                recommendations.append((interests_list[item_idx], predicted_score))
                
    
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations
