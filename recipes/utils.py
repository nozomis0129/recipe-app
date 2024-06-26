from .models import Recipe
from io import BytesIO
import base64
import matplotlib.pyplot as plt


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph


def get_chart(chart_type, data, **kwargs):
    # switch plot backend to AGG (Anti-Grain Geometry) - to write to file
    # AGG is preferred solution to write PNG files
    plt.switch_backend("AGG")

    # specify figure size
    fig = plt.figure(figsize=(6, 3))

    # select chart_type based on user input from the form
    if chart_type == "#1":
        # plot bar chart between date on x-axis and quantity on y-axis
        plt.bar(data["name"], data["cooking_time"])

    elif chart_type == "#2":
        # generate pie chart based on the price.
        # The book titles are sent from the view as labels
        labels = kwargs.get("labels")
        plt.pie(data["cooking_time"], labels=labels)

    else:
        print("unknown chart type")

    # specify layout details
    plt.tight_layout()

    # render the graph to file
    chart = get_graph()
    return chart
