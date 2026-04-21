# mj-sapien
- currently just a personal investigation into mj-warp, sapien, and simulation infra/framework design ideas

## planning and fixes
- Viser based viewer with option to still use mujoco/sapien default viewers
  - viewer "extensions/mods" for various workflows
    - e.g. RL workflow use a RL tracking mod of sorts, basically what MJLab does
    - Robot modelling workflow. Lot more utilities to inspect everything about a robot model
- typed everything from the start
- better decision making on when to go functional vs. make a class out of something
- better data and asset management tooling
- better motion planning tooling (probably just copy pyroki/mink code, get rid of mplib)
- support combining `Agent` classes instead of a hacky `MultiAgent` class. Would mean properly combining mjcfs/urdf files
- avoiding package bloat. mistake previously including too many asset files that were often unused and should've been downloaded by choice
- using uv, better and more strict linting
- don't assume there must exist an agent, can have an empty agent
- Overall better class hierarchy, with better figures to explain it all
- pufferlib if possible instead of old PPO code
- sim2real deployment tooling + sapien compatible system-id, following the steps of mj sys ID + own tricks
- throw warnings properly, log everything properly
- returned rewards should be a dict, not one value. Support more configurable experimentation/config tooling for rewards and doing curricula with rewards.
- automated cloud tests for performance + check rendering
- document API design decisions and why I made certain choices so I can blog about it
