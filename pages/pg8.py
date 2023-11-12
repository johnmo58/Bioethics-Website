import dash
from dash import dcc, html
import plotly.express as px

# Register the page with a specific path
dash.register_page(__name__, name='Chat Room')

# Creating a rectangle with specified style
rectangle_div = html.Div(
    "Chat Room Here",
    style={
        'width': '100%',
        'height': '400px',
        'background-color': 'white',
        'border': '2px solid black',
        'text-align': 'center',
        'line-height': '400px',  # Center text vertically
        'font-size': '20px',     # Adjust font size
        'margin-bottom': '20px',  # Add margin at the bottom
    }
)

# Adding the chat room text
text_content = """
This is the chat room where people's potential objections about the philosophical nature of this topic are listed.
"""

layout = html.Div(
    [
        rectangle_div,
        dcc.Markdown(text_content, style={'line-height': '2'}),
    ],
    style={'margin-left': '80px', 'margin-right': '100px'}  # Adjust the values as needed
)
