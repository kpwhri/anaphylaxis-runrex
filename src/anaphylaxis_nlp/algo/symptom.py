from runrex.algo.pattern import Pattern

ASYSTOLE = Pattern(
    rf'(asystole|cardiac flatline|cardiac arrest)'
)

HIVES = Pattern(
    rf'\b(hives|urticaria|rash)\b'
)

SWELLING = Pattern(
    rf'\b(swelling|o?edema)\b'
)

SOB = Pattern(
    rf'('
    rf'\bs o b\b|short\w* of breath\w*'
    rf'|dyspno?ea'
    rf'|difficult\w* (\w+ )?breath\w*'
    rf'|breathless(ness)?'
    rf'|(respiratory|pulmonary) distress'
    rf')'
)


ALL_SYMPTOMS = (ASYSTOLE, HIVES, SWELLING, SOB)
