import dash
from dash import dcc, html
import plotly.express as px

# Register the page with a specific path
dash.register_page(__name__, name="Warren's Argument")

text_content = """
In her critique of Judith Thomson's argument presented in "A Defense of Abortion," Mary Anne Warren challenges the scope and implications of Thomson's violinist analogy. Warren underscores a critical aspect of Thomson's scenario – the involuntary nature of being kidnapped and connected to the violinist. She contends that Thomson's analogy applies only to a limited subset of pregnancies, most notably those resulting from rape. Warren highlights Thomson's acknowledgment that in cases where an individual is clearly responsible for becoming pregnant, as if they had "invited the fetus in," Thomson herself concedes that abortion may not be permissible.

However, Warren goes further by examining scenarios in which pregnancy occurs after voluntarily taking a risk of becoming pregnant, such as using fallible birth control methods. To explore these situations, Warren introduces another hypothetical – a lottery where individuals might be chosen to be connected to an ailing violinist. If one voluntarily enters the lottery and is selected, Warren questions whether it would be permissible to disconnect oneself. According to Warren, Thomson's framework suggests that taking a known risk, even in the context of a large lottery, commits individuals to accept the consequences if chosen. Extrapolating from Thomson's account, Warren argues that even a minimal risk of pregnancy could, by analogy, bind individuals to carry a pregnancy to term. This conclusion, Warren contends, is implausible, leading her to reject Thomson's reasoning.

In essence, Warren strengthens her case against Thomson by highlighting the limited applicability of the original analogy and extending the critique to scenarios involving voluntary but risky behavior, ultimately finding Thomson's conclusions to be untenable and dismissing the validity of her reasoning.
"""

# Image source
new_image_source = 'https://www.bmj.com/content/bmj/365/bmj.l1531/F1.medium.jpg'

df = px.data.gapminder()

layout = html.Div(
    [
        dcc.Markdown(text_content, style={'line-height': '2'}),
        html.Div(
            html.Img(src=new_image_source, alt='Mary Anne Warren', style={'width': '100%', 'max-width': '500px', 'margin': 'auto'}),
            style={'text-align': 'center'}
        ),
    ],
    style={'margin-left': '80px', 'margin-right': '100px'}  # Adjust the values as needed
)
