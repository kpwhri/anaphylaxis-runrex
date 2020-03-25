from runrex.algo.pattern import Pattern, Document
from runrex.algo.result import Status, Result

from anaphylaxis_nlp.algo.epinephrine import hypothetical, negation


class DxStatus(Status):
    NONE = -1
    PRIMARY = 1
    DIFFERENTIAL = 2
    ASSOCIATED = 3
    GENERIC = 4
    VISIT = 5
    FOLLOWUP = 6
    ACTIVE = 7
    FINDING = 8


diagnosis = r'\b(diagnos[ie]s|dx)\b'

ANAPHYLAXIS = Pattern(
    rf'(anaphyla\w+|t78\.0)'
)

FINDING = Pattern(
    rf'(evidence of|caused by|symptoms of|because of|on account of'
    rf'|due to|\bin|consistent with) (acute|mild|severe)? anaphyla\w+',
    negates=('not?', negation)
)

DIAGNOSIS = Pattern(
    rf'{diagnosis}',
    negates=('differential', hypothetical)
)

PRIMARY = Pattern(
    rf'('
    rf'(primary|main|princip(le|al)) (discharge )?{diagnosis}'
    rf'|secondary to'
    rf')'
)

DIFFERENTIAL = Pattern(
    rf'differential {diagnosis}',
    negates=[hypothetical]
)

VISIT = Pattern(
    rf'(visit|admission) {diagnosis}',
    negates=[hypothetical]
)

ASSOCIATED = Pattern(
    rf'associated {diagnosis}',
    negates=[hypothetical]
)

FOLLOWUP = Pattern(
    rf'follow up {diagnosis}',
    negates=[hypothetical]
)

ACTIVE = Pattern(
    rf'active {diagnosis}',
    negates=[hypothetical]
)


def _search_anaphylaxis_dx(document: Document):
    for sentence in document.select_sentences_with_patterns(ANAPHYLAXIS):
        text = None
        for text, start, end in sentence.get_patterns(PRIMARY):
            yield DxStatus.PRIMARY, text, start, end
        for text, start, end in sentence.get_patterns(DIFFERENTIAL):
            yield DxStatus.DIFFERENTIAL, text, start, end
        for text, start, end in sentence.get_patterns(VISIT):
            yield DxStatus.VISIT, text, start, end
        for text, start, end in sentence.get_patterns(FOLLOWUP):
            yield DxStatus.FOLLOWUP, text, start, end
        for text, start, end in sentence.get_patterns(DIAGNOSIS):
            yield DxStatus.GENERIC, text, start, end
        for text, start, end in sentence.get_patterns(FINDING):
            yield DxStatus.FINDING, text, start, end
        if not text:
            yield DxStatus.NONE, sentence.match_text, sentence.match_start, sentence.match_end


def get_anaphylaxis_dx(document: Document, expected=None):
    for status, text, start, end in _search_anaphylaxis_dx(document):
        yield Result(status, status.value, expected=expected,
                     text=text, start=start, end=end)
