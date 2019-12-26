import pytest

from anaphylaxis_nlp.algo.epinephrine import ANY_EPI, RELATED_MEDS, EPI_HAS, MULTIPLE_EPI


@pytest.mark.parametrize('text', [
    'epi given',
    'has an epipen at home',
    'epinephrine dose',
])
def test_matches_any_epinephrine(text):
    assert ANY_EPI.matches(text)


@pytest.mark.parametrize('text', [
    'loratidine',
    'claritin',
    'took epipen and inhaler',
    'solu-medrol',
    'solumedrol',
])
def test_matches_related_meds(text):
    assert RELATED_MEDS.matches(text)


@pytest.mark.parametrize('text', [
    'gave a 2nd dose',
    '3rd injection',
    'given another epi injection',
])
def test_matches_multiple_epi(text):
    assert MULTIPLE_EPI.matches(text)


@pytest.mark.parametrize('text', [
    'carries an epipen',
    'rx for epi',
    'pick up from pharmacy',
])
def test_matches_has_epi(text):
    assert EPI_HAS.matches(text)
