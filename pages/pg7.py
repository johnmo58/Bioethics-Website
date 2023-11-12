import dash
from dash import dcc, html
import plotly.express as px

# Register the page with a specific path
dash.register_page(__name__, name="Example Objection")

text_content = """
To counter this objection, Thomson could emphasize the broader applicability of her argument by focusing on the underlying principles. Thomson's defense of abortion is not confined to the specific details of the violinist scenario but rather centers on the general concept of bodily autonomy and the right to decide what happens within one's own body.

Thomson might argue that her violinist analogy serves as an illustrative example rather than an exhaustive representation of all possible scenarios. The key point is the right to make decisions about one's body, and the violinist scenario is just one way to highlight the conflict between bodily autonomy and the fetus's right to life.

Additionally, Thomson could address Warren's objection by introducing the role of intentions and the willingness to assume the risk of pregnancy. She might argue that her argument extends to various pregnancy situations, acknowledging that individuals who willingly assume the risks of activities leading to pregnancy may still have the right to make decisions about their bodies.

With that in mind, consider a scenario where a person decides to order a pizza for dinner but unexpectedly faces a peculiar situation. The pizza delivery person arrives with not only the desired pizza but also a penguin.

In this scenario, Thomson's defense of abortion rights could be likened to the right of the person to decide what happens within their own living space. The key point is the autonomy to make decisions about one's immediate environment, akin to deciding who or what enters their home.

Now, to address Warren's objection, Thomson might argue that this pizza delivery analogy serves as a vivid but specific example, not an exhaustive representation of all potential scenarios. The emphasis here would be on the general concept of bodily autonomy and the right to decide about one's immediate surroundings, using the unexpected penguin as a symbol.

Thomson could then bring attention to the role of intentions and the willingness to assume unexpected consequences. She might argue that her defense extends to various unexpected situations, emphasizing that individuals who willingly engage in activities like ordering pizza, even if they end up with unanticipated companions, should still have the right to decide about their living space.

In essence, this comical analogy, aligned with Thomson's argument, highlights the broader principles of bodily autonomy and decision-making, even in unexpected circumstances. The scenario underlines the idea that individuals, despite unforeseen consequences, should maintain the right to make decisions about their immediate surroundings based on their initial intentions."""

# Image source
new_image_source = 'https://www.clio.com/wp-content/uploads/2023/08/Blog-Type-of-Objections-in-Court-1500x844.webp'

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
