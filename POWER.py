

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import os
import flask

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True, assets_folder='assets')
server = app.server  # Expose the server for WSGI

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# File directory for static files
STATIC_PATH = "static"
FILE_NAME = "Staff Qualification Overview Per Department.pptx"
FILE_PATH = os.path.join(STATIC_PATH, FILE_NAME)

# Create a Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Staff Qualification Dashboard"

# Define the layout of the app
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label="Staff Qualification Overview Per Department", children=[
            html.Div([
                html.H3("Download Staff Qualification Overview"),
                html.P("Click the button below to download the PowerPoint slides:"),
                html.A("Download PowerPoint",
                       href=f"/download/{FILE_NAME}",
                       download=FILE_NAME,
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
        ]),
        dcc.Tab(label="Other Features", children=[
            html.Div("Additional tabs can go here.")
        ])
    ])
])

# Serve the file for download
@app.server.route('/download/<filename>')
def download_file(filename):
    if filename == FILE_NAME:
        return flask.send_from_directory(STATIC_PATH, filename, as_attachment=True)
    else:
        return "Error: Invalid file request!", 400

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

