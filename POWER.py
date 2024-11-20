import dash
from dash import dcc, html, Input, Output, State
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
PPT_FILE_NAME = "Staff Qualification Overview Per Department.pptx"
PDF_FILE_NAME = "Faculty EXCO.pptx"
FAS_FILE_NAME = "FAS Preliminary Analysis 2023.pptx"
ACADEMIA_FILE_NAME = "Transformation of Academia.pptx"
PPT_FILE_PATH = os.path.join(STATIC_PATH, PPT_FILE_NAME)
PDF_FILE_PATH = os.path.join(STATIC_PATH, PDF_FILE_NAME)
FAS_FILE_PATH = os.path.join(STATIC_PATH, FAS_FILE_NAME)
ACADEMIA_FILE_PATH = os.path.join(STATIC_PATH, ACADEMIA_FILE_NAME)

# Verify that the static directory and files exist
if not os.path.exists(STATIC_PATH):
    os.makedirs(STATIC_PATH)  # Create the directory if it doesn't exist
    logging.info(f"Static directory '{STATIC_PATH}' created.")

for file_name, file_path in [
    (PPT_FILE_NAME, PPT_FILE_PATH),
    (PDF_FILE_NAME, PDF_FILE_PATH),
    (FAS_FILE_NAME, FAS_FILE_PATH),
    (ACADEMIA_FILE_NAME, ACADEMIA_FILE_PATH),
]:
    if not os.path.exists(file_path):
        logging.warning(f"File '{file_name}' not found in '{STATIC_PATH}'. Ensure the file is placed in the correct location.")

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
                "marginRight": "40px",  # Moved slightly to the right
                "animation": "pulse 3s ease-in-out infinite"  # New animation
            }
        ),
        html.H1("FACULTY OF APPLIED SCIENCE DASHBOARD",
                style={"color": "#333", "fontWeight": "bold", "textAlign": "center"}),
        html.Div(style={"height": "10px", "backgroundColor": "purple"})
    ], style={"padding": "10px"}),

    # Tabs
    dcc.Tabs([
        # Tab 1: Staff Qualification Overview Per Department
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
        ], style={"backgroundColor": "#FFD9D9"}),  # Light red background

        # Tab 2: Faculty Exco
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
        ], style={"backgroundColor": "#FFFACD"}),  # Light yellow background

        # Tab 3: FAS Preliminary Analysis 2023
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
        ], style={"backgroundColor": "#FFE4B5"}),  # Light orange background

        # Tab 4: Transforming the Academia
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
        ], style={"backgroundColor": "#90EE90"}),  # Light green background

        # Tab 5: Chat Bot
        dcc.Tab(label="Chat Bot", children=[
            html.Div([
                html.H3("Send a Message", style={"color": "#333"}),
                html.P("Write your message below and it will be sent to Ngcobo.Nkululeko@yahoo.com."),
                dcc.Textarea(id="message-input", style={"width": "100%", "height": "150px"}),
                html.Button("Send Message", id="send-button", n_clicks=0, style={
                    "marginTop": "10px",
                    "padding": "10px 20px",
                    "backgroundColor": "#007BFF",
                    "color": "white",
                    "borderRadius": "5px",
                    "border": "none"
                }),
                html.Div(id="send-status", style={"marginTop": "20px", "fontWeight": "bold", "color": "green"})
            ])
        ], style={"backgroundColor": "#D6EAF8"})  # Light blue background
    ])
])

# Add CSS animation styles
app.index_string = '''
<!DOCTYPE html>
<html>
<head>
    <title>Faculty Dashboard</title>
    <style>
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    {%app_entry%}
    <footer>
        {%config%}
        {%scripts%}
        {%renderer%}
    </footer>
</body>
</html>
'''


# Serve files for download
@app.server.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(STATIC_PATH, filename)
    if os.path.exists(file_path):
        logging.info(f"Serving file '{filename}' from '{STATIC_PATH}'.")
        return flask.send_from_directory(STATIC_PATH, filename, as_attachment=True)
    else:
        logging.error(f"File '{file_path}' does not exist.")
        return f"Error: File '{filename}' not found!", 404


# Callback for sending messages
@app.callback(
    Output("send-status", "children"),
    [Input("send-button", "n_clicks")],
    [State("message-input", "value")]
)
def send_message(n_clicks, message):
    if n_clicks > 0 and message:
        logging.info(f"Message sent to Ngcobo.Nkululeko@yahoo.com: {message}")
        # In a real application, here you would integrate an email-sending service.
        return "Message sent successfully!"
    elif n_clicks > 0:
        return "Error: Message cannot be empty."
    return ""


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=False, port=8050)
