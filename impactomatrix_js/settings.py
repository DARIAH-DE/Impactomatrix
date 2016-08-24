# -*- coding: utf-8 -*-
import os
current_dir = os.path.dirname(os.path.realpath(__file__))


# REQUIRED: Which templates do you want to generate? (Use relative paths here!)
# Use strings (with single or double quotes), and separate each template in a line terminated with a comma. Such as examples below.
OUTPUT_TEMPLATES = [
    'index.html',
    'external-impact.html',
    'innovation.html',
    'coherence.html',
    'collaboration.html',
    'communication.html',
    'competitiveness.html',
    'data-security.html',
    'dissemination.html',
    'education.html',
    'effectivity.html',
    'efficiency.html',
    'external-impact.html',
    'funding-perspective.html',
    'index.html',
    'innovation.html',
    'integration.html',
    'publications.html',
    'relevance.html',
    'reputation.html',
    'sustainability.html',
    'transfer-expertise.html',
    'transfer-knowledge.html',
    'transparency.html',
    'usage.html'
]

# OPTIONAL: Where are the skeleton (.jinja) templates? - Defaults to 'jinja_templates' folder inside this project
INPUT_FOLDER = current_dir + '/impactomatrix_templates'

# OPTIONAL: Which folder does it dump generated templates? - Defaults to 'html_templates' folder inside this project
OUTPUT_FOLDER = current_dir + '/static_impactomatrix'
