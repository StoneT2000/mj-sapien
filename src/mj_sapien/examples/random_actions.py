from dataclasses import dataclass
import tyro

from mj_sapien.envs.base_env import BaseEnv, BaseEnvCfg

@dataclass
class Args:
    num_envs: int = 1
    env_cfg: BaseEnvCfg = BaseEnvCfg()

def main(args: Args):
    cfg = args.env_cfg
    env = BaseEnv(cfg)

if __name__ == "__main__":
    args = tyro.cli(Args)
    main(args)