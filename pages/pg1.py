import dash
from dash import dcc, html
import plotly.express as px

# Register the page with a specific path
dash.register_page(__name__, name='Historical Background', path='/')

text_content = """
In the 1973 Roe v. Wade ruling, the Supreme Court affirmed that the constitutional right to liberty, encompassing personal privacy, includes the freedom to make decisions regarding pregnancy. This landmark decision elevated reproductive decision-making to the level of other fundamental rights, such as freedom of speech and religion, subjecting it to the highest level of constitutional protection known as "strict scrutiny."

The Court mandated that the state must provide a compelling interest to justify any intrusion on the right to access abortion. Before the point of viability, no such compelling interest was deemed sufficient to justify a ban on abortion. Post-viability, the state could restrict abortion or take measures to safeguard the fetus's interest. However, even after viability, abortion must be allowed to preserve the life and health of the patient.

Roe aligned with earlier Supreme Court decisions acknowledging a right to privacy safeguarding intimate and personal choices, including those related to child-rearing, marriage, procreation, and contraception, shielding them from governmental interference. By securing the right to make decisions during pregnancy, Roe played a pivotal role in advancing gender equality across educational, economic, and political domains.

In 1973, the majority of states prohibited abortion except in specific circumstances. Criminalized abortion contributed to numerous fatalities among individuals lacking access to safe, legal procedures. Roe rendered these abortion bans unconstitutional, resulting in legal, more accessible, and safer abortion options for many individuals nationwide. Despite its monumental legal impact, Roe did not guarantee universal access, and individuals facing economic challenges, people of color, youth, and others continued to encounter barriers to abortion care.

The Court divided the duration of pregnancy into three trimesters. In the initial trimester, the woman had full discretion to decide on terminating the pregnancy. Following the first trimester, the state could intervene to "regulate procedure." In the second trimester, the state could impose regulations (though not outright bans) on abortions to safeguard the mother's health. Upon entering the third trimester when the fetus became viable, the state gained the authority to regulate or prohibit abortions in the interest of potential life, except when essential to preserve the life or health of the mother.
"""

# Image source
image_source = 'https://divinity.uchicago.edu/sites/default/files/styles/sightings_article_featured_image/public/2022-07/jane2.v1.jpg?itok=r3IPoIXp'

df = px.data.gapminder()

layout = html.Div(
    [
        dcc.Markdown(text_content, style={'line-height': '2'}),
        html.Div(
            html.Img(src=image_source, alt='Judith Thomson', style={'width': '100%', 'max-width': '500px'}),
            style={'text-align': 'center', 'margin': 'auto'}
        ),
    ],
    style={'margin-left': '80px', 'margin-right': '100px'}  # Adjust the values as needed
)
