
import os

chart_files = [
    "income_trends_by_state.png",
    "income_comparison_2024.png",
    "income_heatmap.png",
    "marriage_trends_by_gender.png",
    "marriage_comparison_by_state_2024.png",
    "marriage_rate_heatmap.png",
    "schools_by_state_2024.png",
    "schools_by_stage_2024.png",
    "schools_trends_by_stage.png"
]

for file in chart_files:
    if os.path.exists(file):
        print("FOUND:", file)
    else:
        print("MISSING:", file)
