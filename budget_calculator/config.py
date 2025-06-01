"""Configuration settings for the Budget Calculator application."""

# UI Constants
WINDOW_SIZE = "600x600"
BACKGROUND_COLOR = "#FFFFFF"
WINDOW_TITLE = "Budget Calculator"
TITLE_FONT = ("helvetica", 22, "bold")
BOLD_FONT = ("Segoe UI", 9, "bold")

# Chart Constants
CHART_DPI = 300
CHART_SIZE = (1, 1)
PIE_CHART_SETTINGS = {
    "radius": 1,
    "shadow": True,
    "autopct": "%1.2f%%",
    "textprops": {"fontsize": 2.8}
}

# Categories
INCOME_CATEGORIES = ["Salary", "Side Hustles", "Gifts", "Passive"]
EXPENSE_CATEGORIES = ["Rent", "Transportation", "Food", "Investments", "Entertainment", "Saving", "Other"]

# Data Storage
DEFAULT_DATA = {
    "income": {
        "salary": 100.0,
        "gifts": 100.0,
        "side hustles": 100.0,
        "passive": 100.0
    },
    "expenses": {
        "rent": 100.0,
        "transport": 100.0,
        "food": 100.0,
        "investments": 100.0,
        "savings": 100.0,
        "entertainment": 100.0,
        "other": 100.0
    }
}

# File paths
DATA_FILE = "data.json" 