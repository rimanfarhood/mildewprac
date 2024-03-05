import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_visualization import page_visualization_body
from app_pages.page_MildewDetector import page_MildewDetector_body
from app_pages.page_hypothesis import page_project_hypothesis_body
from app_pages.page_mlPerformance import page_ml_performance_metrics

app = MultiPage(app_name="Powdery Mildew Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Leaves Visualizer", page_visualization_body)
app.add_page("Powdery Mildew Detection", page_MildewDetector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)

app.run()