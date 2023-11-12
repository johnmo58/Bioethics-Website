import dash
from dash import dcc, html, Input, Output

# Register the page with a specific path
dash.register_page(__name__, name="Potential Objection")

text_content = """
How do you think Thomson could object to Warren's argument? What philosphical ideologies will you use to object to Warren?
"""

# Add a Textarea component for user input
user_input_box = dcc.Textarea(
    id='user-input',
    placeholder='Type your objection here...',
    style={'width': '100%', 'height': '100px'},
)

# Add a Submit button
submit_button = html.Button('Submit', id='submit-button', n_clicks=0)

# Add a div to display submitted text
submitted_text_div = html.Div(id='submitted-text-container', style={'margin-top': '20px', 'border': '1px solid black', 'padding': '10px', 'min-height': '100px', 'overflow-y': 'auto'})

# Image source
new_image_source = 'https://static.scientificamerican.com/sciam/cache/file/BB881E9D-AC85-4614-B36E001BD4B1ECF6_source.jpg?w=590&h=800&48350384-C4FE-4984-945D026305C9FEA1'


layout = html.Div(
    [
        dcc.Markdown(text_content, style={'line-height': '2'}),
        html.Div(
            html.Img(src=new_image_source, alt='Mary Anne Warren', style={'width': '100%', 'max-width': '500px', 'margin': 'auto'}),
            style={'text-align': 'center'}
        ),
        html.Br(),  # Add a line break for spacing
        html.Label('Objection:'),
        user_input_box,
        submit_button,
        submitted_text_div,
    ],
    style={'margin-left': '80px', 'margin-right': '100px'}  # Adjust the values as needed
)

# Dash callback to update submitted text
@dash.callback(
    Output('submitted-text-container', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.State('user-input', 'value')]
)
def update_submitted_text(n_clicks, user_input):
    if n_clicks > 0 and user_input.strip() != '':
        return [
            html.Br(),
            html.P(f"User Submission: {user_input}"),
            html.Hr(),
        ]
    else:
        return []

if __name__ == '__main__':
    dash.run_server()
