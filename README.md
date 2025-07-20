# Prime Edit Site

A prototype bioinformatics tool for generating and scoring nucleotide sequence triples (spacer, PBS, RTT).

## Repository Structure

```
prime_edit_site/
│
├── app.py              # Flask web app entry point
├── funs.py             # API: input validation, imports real or mock triple logic
├── triple.py           # Real triple generation and scoring (edit here for production)
├── mock_triple.py      # Mock triple generation and scoring (for testing/demo)
├── templates/
│   ├── base.html       # Base HTML template (Bootstrap 5)
│   └── index.html      # Main page template
├── static/             # (Optional) Static files (CSS, JS, images)
└── README.md           # This file
```

## How It Works

- **app.py**: Handles web requests, form input, and rendering.
- **funs.py**: Validates input and delegates triple generation/scoring to either `triple.py` (real) or `mock_triple.py` (mock), based on the `USE_MOCK` flag.
- **triple.py**: Place your real scientific logic here. Functions: `generate_triples`, `score_triples`.
- **mock_triple.py**: Provides mock implementations for development/testing.
- **templates/**: Contains HTML templates using Bootstrap for a modern UI.

## Switching Between Mock and Real Logic

Edit `funs.py` and set:

```python
USE_MOCK = True  # Use mock logic (default)
USE_MOCK = False # Use real logic in triple.py
```

## Development

- Default form values are provided for easy testing.
- You can run the app and click "Generate" to see mock results.

## Adding Real Analysis

- Implement your real triple generation and scoring in `triple.py`.
- Ensure the function signatures match those in `mock_triple.py