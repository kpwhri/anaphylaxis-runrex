import pytest

from anaphylaxis_nlp.algo.observation import OBSERVATION, MONITORING


@pytest.mark.parametrize('text', [
    'admit overnight',
    'admit for observation',
    'transferred to main hospital for monitoring',
    'transfered to icu',  # intentional misspelling
])
def test_observation(text):
    assert OBSERVATION.matches(text)


@pytest.mark.parametrize('text', [
    'close monitoring',
])
def test_monitoring(text):
    assert MONITORING.matches(text)
