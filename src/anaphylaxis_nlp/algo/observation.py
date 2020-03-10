from runrex.algo.pattern import Pattern
from runrex.algo.result import Status


class ObsStatus(Status):
    NONE = -1
    OBSERVATION = 1
    MONITORING = 2


overnight = r'(observation|overnight|extended|hospital|unit|icm?u|neuro)'
admit = r'\b(add?mit|admission|transfer|xfer)\w*'

OBSERVATION = Pattern(
    rf'{admit} ((for|to) )?(\w+ )?{overnight}'
)

MONITORING = Pattern(
    rf'(close|continu)\w* ((to|for) )?(\w+ )?(monitor|observ|check|follow|track)\w*'
)
