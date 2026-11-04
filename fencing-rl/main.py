from env.fencing_env import FencingEnv, ADVANCE, LUNGE, PARRY, RETREAT, WAIT, ACTION_NAMES

# Fixed Actions Env Test
# env = FencingEnv()
# obs, info = env.reset(seed=0)
# env.render()

# for a_act, b_act in [(ADVANCE, ADVANCE), (ADVANCE, WAIT), (LUNGE, WAIT), (LUNGE, PARRY), (RETREAT, RETREAT)]:
#     obs, rewards, terminated, truncated, info = env.step(a_act, b_act)
#     print(f"A:{ACTION_NAMES[a_act]:8} B:{ACTION_NAMES[b_act]:8} rewards {[round(r, 2) for r in rewards]}")
#     env.render()


# Random Actions Test
import random

def play_bout(policy_a, policy_b, seed=0, verbose=False):
    env = FencingEnv()
    (obs_a, obs_b), _ = env.reset(seed=seed)
    done = False
    while not done:
        act_a, act_b = policy_a(obs_a), policy_b(obs_b)
        (obs_a, obs_b), rewards, terminated, truncated, _ = env.step(act_a, act_b)
        if verbose:
            print(f"{ACTION_NAMES[act_a]:8} vs {ACTION_NAMES[act_b]:8}", end=" | ")
            env.render()
        done = terminated or truncated
    return env.touches

random_policy = lambda obs: random.randrange(5)
print(play_bout(random_policy, random_policy, seed=1, verbose=True))

def aggressive(obs):
    dist, my_stam, opp_stam, opp_last = obs
    if dist <= 2 and my_stam > 0:
        return LUNGE
    return ADVANCE if dist > 2 else WAIT

def defensive(obs):
    dist, my_stam, opp_stam, opp_last = obs
    if dist == 2:
        return PARRY
    if dist < 2:
        return RETREAT
    return ADVANCE

def win_rate(policy_a, policy_b, n=1000):
    wins = [0, 0, 0]  # A, B, draw
    for s in range(n):
        ta, tb = play_bout(policy_a, policy_b, seed=s)
        wins[0 if ta > tb else 1 if tb > ta else 2] += 1
    return [w / n for w in wins]

print("aggressive vs random:", win_rate(aggressive, random_policy))
print("defensive vs random: ", win_rate(defensive, random_policy))
print("aggressive vs defensive:", win_rate(aggressive, defensive))