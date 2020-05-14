"""
Captures suddenness of an event (specifically, for symptoms of anaphylactic shock).

"""
from runrex.algo.pattern import Pattern
from runrex.algo.result import Status, Result

from anaphylaxis_nlp.algo.epinephrine import hypothetical
from anaphylaxis_nlp.algo.symptom import ALL_SYMPTOMS
from runrex.text import Document


class SuddennessStatus(Status):
    NONE = -1
    WITHIN_TIME = 1
    SUDDEN = 2
    WITHIN_TIME_SYMPTOM = 3
    SUDDEN_SYMPTOM = 4


WITHIN_TIME = Pattern(
    rf'(within|over) (a (few|couple)|the next|\d+)? (minute|hour)s?',
    negates=[hypothetical]
)

SUDDEN = Pattern(
    rf'('
    rf'(sudden|abrupt|rapid|quick|swift|without warning|immediate|shortly)(ly)?'
    rf'|after \w+ing'
    rf'|began (to )?(hav|expierenc)\w+'
    rf'|acute onset'
    rf')',
    negates=[hypothetical]
)


def _search_suddenness(document: Document):
    for sentence in document.select_sentences_with_patterns(WITHIN_TIME):
        text = None
        for text, start, end in sentence.get_patterns(*ALL_SYMPTOMS):
            yield SuddennessStatus.WITHIN_TIME_SYMPTOM, text, start, end
        if not text:
            yield SuddennessStatus.WITHIN_TIME, sentence.match_text, sentence.match_start, sentence.match_end
    for sentence in document.select_sentences_with_patterns(SUDDEN):
        text = None
        for text, start, end in sentence.get_patterns(*ALL_SYMPTOMS):
            yield SuddennessStatus.SUDDEN_SYMPTOM, text, start, end
        if not text:
            yield SuddennessStatus.SUDDEN, sentence.match_text, sentence.match_start, sentence.match_end


def get_suddenness(document: Document, expected=None):
    for status, text, start, end in _search_suddenness(document):
        yield Result(status, status.value, expected=expected, text=text, start=start, end=end)
