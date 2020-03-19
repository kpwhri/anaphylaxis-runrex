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
        found = 0
        for _, start, end in sentence.get_patterns(PRIMARY):
            found = 1
            yield DxStatus.PRIMARY, sentence.text, start, end
        for _, start, end in sentence.get_patterns(DIFFERENTIAL):
            found = 1
            yield DxStatus.DIFFERENTIAL, sentence.text, start, end
        for _, start, end in sentence.get_patterns(VISIT):
            found = 1
            yield DxStatus.VISIT, sentence.text, start, end
        for _, start, end in sentence.get_patterns(FOLLOWUP):
            found = 1
            yield DxStatus.FOLLOWUP, sentence.text, start, end
        for _, start, end in sentence.get_patterns(DIAGNOSIS):
            found = 1
            yield DxStatus.GENERIC, sentence.text, start, end
        for _, start, end in sentence.get_patterns(FINDING):
            found = 1
            yield DxStatus.FINDING, sentence.text, start, end
        if not found:
            yield DxStatus.NONE, sentence.text, None, None


def get_anaphylaxis_dx(document: Document, expected=None):
    for status, text, start, end in _search_anaphylaxis_dx(document):
        yield Result(status, status.value, expected=expected,
                     text=text, start=start, end=end)
