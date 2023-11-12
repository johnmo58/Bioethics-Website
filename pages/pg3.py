import dash
from dash import dcc, html
import plotly.express as px

# Register the page with a specific path
dash.register_page(__name__, name='Philosophy Summary')

text_content = """
In her 1971 essay “A Defense of Abortion,” Judith Thomson presents a compelling argument suggesting that abortion can have moral justification, even while acknowledging the inherent right to life of the fetus. Specifically, she argues that even if a fetus possesses an inherent right to life, abortion may be morally acceptable. Mary Ann Warren, in her essay “The Moral and Legal Status of Abortion,” argues that the analogy oversimplifies the complexities of pregnancy, emphasizing its focus on specific, extreme cases. Warren advocates for a more comprehensive analysis that considers diverse circumstances, intentions, and responsibilities. Thomson responds by stressing the illustrative nature of her analogy, applicable to a range of scenarios. She addresses Warren's concerns by highlighting the broader principles of bodily autonomy and the nuanced considerations of intentionality in assuming the risks of pregnancy, demonstrating the universality of her ethical framework.

Now that users have a better understanding of this topic, this website aims to prompt them to explore two contrasting moral philosophies and draw their own conclusions on the controversial topic under discussion. Rather than advocating a specific viewpoint, the goal is to encourage critical thinking and independent reflection. By delving into the intricacies of these philosophical perspectives, users are invited to navigate the complexities of the arguments presented and formulate their own informed opinions. """

layout = html.Div(
    [
        dcc.Markdown(text_content, style={'line-height': '2'}),
    ],
    style={'margin-left': '80px', 'margin-right': '100px'}  # Adjust the values as needed
)
