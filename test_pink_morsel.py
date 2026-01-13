from dash_visualiser import app

"""
AI-assisted code note:
  This compatibility section was generated with assistance from ChatGPT (OpenAI).

Citation:
  OpenAI. (2026). ChatGPT (GPT-5.2) [Large language model]. https://chat.openai.com/ (accessed 13 Jan 2026).
"""
try:
    from dash.testing.composite import DashComposite
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait

    if not hasattr(DashComposite, "get_graph_figure"):
        def get_graph_figure(self, graph_id, timeout=10):
            # wait until plotly has actually created the .js-plotly-plot div
            WebDriverWait(self.driver, timeout).until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, f"#{graph_id} .js-plotly-plot")) > 0
            )

            # return a dict that looks like a Plotly figure: {"data": ..., "layout": ...}
            return self.driver.execute_script(
                """
                const id = arguments[0];
                const gd = document.querySelector(`#${id} .js-plotly-plot`);
                if (!gd) return null;
                return {data: gd.data, layout: gd.layout};
                """,
                graph_id
            )

        DashComposite.get_graph_figure = get_graph_figure
except Exception:
    # If dash.testing/selenium isn't installed in runtime usage, ignore.
    pass



# Header exists 
def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text.strip() == "Pink Morsel Sales"

# Visualisation exists 
def test_visualisation_exists(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#pink-morsel-sales-linechart")
    assert graph is not None

# Region picker exists
def test_regions_present_in_graph(dash_duo):
    dash_duo.start_server(app)

    # Wait until plotly graph is rendered
    dash_duo.wait_for_element("#pink-morsel-sales-linechart", timeout=10)

    # Grab figure from the Dash component via browser
    graph_component = dash_duo.find_element("#pink-morsel-sales-linechart")
    assert graph_component is not None

    # Use Dash's helper to access the props of the React component
    figure = dash_duo.get_graph_figure("pink-morsel-sales-linechart")  # dash_duo has a method to get the graph's figure through the Dash renderer
    assert figure is not None
    assert "data" in figure

    # Expect minimumm of 2 region traces
    assert len(figure["data"]) >= 2