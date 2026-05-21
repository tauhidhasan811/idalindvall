# Description

This repository contains a FastAPI-based web application designed for AI-driven financial analysis and budgeting. It integrates multiple budget methods and income-related endpoints, leveraging Anthropic AI chat models for processing user input. The project includes detailed Pydantic schemas for data validation, Excel report generation with OpenPyXL, and cloud media management via Cloudinary. The code supports session management, prompt generation, and structured financial data handling to automate budget calculations and reporting. Configuration files manage dependencies, Python version, and environment variables to ensure consistent setup and deployment.

# Run Instructions

1. Clone the repository:  
   `git clone <repo-url>`

2. Create a virtual environment:  
   `py -3.13 -m venv venv`

3. Activate the virtual environment:  
   - On Windows: `venv\Scripts\activate`  
   - On Unix/Mac: `source venv/bin/activate`

4. Install dependencies:  
   `pip install -r requirements.txt`

5. Run important files:  
   - `python main.py`  
   - `python test.py`

# Folder Structure

```
idalindvall
|-- .python-version
|-- main.py
|-- pyproject.toml
|-- README.md
|-- test.py
|-- uv.lock
|-- api
|   |-- route
|   |   |-- budget_method_route.py
|   |   |-- income_route.py
|   |-- schema
|       |-- budget_method_schema.py
|       |-- chat_schema.py
|-- src
    |-- budget_method_output_parameters.py
    |-- cellmaper.py
    |-- hyperparameter.py
    |-- config
    |   |-- config_anthropic.py
    |   |-- config_cloudinary.py
    |-- core
    |   |-- chat_with_anthropic.py
    |   |-- create_excel.py
    |   |-- data_processor.py
    |   |-- generate_prompt.py
    |   |-- session.py
    |-- service
        |-- budget_method_service.py
        |-- income_service.py
```

# File Descriptions

**.python-version**  
Specifies Python version 3.13 for consistent environment setup.

**main.py**  
FastAPI app initializing CORS middleware and registering API routers for income and budget methods.

**pyproject.toml**  
Project metadata and dependency declarations including FastAPI, LangChain, Cloudinary, and OpenPyXL.

**README.md**  
Documentation outlining project overview, setup, and usage instructions.

**test.py**  
Prepares nested financial data dictionaries and integrates Excel export functionality.

**uv.lock**  
Dependency lock file ensuring reproducible installs with pinned package versions.

**api/route/budget_method_route.py**  
Defines POST endpoint for budget method processing integrating AI chat model and Cloudinary uploads.

**api/route/income_route.py**  
Defines POST endpoint handling financial chat sessions using AI chat models for analysis.

**api/schema/budget_method_schema.py**  
Pydantic models validating budget method financial category inputs.

**api/schema/chat_schema.py**  
Pydantic models for chat data validation, structuring chat item histories.

**src/budget_method_output_parameters.py**  
Template defining budget parameter categories and allocation tracking for the Command Center method.

**src/cellmaper.py**  
Maps financial data fields to Excel cell references based on budgeting method.

**src/hyperparameter.py**  
Defines financial categories and data collection order for budget input.

**src/config/config_anthropic.py**  
Configures and initializes Anthropic AI chat model with environment variables.

**src/config/config_cloudinary.py**  
Loads Cloudinary credentials and manages file uploads to the Cloudinary service.

**src/core/chat_with_anthropic.py**  
Controller class to send prompts and retrieve responses from the Anthropic AI model.

**src/core/create_excel.py**  
Manages updating Excel budget templates using mapped data and OpenPyXL.

**src/core/data_processor.py**  
Processes chat histories and cleans AI textual responses for JSON parsing.

**src/core/generate_prompt.py**  
Generates structured prompts from financial data categories for language model input.

**src/core/session.py**  
Handles session persistence with JSON file storage and unique session ID generation.

**src/service/budget_method_service.py**  
Processes budget method inputs via AI chat model, generates Excel reports, and uploads results to Cloudinary.

**src/service/income_service.py**  
Analyzes chat history to generate financial analysis prompts and clean AI responses.