import dash
import dash_core_components as dcc
import dash_html_components as html

from src.gui.layout_graph import get_plot_layout
from definitions import PROCESSED_DATA_DIR
from src.gui.gui_interactions import load_daily_cases_plot_data

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

plot_layout = get_plot_layout(colors)
daily_cases_plot_object = {
    "data": load_daily_cases_plot_data(PROCESSED_DATA_DIR),
    "layout": plot_layout
}
print(daily_cases_plot_object)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Dutch Corona dashboard (PoC)',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='High level graphs', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': daily_cases_plot_object["data"],
            'layout': daily_cases_plot_object["layout"]
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)