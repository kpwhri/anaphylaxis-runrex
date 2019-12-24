"""
Captures suddenness of an event (specifically, for symptoms of anaphylactic shock).

"""
from runrex.algo.pattern import Pattern, Document
from runrex.algo.result import Status, Result

from anaphylaxis_nlp.algo.symptom import ALL_SYMPTOMS


class SuddennessStatus(Status):
    NONE = -1
    WITHIN_TIME = 1
    SUDDEN = 2
    WITHIN_TIME_SYMPTOM = 3
    SUDDEN_SYMPTOM = 4


WITHIN_TIME = Pattern(
    rf'within '
    rf'(a (few|couple)|\d+)?'
    rf'minutes?'
)

SUDDEN = Pattern(
    rf'(sudden|abrupt|rapid|quick|swift|without warning)(ly)?'
)


def _search_suddenness(document: Document):
    for sentence in document.select_sentences_with_patterns(WITHIN_TIME):
        if sentence.has_patterns(*ALL_SYMPTOMS):
            yield SuddennessStatus.WITHIN_TIME_SYMPTOM, sentence.text
        else:
            yield SuddennessStatus.WITHIN_TIME, sentence.text
    for sentence in document.select_sentences_with_patterns(SUDDEN):
        if sentence.has_patterns(*ALL_SYMPTOMS):
            yield SuddennessStatus.SUDDEN_SYMPTOM, sentence.text
        else:
            yield SuddennessStatus.SUDDEN, sentence.text


def get_suddenness(document: Document, expected=None):
    for status, text in _search_suddenness(document):
        yield Result(status, status.value, expected=expected, text=text)
