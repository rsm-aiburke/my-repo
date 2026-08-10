# Markdown File

```Python
def grad_desc(x0, learning_rate=0.1, max_iter=100, tol=0.01):
    distance = inf
    iterations = 0
    x = x0
    for num in range(max_iter):
        iterations += 1
        next_x = next_guess(x, learning_rate)
        distance = abs(next_x - x)
        if distance < tol:
            print(f"this occurred after {iterations} iterations, converges")
            return x
        x = next_x
    print(f"this occured after {iterations} iterations, reached max iterations")
    return x

def matpow(X, n):
    if X.shape[0] != X.shape[1]:
        raise ValueError()
    X2 = X.copy()
    for power in range(n - 1):
        X2 = matmult(X2, X.copy())
    return X2


def eigenvector_centrality(X, max_iter=20, tol=0.001):
    scores = []
    for i in range(X.shape[0]):
        scores.append(1)
    n = X.shape[0]
    for its in range(max_iter):
        old_scores = scores.copy()
        new_scores = []
        for r in range(n):
            n_score = sum(X[r, c] * scores[c] for c in range(n))
            new_scores.append(n_score)
        scores = new_scores
        total = sum(new_scores)
        scores = [score / total for score in new_scores]
        differences = [abs(scores[i] - old_scores[i]) for i in range(n)]
        if max(differences) < tol:
            return scores
    return scores

def col_vector_norm(x):
    total = 0
    for i in range(x.shape[0]):
        total += x[i] ** 2
    return total**0.5
def find_eigenvector(A, max_iter, tol):
    vec = np.ones([A.shape[0], 1])
    for _ in range(max_iter):
        new_vec = matmult(A, vec)
        norm = col_vector_norm(new_vec)
        new_vec = new_vec / norm
        if np.all((abs(vec - new_vec)) < tol):
            return new_vec
        else:
            vec = new_vec
    return vec
def summarize_customers(transactions, today):
    dct = {}
    for c_id in set([transactions[i]["customer_id"] for i in range(len(transactions))]):
        dct[c_id] = {}
    for c_id in set([transactions[i]["customer_id"] for i in range(len(transactions))]):# recency value
        dct[c_id]["recency"] = recency(transactions, c_id, today)
    for c_id in set([transactions[i]["customer_id"] for i in range(len(transactions))]):
        count = 0
        for i in range(len(transactions)):
            if transactions[i]["customer_id"] == c_id:
                count += 1
        dct[c_id]["frequency"] = count
    for c_id in set([transactions[i]["customer_id"] for i in range(len(transactions))]):
        dct[c_id]["monetary"] = total_spent(transactions, c_id)
    return dct
def xtile(values, n=5, rev=False):
    lst = []
    count = len(values)
    for i in range(count):
        rank = 0
        for j in range(count):
            if values[j] < values[i]:
                rank += 1
        b = int(rank * n / count) + 1
        if b > n:
            b = n
        if rev == True:
            b = n + 1 - b
        lst.append(b)
    return lst
def rfm_scores(summary):
    customer_ids = sorted(summary)
    recencies = []
    for customer in customer_ids:
        recencies.append(summary[customer]["recency"])
    frequencies = []
    for customer in customer_ids:
        frequencies.append(summary[customer]["frequency"])
    monetaries = []
    for customer in customer_ids:
        monetaries.append(summary[customer]["monetary"])
    r_bins = xtile(recencies, 5)
    f_bins = xtile(frequencies, 5, rev=True)
    m_bins = xtile(monetaries, 5, rev=True)
    scores = {}
    for i in range(len(customer_ids)):
        scores.update({customer_ids[i]: str(r_bins[i]) + str(f_bins[i]) + str(m_bins[i])})
    return scores
def average_clv_by_segment(summary, churn_by_segment, discount_rate=0.1, years=5):
    scores = rfm_scores(summary)
    segment_clv = {}
    for customer, values in summary.items():
        score = scores[customer]
        seg = segment(score)
        rate = churn_by_segment[seg]
        annual = values["monetary"]
        customer_clv = clv(annual, rate, discount_rate, years)
        if seg not in segment_clv:
            segment_clv[seg] = []
            segment_clv[seg].append(customer_clv)
    for seg in segment_clv:
        segment_clv[seg] = sum(segment_clv[seg]) / len(segment_clv[seg])
    return segment_clv
def update_centroids(points, labels, centroids):
    new_centroids = []
    for c in range(len(centroids)):
        members = []
        for i in range(len(points)):
            if labels[i] == c:
                members.append(points[i])
        if len(members) > 0:
            new_centroids.append(mean_point(members))
            new_centroids.append(list(centroids[c]))
        else:
    return new_centroids
def has_converged(old_centroids, new_centroids, tol=1e-6):
    for i in range(len(old_centroids)):
        if euclidean(old_centroids[i], new_centroids[i]) > tol:
            return False
    return True
def kmeans(points, initial_centroids, max_iter=100, tol=1e-6):
    centroids = []
    for c in initial_centroids:
        centroids.append(c)
    labels = assign_clusters(points, initial_centroids)
    for it in range(max_iter):
        new_centroids = update_centroids(points, labels, centroids)
        labels = assign_clusters(points, new_centroids)
        finished = has_converged(centroids, new_centroids, tol)
        centroids = new_centroids
        if finished:
            break
    return (centroids, labels)
def kmeans_best(points, starts, max_iter=100, tol=1e-6):
    best_score = None
    best_centroids = None
    best_labels = None
    for i in range(len(starts)):
        centroids, labels = kmeans(points, starts[i], max_iter, tol)
        score = within_ss(points, labels, centroids)
        if (best_score is None) or (score < best_score):
            best_centroids = centroids
            best_labels = labels
            best_score = score
    return (best_centroids, best_labels, best_score)
def elbow_scores(points, starts_by_k, max_iter=100, tol=1e-6):
    scores = {}
    for k in starts_by_k:
        score = kmeans_best(points, starts_by_k[k], max_iter, tol)
        scores[k] = score[2]
    return scores

scores_in5 = []  # Replace with your code
for score_a in range(6):
    for score_b in range(6):
        if score_a >= score_b:
            scores_in5.append({"score_a": score_a, "score_b": score_b})
def binom_pmf(k, n, p):
    return math.comb(n, k) * (p**k) * ((1 - p) ** (n - k))
    pass

# Replace with your code: add "p_score" to each dict in scores_in5
for i in range(len(scores_in5)):
    scores_in5[i]["p_score"] = binom_pmf(scores_in5[i]["score_a"], 5, P) * binom_pmf(
        scores_in5[i]["score_b"], 5, P
    )
def prob_win_a(rnd, curr_a, curr_b, turn):
    if rnd > 5:
        if turn == "A":
            return sudden_prob_a_win(curr_a > curr_b)
        else:
            if curr_a > curr_b:
                return 1.0
            elif curr_a < curr_b:
                return 0.0
            else:
                return 0.5
    else:
        if turn == "A":
            kicks_a = rnd
            kicks_b = rnd - 1
        else:
            kicks_a = rnd
            kicks_b = rnd
        remaining_a = 5 - kicks_a
        remaining_b = 5 - kicks_b
        prob = 0
        for add_a in range(remaining_a + 1):
            for add_b in range(remaining_b + 1):
                future_prob = binom_pmf(add_a, remaining_a, P) * binom_pmf(
                    add_b, remaining_b, P
                )
                final_a = curr_a + add_a
                final_b = curr_b + add_b
                if final_a > final_b:
                    prob += future_prob
                elif final_a == final_b:
                    prob += future_prob * 0.5
    return prob
def simulate_from(rnd, curr_a, curr_b, turn, rng):
    num_kicks = kicks_left(rnd, turn)
    score_a = curr_a
    score_b = curr_b
    for i in range(num_kicks[0]):
        if rng.random() < P:
            score_a += 1
    for i in range(num_kicks[1]):
        if rng.random() < P:
            score_b += 1
    if score_a == score_b:
        if sudden_death_winner(rng) == "A":
            return True
        else:
            return False
    elif score_a > score_b:
        return True
    elif score_b > score_a:
        return False
```
