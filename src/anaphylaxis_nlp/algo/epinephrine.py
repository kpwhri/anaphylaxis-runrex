"""
Features having to do with epinephrine. Of particular interest:

* name 'epinephrine' or equivalent
* number of mentions (this is aggregation statistic)
* indication that multiple epinephrine shots have been taken/received

"""
from runrex.algo.pattern import Document, Pattern
from runrex.algo.result import Status, Result

negation = r'((does|wo|has)n t\b|refuses?|\bnot\b|den(y|ies)|\bnor\b|neither)'
instructions = r'(instruct(ions?|ed)?|do not|discussed)'
hypothetical = r'(should|ought|\bif\b|please|\bmay\b|shall|call 911)'


class EpiStatus(Status):
    NONE = -1
    EPI_MENTION = 1
    MULTIPLE_EPI = 2
    PREVIOUS_EPI = 3
    ALLERGY_MED = 4
    EPI_USE = 5
    HAS_EPI = 6
    HISTORICAL_EPI = 7


epinephrine = rf'(\bepi\b|\bepinephrine|\bepi pend?s?|adrenalin\b|adrenaclick)'
another = rf'(second|third|fourth|fifth|another|2nd|3rd|4th|5th)'
times_ge2 = rf'(2|3|4|two|three|four)'
prescription = rf'(take\b|ordered|prescription|pr[eo]scribed|plan|injector' \
               rf'|as needed|medications?|warning|\bkit\b)'

RELATED_MEDS = Pattern(  # only in sentences with epi mention
    rf'('
    rf'lorat[ai]dine?|claritin|claratyne|benadryl|inhaler'
    rf'|solu medrol|cetirizine|zyrtec|duoneb'
    rf')',
    negates=[prescription]
)

EPI_USE = Pattern(
    rf'\b('
    rf'after|post|(gave|given|will give)|m[gl]|used|dose|admin(istred)?'
    rf'|already|tolerated|initial|responded|received|required|(took|taken)'
    rf'|amp(ules?)?|drip'
    rf'|1st'
    rf')\b',
    negates=[negation, instructions, hypothetical, prescription],
)

EPI_HAS = Pattern(
    rf'('
    rf'\b(has|carr(y|ies))\b'
    rf'|\brx\b|prescription|prescribed'
    rf'|expired'
    rf'|pick up'
    rf'|refill(ed)?'
    rf'|medications?'
    rf')',
    negates=[negation, instructions, hypothetical],
)

MULTIPLE_EPI = Pattern(
    rf'('
    rf'{times_ge2} (times|x\b|doses?|injections?|{epinephrine})'
    rf'|(twice|thrice)'
    rf'|x {times_ge2}'
    rf'|repeated'
    rf'|{another} ({epinephrine}|time|dose|injection)'
    rf')',
    negates=[negation, hypothetical, instructions, prescription]
)


HISTORICAL_EPI = Pattern(  # ever had epi before
    rf'('  # can't find any examples
    rf''
    rf')'
)


ANY_EPI = Pattern(
    rf'{epinephrine}'
)


def _epinephrine_use(document: Document):
    for sentence in document.select_sentences_with_patterns(ANY_EPI):
        found = 0
        if sentence.has_pattern(EPI_HAS):
            found = 1
            yield EpiStatus.HAS_EPI
            continue   # ?? - probably non-event
        if sentence.has_pattern(RELATED_MEDS):
            found = 1
            yield EpiStatus.ALLERGY_MED, sentence.text
        if sentence.has_pattern(MULTIPLE_EPI):
            found = 1
            yield EpiStatus.MULTIPLE_EPI
        if sentence.has_pattern(RELATED_MEDS):
            found = 1
            yield EpiStatus.ALLERGY_MED
        if not found:
            yield EpiStatus.EPI_MENTION, sentence.text


def get_epinephrine(document: Document, expected=None):
    for status, text in _epinephrine_use(document):
        yield Result(status, status.value, expected=expected,
                     text=text)
