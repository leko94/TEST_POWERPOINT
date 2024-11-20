

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import os
import flask
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the Dash app and Flask server
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server  # Expose the server for deployment

# File directory for static files
STATIC_PATH = "static"
FILE_NAME = "Staff Qualification Overview Per Department.pptx"
FILE_PATH = os.path.join(STATIC_PATH, FILE_NAME)

# Verify that the static directory and file exist
if not os.path.exists(STATIC_PATH):
    os.makedirs(STATIC_PATH)  # Create the directory if it doesn't exist
    logging.info(f"Static directory '{STATIC_PATH}' created.")

if not os.path.exists(FILE_PATH):
    logging.warning(f"File '{FILE_NAME}' not found in '{STATIC_PATH}'. Ensure the file is placed in the correct location.")

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
        if os.path.exists(FILE_PATH):
            logging.info(f"Serving file '{FILE_NAME}' from '{STATIC_PATH}'.")
            return flask.send_from_directory(STATIC_PATH, filename, as_attachment=True)
        else:
            logging.error(f"File '{FILE_PATH}' does not exist.")
            return f"Error: File '{FILE_NAME}' not found!", 404
    else:
        logging.error(f"Invalid file request: {filename}")
        return "Error: Invalid file request!", 400


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=False, port=8050)  # Set debug=False for production
