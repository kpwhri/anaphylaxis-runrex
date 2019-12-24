from runrex.algo.pattern import Pattern, Document
from runrex.algo.result import Status, Result


class DxStatus(Status):
    NONE = -1
    PRIMARY = 1
    DIFFERENTIAL = 2
    ASSOCIATED = 3
    GENERIC = 4
    VISIT = 5
    FOLLOWUP = 6
    ACTIVE = 7


diagnosis = r'\b(diagnos[ie]s|dx)\b'

ANAPHYLAXIS = Pattern(
    rf'(anaphyla(xis|ctic)|t78\.0)'
)

DIAGNOSIS = Pattern(
    rf'{diagnosis}',
    negates=('differential',)
)

PRIMARY = Pattern(
    rf'(primary|main|princip(le|al)) (discharge )?{diagnosis}'
)

DIFFERENTIAL = Pattern(
    rf'differential {diagnosis}'
)

VISIT = Pattern(
    rf'(visit|admission) {diagnosis}'
)

ASSOCIATED = Pattern(
    rf'associated {diagnosis}'
)

FOLLOWUP = Pattern(
    rf'follow up {diagnosis}'
)

ACTIVE = Pattern(
    rf'active {diagnosis}'
)


def _search_anaphylaxis_dx(document: Document):
    for sentence in document.select_sentences_with_patterns(ANAPHYLAXIS):
        if sentence.has_pattern(PRIMARY):
            yield DxStatus.PRIMARY, sentence.text
        elif sentence.has_pattern(DIFFERENTIAL):
            yield DxStatus.DIFFERENTIAL, sentence.text
        elif sentence.has_pattern(VISIT):
            yield DxStatus.VISIT, sentence.text
        elif sentence.has_pattern(FOLLOWUP):
            yield DxStatus.FOLLOWUP, sentence.text
        elif sentence.has_pattern(DIAGNOSIS):
            yield DxStatus.GENERIC, sentence.text


def get_anaphylaxis_dx(document: Document, expected=None):
    for status, text in _search_anaphylaxis_dx(document):
        yield Result(status, status.value, expected=expected,
                     text=text)
