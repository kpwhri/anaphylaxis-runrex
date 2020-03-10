from runrex.algo.pattern import Pattern, Document
from runrex.algo.result import Status, Result


class ObsStatus(Status):
    NONE = -1
    OBSERVATION = 1
    MONITORING = 2


overnight = r'(observation|overnight|extended|hospital|unit|icm?u|neuro)'
admit = r'\b(add?mit|admission|transfer|xfer)\w*'

OBSERVATION = Pattern(
    rf'{admit} (\w+ )?((for|to) )?(\w+ )?{overnight}'
)

MONITORING = Pattern(
    rf'(close|continu)\w* ((to|for) )?(\w+ )?(monitor|observ|check|follow|track)\w*'
)


def _search_observation(document: Document):
    for sentence in document:
        if sentence.has_pattern(OBSERVATION):
            yield ObsStatus.OBSERVATION, sentence.text
        if sentence.has_pattern(MONITORING):
            yield ObsStatus.MONITORING, sentence.text


def get_observation(document: Document, expected=None):
    for status, text in _search_observation(document):
        yield Result(status, status.value, expected=expected,
                     text=text)
