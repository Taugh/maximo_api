# Maximo Parameter-Driven API

This project is a FastAPI-based service that dynamically generates SQL queries for Maximo reports based on user-supplied parameters.

## Features
- Modular input model
- Dynamic query builder
- SQL Server integration
- Flexible output formatting
- Auto-generated documentation
- Interactive frontend for field selection and filtering
- Filter controls retain and display selected values
- Live filter summary for user clarity

## Setup Instructions
...

## Frontend Usage

The web UI allows users to:
- Select required, optional, and multi-entry fields for their report
- Set filter values using dropdowns, text inputs, and textareas
- See all selected fields and filter values in a live summary below the controls
- Generate and review report results before downloading as Excel

### Filter Controls
- Dropdowns support single and multiple selections, and retain chosen values
- Text inputs and textareas keep entered values visible
- Filter summary updates instantly as you change selections

### Report Generation
- Click "Generate Report" to view results in the browser
- Click "Download Excel" to export the current report

All selected fields and filter values are sent to the backend and applied to the report query.