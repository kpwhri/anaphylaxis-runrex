from runrex.algo.pattern import Pattern

ASYSTOLE = Pattern(
    rf'(asystole|cardiac flatline|cardiac arrest)'
)

HIVES = Pattern(
    rf'(hives|urticaria|rash)'
)

SWELLING = Pattern(
    rf'(swelling|o?edema)'
)

SOB = Pattern(
    rf'('
    rf'\bs o b\b|short\w* of breath\w*'
    rf'|dyspno?ea'
    rf'|difficult* (\w+ )?breath\w*'
    rf'|breathless(ness)?'
    rf'|(respiratory|pulmonary) distress'
    rf')'
)


ALL_SYMPTOMS = (ASYSTOLE, HIVES, SWELLING, SOB)
