import dash
from dash import dcc, html
import plotly.express as px

# Register the page with a specific path
dash.register_page(__name__, name='Sources')

text_content = """
Works Cited:

Cohn, Nate. "Do Americans Support Abortion Rights? Depends on the State." The New York Times, 4 May 2022, www.nytimes.com/2022/05/04/upshot/polling-abortion-states.html. Accessed 10 Nov. 2023.

"Public Opinion on Abortion." Pew Research Center, 17 May 2022, www.pewresearch.org/religion/fact-sheet/public-opinion-on-abortion/. Accessed 10 Nov. 2023.

"Roe v. Wade." Center of Reproductive Rights, reproductiverights.org/roe-v-wade/. Accessed 10 Nov. 2023.

"Roe v. Wade (1973)." Legal Information Institute, Cornell University, www.law.cornell.edu/wex/roe_v_wade_(1973)#:~:text=During%20the%20first%20trimester%2C%20the,interests%20of%20the%20mother's%20health. Accessed 10 Nov. 2023.

Thomson, Judith Jarvis. "A Defense of Abortion." Judith Jarvis Thomson: A Defense of Abortion, CU Boulder, 1971, spot.colorado.edu/~heathwoo/Phil160,Fall02/thomson.htm. Accessed 10 Nov. 2023.

"Thomson's Violinist and The Importance of Risk." Manuscript.

Warren, Mary Anne. "ON THE MORAL AND LEGAL STATUS of ABORTION." The Monist, vol. 57, no. 1, 1973, pp. 43-61. JSTOR, www.jstor.org/stable/27902294. Accessed 10 Nov. 2023.
"""

layout = html.Div(
    [
        dcc.Markdown(text_content, style={'line-height': '2'}),
    ],
    style={'margin-left': '80px', 'margin-right': '100px'}  # Adjust the values as needed
)
