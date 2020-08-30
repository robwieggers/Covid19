"""
Functionality to get layout of graphs
"""


def get_plot_layout(colors: dict = None) -> dict:
    """

    Args:
        colors: definition of colors like background, text etc

    Returns: layout definition
    """

    if colors is None:
        colors = get_default_colors()

    layout = {
        'plot_bgcolor': colors['background'],
        'paper_bgcolor': colors['background'],
        'font': {
            'color': colors['text']
        }
    }
    return layout


def get_default_colors() -> dict:
    """
    return default color definition

    Returns: color definition

    """
    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }
    return colors