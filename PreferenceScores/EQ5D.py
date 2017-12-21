
# EQ-5D regression coefficients
Constant = 0.081
N3 = 0.269
dictCoefficients = {'Mobility':             [0, 0.069, 0.314],
                    'Self-Care':            [0, 0.104, 0.214],
                    'Usual Activity':       [0, 0.036, 0.094],
                    'Pain/Discomfort':      [0, 0.123, 0.386],
                    'Anxiety/Depression':   [0, 0.071, 0.236]};


def get_score(mobility, self_care, usual_activity, pain_discomfort, anxiety_depression):
    """
    :param mobility: level of mobility dimension
    :param self_care: level of self-care dimension
    :param usual_activity: level of usual activity dimension
    :param pain_discomfort: level of pain/discomfort dimension
    :param anxiety_depression: level of anxiety/depression dimension
    :return: EQ-5D preference score
    """

    # ensure the entered health dimension levels are acceptable
    if not(mobility in [1, 2, 3]):
        raise ValueError('Mobility level can take only 1, 2 or 3')
    if not(self_care in [1, 2, 3]):
        raise ValueError('Self-care level can take only 1, 2 or 3')
    if not(usual_activity in [1, 2, 3]):
        raise ValueError('Usual activity level can take only 1, 2 or 3')
    if not(pain_discomfort in [1, 2, 3]):
        raise ValueError('Pain/discomfort level can take only 1, 2 or 3')
    if not(anxiety_depression in [1, 2, 3]):
        raise ValueError('Anxiety level can take only 1, 2 or 3')

    score = 1   # start by setting score to 1

    # check if the constant term should be subtracted.
    if mobility * self_care * usual_activity * pain_discomfort * anxiety_depression > 1:
        score -= Constant

    # check if the N3 constant should be subtracted.
    if max(mobility, self_care, usual_activity, pain_discomfort, anxiety_depression) == 3:
        score -= N3

    # subtract the coefficients of other dimensions
    score -= dictCoefficients['Mobility'][mobility - 1]
    score -= dictCoefficients['Self-Care'][self_care - 1]
    score -= dictCoefficients['Usual Activity'][usual_activity - 1]
    score -= dictCoefficients['Pain/Discomfort'][pain_discomfort - 1]
    score -= dictCoefficients['Anxiety/Depression'][anxiety_depression - 1]

    return score