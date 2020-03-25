from runrex.algo.pattern import Pattern, Document
from runrex.algo.result import Status, Result

from anaphylaxis_nlp.algo.epinephrine import hypothetical


class ObsStatus(Status):
    NONE = -1
    OBSERVATION = 1
    MONITORING = 2


overnight = r'(observation|overnight|extended|hospital|unit|[i1]cm?u|neuro)'
admit = r'\b(add?mit|admission|transfer|xfer)\w*'

OBSERVATION = Pattern(
    rf'{admit} (\w+ )?((for|to) )?(\w+ )?{overnight}',
    negates=[hypothetical]
)

MONITORING = Pattern(
    rf'(close|continu)\w* ((to|for) )?(\w+ )?(monitor|observ|check|follow|track)\w*',
    negates=[hypothetical]
)


def _search_observation(document: Document):
    for sentence in document:
        for text, start, end in sentence.get_patterns(OBSERVATION):
            yield ObsStatus.OBSERVATION, text, start, end
        for text, start, end in sentence.get_patterns(MONITORING):
            yield ObsStatus.MONITORING, text, start, end


def get_observation(document: Document, expected=None):
    for status, text, start, end in _search_observation(document):
        yield Result(status, status.value, expected=expected,
                     text=text, start=start, end=end)
