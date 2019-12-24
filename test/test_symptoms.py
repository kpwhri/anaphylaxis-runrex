import pytest

from anaphylaxis_nlp.algo.symptom import ASYSTOLE, SWELLING, SOB, HIVES


@pytest.mark.parametrize('text', [
    'asystole',
])
def test_matches_asystole(text):
    assert ASYSTOLE.matches(text)


@pytest.mark.parametrize('text', [
    'swelling',
    'oedema',
    'edema',
])
def test_matches_swelling(text):
    assert SWELLING.matches(text)


@pytest.mark.parametrize('text', [
    'hives',
    'rash',
    'urticaria',
])
def test_matches_hives(text):
    assert HIVES.matches(text)


@pytest.mark.parametrize('text', [
    'presents with s. o. b.',
    'shortness of breath',
    'short of breath',
    'dyspnea',
    'had difficulty breathing',
    'was difficult to breathe',
    'sob'
])
def test_matches_sob(text):
    assert SOB.matches(text)


