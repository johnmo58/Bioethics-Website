import dash
from dash import dcc, html
import plotly.express as px

# Register the page with a specific path
dash.register_page(__name__, name="Thomson's Stance")

text_content = """
Thomson constructs her primary argument through a hypothetical scenario that prompts readers to envision waking up in a hospital, intricately connected to life support systems and linked to an unconscious, renowned violinist. The individual's kidneys function as life-sustaining filters for the violinist's blood, and severing this connection would result in the violinist's demise (Thomson, p. 48-49). Despite asserting that it would be a "great kindness" to remain connected to the violinist in this scenario (Thomson, p. 49), Thomson contends that there is no moral obligation to do so. Consequently, she argues that it becomes ethically permissible to terminate the life of the violinist, even though he possesses a fundamental right to life.

Thomson strategically utilizes this thought experiment to draw parallels with the complex issue of pregnancy. For the sake of argument, she assumes that the fetus, akin to the unconscious violinist, possesses an inherent right to life. In both scenarios, the sustenance of another life depends on the bodily functions of an individual. Drawing a parallel between justifiably terminating the connection with the violinist by unhooking oneself and the act of abortion, Thomson's argument aims to illustrate that even if the fetus holds a right to life, abortion may still be morally acceptable. In this context, the fetus's right to life does not confer upon it the entitlement to utilize the woman's body. Thomson contends that the woman's right to bodily integrity can take precedence over the fetus's right to life, analogous to how it supersedes the violinist's right to life in the thought experiment.
"""

# Image source
image_source = 'https://www.thebritishacademy.ac.uk/media/images/judith-thomson.2e16d0ba.fill-400x400.format-png.png'

df = px.data.gapminder()

layout = html.Div(
    [
        dcc.Markdown(text_content, style={'line-height': '2'}),
        html.Div(
            html.Img(src=image_source, alt='Judith Thomson', style={'width': '100%', 'max-width': '500px', 'margin': 'auto'}),
            style={'text-align': 'center'}
        ),
    ],
    style={'margin-left': '80px', 'margin-right': '100px'}  # Adjust the values as needed
)
