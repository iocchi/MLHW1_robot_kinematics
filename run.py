import sys, time
sys.path.append("..")
import argparse
import gymnasium as gym

from envs.reacher_v6 import ReacherEnv
from envs.reacher3_v6 import Reacher3Env
from envs.marrtino_arm import MARRtinoArmEnv

def print_header(njoints, ndim):
    for i in range(njoints):
        print(f"j{i};", end="")
    for i in range(njoints):
        print(f"cos(j{i});", end="")
    for i in range(njoints):
        print(f"sin(j{i});", end="")
    if ndim==2:
        print("ft_x;ft_y;ft_qw;ft_qz")
    elif ndim==3:
        print("ft_x;ft_y;ft_z;ft_qw;ft_qx;ft_qy;ft_qz")


def print_obs(obs, njoints, ndim):
    # j_i; cosx(j_i); sin(j_i)
    r = ""
    for i in range(0,3*njoints):
        r = r + f"{obs[i]:6.3f}; "
    if ndim==2:
        # fingertip pose  ft_x;ft_y;ft_qw;ft_qz
        for i in range(-6,-2):
            r = r + f"{obs[i]:6.3f}; "
    elif ndim==3:
        # fingertip pose  ft_x;ft_y;ft_z;ft_qw;ft_qx;ft_qy;ft_qz
        for i in range(-10,-3):
            r = r + f"{obs[i]:6.3f}; "
    print(r[0:-2])

def dorun(args):

    render_mode="human" if args.render else None
        
    if args.env=='r2':
        env = ReacherEnv(render_mode=render_mode)
    elif args.env=='r3':
        env = Reacher3Env(render_mode=render_mode)
    elif args.env=='r5':
        env = MARRtinoArmEnv(render_mode=render_mode)
    else:
        print(f"Unknown environment {args.env}")
        sys.exit(1)

    #print(f"Observation: {env.observation_space}")
    #print(f"Action: {env.action_space}")

    if args.log:
        print_header(env.njoints, env.ndim)

    observation, info = env.reset(seed=args.seed)
    env.action_space.seed(seed=args.seed)
    if args.log:
        print_obs(observation, env.njoints, env.ndim)

    for i in range(1,args.steps):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)
        if args.log:
            print_obs(observation, env.njoints, env.ndim)
        if render_mode=="human":
            time.sleep(0.1)
        if terminated or truncated:
            observation, info = env.reset()

    env.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-env", type=str, default="r2",
        help="environment [r2,r3,r5] (default: r2)")
    parser.add_argument("-steps", type=int, default=10000,
        help="Execution steps (default: 10,000)")
    parser.add_argument("-seed", type=int, default=1000,
        help="Random seed (default: 1000)")
    parser.add_argument('--render', default = False, action ='store_true',
        help='Enable rendering')
    parser.add_argument('--log', default = False, action ='store_true',
        help='Enable data log')

    args = parser.parse_args()
    dorun(args)



