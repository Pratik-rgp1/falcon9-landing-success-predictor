#Import required libraries and load data

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load SpaceX launch data
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Define min and max payload values for RangeSlider
min_payload = spacex_df['Payload Mass (kg)'].min()
max_payload = spacex_df['Payload Mass (kg)'].max()


#  Initialize Dash app

app = dash.Dash(__name__)


#Create app layout with dropdown and slider inputs, plus output graphs

app.layout = html.Div([
    # Launch Site Dropdown for selecting site or all sites
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            # Add all launch site options here dynamically or manually
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
        ],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),
    
    # Payload Range Slider to select range of payload masses (kg)
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        value=[min_payload, max_payload],  # Using dataset min and max
        marks={0: '0', 10000: '10000'}
    ),
    
    # Pie chart showing launch success counts
    dcc.Graph(id='success-pie-chart'),
    
    # Scatter chart showing payload vs. launch success, colored by booster version
    dcc.Graph(id='success-payload-scatter-chart')
])


# Callback for updating pie chart based on dropdown selection

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(selected_site):
    """
    Updates pie chart to show:
    - total successful launches for all sites if 'ALL' selected
    - success vs failure counts for the selected launch site otherwise
    """
    if selected_site == 'ALL':
        # Use entire dataset to create pie chart for all sites
        fig = px.pie(
            spacex_df.groupby('Launch Site')['class'].sum().reset_index(),
            values='class',
            names='Launch Site',
            title='Total Successful Launches for All Sites'
        )
    else:
        # Filter data for the selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        # Create pie chart for success vs failure counts at this site
        counts = filtered_df['class'].value_counts().reset_index()
        counts.columns = ['class', 'count']
        fig = px.pie(
            counts,
            values='count',
            names='class',
            title=f'Success vs Failure for site {selected_site}'
        )
    return fig


#Callback for updating scatter plot based on dropdown and slider selections

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id='payload-slider', component_property='value')
    ]
)
def update_scatter_plot(selected_site, payload_range):
    """
    Updates scatter plot to show payload mass vs launch success, colored by booster version.
    Filters data by selected site and payload range.
    """
    low, high = payload_range
    if selected_site == 'ALL':
        # Filter dataset by payload range only
        filtered_df = spacex_df[
            (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
        ]
    else:
        # Filter dataset by site and payload range
        filtered_df = spacex_df[
            (spacex_df['Launch Site'] == selected_site) & 
            (spacex_df['Payload Mass (kg)'] >= low) & 
            (spacex_df['Payload Mass (kg)'] <= high)
        ]
    # Create scatter plot with booster version color coding
    fig = px.scatter(
        filtered_df, 
        x='Payload Mass (kg)', 
        y='class', 
        color='Booster Version Category',
        title='Payload vs Launch Outcome'
    )
    return fig

# ----------------------------------------
# Run the Dash app
# ----------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
