import dash
from dash import dcc, html
import plotly.express as px

# Register the page with a specific path
dash.register_page(__name__, name="Current Views on Abortion")

text_content = """
While public support for legal abortion has fluctuated some in two decades of polling, it has remained relatively stable over the past several years. In 2022, 61% say abortion should be legal in all or most cases, while 37% say it should be illegal in all or most cases.  
"""

# Image sources
image_source1 = 'https://www.pewresearch.org/wp-content/uploads/2022/06/FT_22.06.07_Abortion_feature.png?w=1200&h=628&crop=1'
image_source2 = 'https://static01.nyt.com/images/2022/05/03/upshot/public-opinion-embed-1651644883275/public-opinion-embed-1651644883275-superJumbo-v5.png'

df = px.data.gapminder()

layout = html.Div(
    [
        dcc.Markdown(text_content, style={'line-height': '2'}),
        html.Div(
            html.Img(src=image_source1, alt='Judith Thomson', style={'width': '100%', 'max-width': '500px'}),
            style={'text-align': 'center', 'margin': 'auto'}
        ),
        dcc.Markdown("""
In states contemplating the implementation of additional abortion restrictions, individuals generally express the belief that abortion should be largely or entirely prohibited, according to an analysis conducted by The New York Times based on extensive national surveys conducted over the past decade. In the 13 states with enacted "trigger laws" designed to swiftly outlaw abortion if Roe v. Wade is overturned, an average of 43 percent of adults assert that abortion should be legal in most or all cases, while 52 percent advocate for its illegality in most or all cases.  

In states possessing pre-Roe bans or anticipating the enactment of new abortion restrictions in the absence of Roe, voter opinions are more evenly divided. In these states, where the abortion debate is anticipated to unfold in campaigns or state legislatures, an average of 49 percent of adults support the legality of abortion in most or all cases, contrasting with 45 percent who hold the opposing view. Despite this, the collective sentiment falls slightly below the national average, where 54 percent predominantly or entirely endorse legalized abortion compared to 41 percent who predominantly or entirely oppose it.  

The regional distribution of these findings suggests that a nationwide outcry following a potential overturning of Roe might not significantly impact the political landscape in states where immediate abortion restrictions could be implemented. In certain states, such restrictions might reinforce the existing political status quo, generating outrage elsewhere in the nation. However, in states where a battle over new abortion restrictions is likely, especially in the seven predominantly Republican-controlled states with majority voter support for legal abortion, such a fight may entail substantial political risks for conservatives."""
        ),
        html.Div(
            html.Img(src=image_source2, alt='Your Image Alt Text', style={'width': '100%', 'max-width': '800px'}),
            style={'text-align': 'center', 'margin': 'auto'}
        ),
    ],
    style={'margin-left': '80px', 'margin-right': '100px'}  # Adjust the values as needed
)
