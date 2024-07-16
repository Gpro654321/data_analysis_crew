from crewai import Agent


data_cleaning_agent = Agent(
    role = 'Data Cleaner',
    goal = 'Read the data from the specified {datafile}, report rows that have missing values and report outliers in each column',
    backstory = """You are expert researcher. You have a knack for cleaning data"""
    tools = [],
    verbose = True,
    allow_delegation = True

)

data_summary_agent = Agent(
    role = 'Data Summarizer',
    goal = 'Read the data from the specified {datafile}, provide a summary of each column',
    backstory = """You are a expert statistician. You provide summary of the given data.""",
    tools = [],
    verbose = True,
    allow_delegation = True
)

data_insights_agent = Agent(
    role = 'Data Insight creator',
    goal = 'Read the data from the specified {datafile} and generate insights within columns and across columns',
    backstory = """You are expert data analyst. You provide excellent insights from the given data which has led to meaningful actions""",
    tools = [],
    verbose = True,
    allow_delegation = True

)

data_visualization_agent = Agent(
    role = 'Data Visualization creator',
    goal = 'Read the data from the specified {datafile} and generate suitable charts to visualize the insights',
    backstory = """You are a expert data analyst. You are extremely creative in making charts that are represent the insights""",
    tools = [],
    verbose = True,
    allow_delegation = True
)