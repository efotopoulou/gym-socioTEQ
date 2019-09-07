from gym.envs.registration import register

register(
    id='socioTEQ-v0',
    entry_point='gym_socioTEQ.envs:SocioTEQEnv',
)
