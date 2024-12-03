import dash
from dash import dcc, html, Input, Output, State
import os
import flask
import logging
import zipfile

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the Dash app and Flask server
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server  # Expose the server for deployment

# File directory for static files
STATIC_PATH = "static"
PPT_FILE_NAME = "Staff Qualification Overview Per Department.pptx"
PDF_FILE_NAME = "Faculty EXCO.pptx"
FAS_FILE_NAME = "FAS Preliminary Analysis 2023.pptx"
ACADEMIA_FILE_NAME = "Transformation of Academia.pptx"
PG_SET_FILE_NAME = "PG & SET Data -2021-2023 (23 Oct 2024).pptx"
CORRELATION_FILE_NAME = "Correlation draft presentation (24102024).pptx"
ZIP_FILE_NAME = "All_PowerPoints.zip"

PPT_FILE_PATHS = {
    PPT_FILE_NAME: os.path.join(STATIC_PATH, PPT_FILE_NAME),
    PDF_FILE_NAME: os.path.join(STATIC_PATH, PDF_FILE_NAME),
    FAS_FILE_NAME: os.path.join(STATIC_PATH, FAS_FILE_NAME),
    ACADEMIA_FILE_NAME: os.path.join(STATIC_PATH, ACADEMIA_FILE_NAME),
    PG_SET_FILE_NAME: os.path.join(STATIC_PATH, PG_SET_FILE_NAME),
    CORRELATION_FILE_NAME: os.path.join(STATIC_PATH, CORRELATION_FILE_NAME),
}

ZIP_FILE_PATH = os.path.join(STATIC_PATH, ZIP_FILE_NAME)

# Verify that the static directory and files exist
if not os.path.exists(STATIC_PATH):
    os.makedirs(STATIC_PATH)  # Create the directory if it doesn't exist
    logging.info(f"Static directory '{STATIC_PATH}' created.")

for file_name, file_path in PPT_FILE_PATHS.items():
    if not os.path.exists(file_path):
        logging.warning(f"File '{file_name}' not found in '{STATIC_PATH}'. Ensure the file is placed in the correct location.")

# Create a ZIP file containing all PowerPoint slides
def create_zip_file():
    with zipfile.ZipFile(ZIP_FILE_PATH, 'w') as zipf:
        for file_name, file_path in PPT_FILE_PATHS.items():
            if os.path.exists(file_path):
                zipf.write(file_path, file_name)
    logging.info(f"ZIP file '{ZIP_FILE_NAME}' created at '{ZIP_FILE_PATH}'.")

# Define the layout of the app
app.layout = html.Div([
    # Top section with logo and title
    html.Div([
        html.Img(
            src="/assets/Logo1.png",
            id="animated-logo",
            style={
                "height": "80px",
                "float": "right",
                "marginRight": "40px",
                "animation": "pulse 3s ease-in-out infinite"
            }
        ),
        html.H1("FACULTY OF APPLIED SCIENCE POWERPOINT DASHBOARD",
                style={"color": "#333", "fontWeight": "bold", "textAlign": "center"}),
        html.Div(style={"height": "10px", "backgroundColor": "purple"})
    ], style={"padding": "10px"}),

    # Tabs
    dcc.Tabs([

        # Existing tabs
        dcc.Tab(label="Staff Qualification Overview Per Department", children=[
            html.Div([
                html.H3("Download Staff Qualification Overview PowerPoint Slides", style={"color": "red"}),
                html.P("Click the button below to download the PowerPoint slides:"),
                html.A("Download PowerPoint",
                       href=f"/download/{PPT_FILE_NAME}",
                       download=PPT_FILE_NAME,
                       className="download-link",
                       style={
                           "fontSize": "16px",
                           "padding": "10px 20px",
                           "color": "white",
                           "backgroundColor": "#007BFF",
                           "borderRadius": "5px",
                           "textDecoration": "none"
                       })
            ])
        ], style={"backgroundColor": "#FFD9D9"}),

        dcc.Tab(label="Faculty Exco", children=[
            html.Div([
                html.H3("Download Faculty Exco PowerPoint Slides", style={"color": "Purple"}),
                html.P("Click the button below to download the PowerPoint slide:"),
                html.A("Download PowerPoint",
                       href=f"/download/{PDF_FILE_NAME}",
                       download=PDF_FILE_NAME,
                       className="download-link",
                       style={
                           "fontSize": "16px",
                           "padding": "10px 20px",
                           "color": "white",
                           "backgroundColor": "#28A745",
                           "borderRadius": "5px",
                           "textDecoration": "none"
                       })
            ])
        ], style={"backgroundColor": "#FFFACD"}),

        dcc.Tab(label="FAS Preliminary Analysis 2023", children=[
            html.Div([
                html.H3("Download FAS Preliminary Analysis 2023 PowerPoint Slides", style={"color": "orange"}),
                html.P("Click the button below to download the PowerPoint slides:"),
                html.A("Download PowerPoint",
                       href=f"/download/{FAS_FILE_NAME}",
                       download=FAS_FILE_NAME,
                       className="download-link",
                       style={
                           "fontSize": "16px",
                           "padding": "10px 20px",
                           "color": "white",
                           "backgroundColor": "#FF8C00",
                           "borderRadius": "5px",
                           "textDecoration": "none"
                       })
            ])
        ], style={"backgroundColor": "#FFE4B5"}),

        dcc.Tab(label="Transforming the Academia", children=[
            html.Div([
                html.H3("Download Transforming the Academia PowerPoint Slides", style={"color": "green"}),
                html.P("Click the button below to download the PowerPoint slides:"),
                html.A("Download PowerPoint",
                       href=f"/download/{ACADEMIA_FILE_NAME}",
                       download=ACADEMIA_FILE_NAME,
                       className="download-link",
                       style={
                           "fontSize": "16px",
                           "padding": "10px 20px",
                           "color": "white",
                           "backgroundColor": "#006400",
                           "borderRadius": "5px",
                           "textDecoration": "none"
                       })
            ])
        ], style={"backgroundColor": "#90EE90"}),

        # New tabs
        dcc.Tab(label="PG & SET Data - 2021-2023 (23 Oct 2024)", children=[
            html.Div([
                html.H3("Download PG & SET Data PowerPoint Slides", style={"color": "blue"}),
                html.P("Click the button below to download the PowerPoint slides:"),
                html.A("Download PowerPoint",
                       href=f"/download/{PG_SET_FILE_NAME}",
                       download=PG_SET_FILE_NAME,
                       className="download-link",
                       style={
                           "fontSize": "16px",
                           "padding": "10px 20px",
                           "color": "white",
                           "backgroundColor": "#0000FF",
                           "borderRadius": "5px",
                           "textDecoration": "none"
                       })
            ])
        ], style={"backgroundColor": "#ADD8E6"}),  # Light blue background

        dcc.Tab(label="Correlation Draft Presentation (24 Oct 2024)", children=[
            html.Div([
                html.H3("Download Correlation Draft Presentation", style={"color": "darkmagenta"}),
                html.P("Click the button below to download the PowerPoint slides:"),
                html.A("Download PowerPoint",
                       href=f"/download/{CORRELATION_FILE_NAME}",
                       download=CORRELATION_FILE_NAME,
                       className="download-link",
                       style={
                           "fontSize": "16px",
                           "padding": "10px 20px",
                           "color": "white",
                           "backgroundColor": "darkmagenta",
                           "borderRadius": "5px",
                           "textDecoration": "none"
                       })
            ])
        ], style={"backgroundColor": "#FFB6C1"}),  # Light pink background

        dcc.Tab(label="FAS Dashboards Links", children=[
            html.Div([
                html.H3("Access FAS Dashboards", style={"color": "navy"}),
                html.Ul([
                    html.Li(html.A("FAS PowerHEDA Dashboard",
                                   href="https://powerheda.dut.ac.za/PowerHEDA/Dashboard.aspx",
                                   target="_blank",
                                   style={"color": "blue"})),
                    html.Li(html.A("FAS Research Dashboard",
                                   href="https://dut-2024-research-8.onrender.com/",
                                   target="_blank",
                                   style={"color": "blue"}))
                ])
            ])
        ], style={"backgroundColor": "#F0F8FF"}),  # Alice blue background

        dcc.Tab(label="Download All PowerPoint Slides", children=[
            html.Div([
                html.H3("Download All PowerPoint Slides as a ZIP File", style={"color": "maroon"}),
                html.P("Click the button below to download all slides:"),
                html.A("Download All Slides",
                       href=f"/download/{ZIP_FILE_NAME}",
                       download=ZIP_FILE_NAME,
                       className="download-link",
                       style={
                           "fontSize": "16px",
                           "padding": "10px 20px",
                           "color": "white",
                           "backgroundColor": "maroon",
                           "borderRadius": "5px",
                           "textDecoration": "none"
                       })
            ])
        ], style={"backgroundColor": "#FFEFD5"}),  # Papaya whip background
    ])
])

# Serve files for download
@app.server.route('/download/<filename>')
def download_file(filename):
    if filename == ZIP_FILE_NAME:
        create_zip_file()  # Ensure ZIP file is created before download
    file_path = os.path.join(STATIC_PATH, filename)
    if os.path.exists(file_path):
        logging.info(f"Serving file '{filename}' from '{STATIC_PATH}'.")
        return flask.send_from_directory(STATIC_PATH, filename, as_attachment=True)
    else:
        logging.error(f"File '{file_path}' does not exist.")
        return f"Error: File '{filename}' not found!", 404

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=False, port=8050)
