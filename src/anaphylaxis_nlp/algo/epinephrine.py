"""
Features having to do with epinephrine. Of particular interest:

* name 'epinephrine' or equivalent
* number of mentions (this is aggregation statistic)
* indication that multiple epinephrine shots have been taken/received

"""
from runrex.algo.pattern import Document, Pattern
from runrex.algo.result import Status, Result

negation = r'((does|wo|has)n t\b|refuses?|\bnot\b|den(y|ies))'
instructions = r'(instruct(ions?|ed)?)'
hypothetical = r'(should|ought|\bif\b|please)'


class EpiStatus(Status):
    NONE = -1
    EPI_MENTION = 1
    MULTIPLE_EPI = 2
    PREVIOUS_EPI = 3
    ALLERGY_MED = 4
    EPI_USE = 5
    HAS_EPI = 6


epinephrine = rf'(\bepi\b|epinephrine|epi pend?s?)'
another = rf'(second|third|fourth|fifth|another|2nd|3rd|4th|5th)'

RELATED_MEDS = Pattern(  # only in sentences with epi mention
    rf'('
    rf'lorat[ai]dine?|claritin|claratyne|benadryl|inhaler'
    rf'|solu medrol|cetirizine|zyrtec'
    rf')'
)

EPI_USE = Pattern(
    rf'{epinephrine}',
    negates=[negation, instructions],
    requires=[r'\bpost\b', r'\b(gave|given)\b', r'\bmg\b', r'\bused\b',
              r'\bdose\b', r'\badmin(istered)?\b', 'already (given|gave)']
)

EPI_HAS = Pattern(
    rf'('
    rf'\b(has|carr(y|ies))\b'
    rf'|\brx\b|prescription|prescribed'
    rf'|expired'
    rf'|pick up'
    rf')',
    negates=[negation, instructions],
)

MULTIPLE_EPI = Pattern(
    rf'('
    rf'(two|three|four) (times|\bx\b|doses?|injections?|{epinephrine})'
    rf'|repeated'
    rf'|{another} ({epinephrine}|time|dose|injection)'
    rf')',
    negates=[negation]
)

ANY_EPI = Pattern(
    rf'{epinephrine}'
)


def _epinephrine_use(document: Document):
    for sentence in document.select_sentences_with_patterns(ANY_EPI):
        found = 0
        if sentence.has_pattern(RELATED_MEDS):
            found = 1
            yield EpiStatus.ALLERGY_MED, sentence.text
        if sentence.has_pattern(MULTIPLE_EPI):
            found = 1
            yield EpiStatus.MULTIPLE_EPI
        if sentence.has_pattern(EPI_HAS):
            found = 1
            yield EpiStatus.HAS_EPI
        if sentence.has_pattern(RELATED_MEDS):
            found = 1
            yield EpiStatus.ALLERGY_MED
        if not found:
            yield EpiStatus.EPI_MENTION, sentence.text


def get_epinephrine(document: Document, expected=None):
    for status, text in _epinephrine_use(document):
        yield Result(status, status.value, expected=expected,
                     text=text)
