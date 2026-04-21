from dataclasses import dataclass
from typing import Literal

SimBackend = Literal["mujoco_cpu", "mujoco_warp", "physx_cpu", "physx_cuda"]
# TODO (stao): we may want to differentiate between a batch renderer vs non-batch renderer
RenderBackend = Literal["mujoco_warp", "sapien"]

@dataclass
class BackendCfg:
    sim_backend: SimBackend
    render_backend: RenderBackend

def parse_backend(sim_backend: SimBackend, render_backend: RenderBackend) -> BackendCfg:
    return BackendCfg(sim_backend=sim_backend, render_backend=render_backend)