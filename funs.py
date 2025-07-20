USE_MOCK = True  # Toggle this to switch between mock and real

if USE_MOCK:
    from mock_triple import generate_triples, score_triples
else:
    from triple import generate_triples, score_triples

def validate_inputs(sequence: str, number: int, character: str) -> (bool, str):
    if not sequence:
        return False, 'Input sequence cannot be empty.'
    if not isinstance(number, int):
        return False, 'Integer parameter is required.'
    if not character or len(character) != 1:
        return False, 'Character parameter must be a single character.'
    return True, 'OK'