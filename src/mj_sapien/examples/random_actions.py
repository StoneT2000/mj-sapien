from dataclasses import dataclass

import torch
import tyro
import warp as wp
from mj_sapien.envs.base_env import BaseEnv, BaseEnvConfig
from mj_sapien.envs.tasks.pick_cube import PickCubeTask, PickCubeTaskConfig


@dataclass
class Args:
    num_envs: int = 1
    env_cfg: BaseEnvConfig = BaseEnvConfig()


def main(args: Args):
    cfg = args.env_cfg
    env = PickCubeTask(cfg)
    env.reset()
    env.scene.viewer.show_ui = True
    while env.scene.viewer.is_running():
        for t in range(100000000):
            action = torch.rand(size=(8, )) * 2 - 1
            wp.copy(dest=env.scene.control.joint_target_pos[:7], src=wp.from_torch(action[:7]))
            if env.scene.viewer.should_step():
                obs, rew, term, trunc, info = env.step(action)
                print(t, obs)
            env.render()


if __name__ == "__main__":
    args = tyro.cli(Args)
    main(args)
