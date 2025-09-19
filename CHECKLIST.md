# ✅ Maximo API Development Checklist

## 📁 Project Setup

- [x] Create structured project folder in VS Code
- [x] Include subfolders: `app`, `models`, `services`, `db`, `utils`, `tests`
- [x] Add `main.py`, `config.py`, `.env`, `requirements.txt`, `README.md`

## 🚀 FastAPI App Initialization

- [x] Define root endpoint `/` to confirm server is running
- [x] Enable Swagger UI at `/docs` for interactive testing

## 🧩 Input Model Design

- [x] Use `Pydantic` to define `WorkOrderInput` model
- [x] Categorize fields using Excel mapping: required, optional, multi-entry
- [x] Replace `.dict()` with `.model_dump()` for Pydantic v2 compatibility
- [x] Set sensible defaults for required fields where applicable
- [x] Frontend filter controls retain and display selected values
- [x] Live filter summary for user clarity

## 🔌 Endpoint Implementation

- [x] Create `POST /workorder` endpoint
- [x] Validate input against `WorkOrderInput`
- [x] Return structured confirmation response

## 🧠 Field Behavior Logic

- [x] Support multi-entry fields (`List[str]`, `List[datetime]`)
- [x] Allow optional fields to default to `None`
- [x] Enforce required fields with FastAPI validation

## 🛠️ Query Builder

- [ ] Build dynamic SQL generator based on input parameters
- [ ] Handle `IN (...)` logic for multi-entry fields
- [ ] Apply filters and date ranges conditionally

## 🗃️ Database Integration

- [ ] Use `.env` for secure SQL Server credentials
- [ ] Implement `get_connection()` in `connection.py`
- [ ] Execute queries and return results in JSON format

## 📊 Output Customization

- [ ] Allow user to specify which fields to include in output
- [ ] Format response consistently for dashboard or reporting use

## 🧪 Testing & Validation

- [ ] Add unit tests in `tests/test_api.py`
- [ ] Validate edge cases and error handling (422, missing fields)

## 📚 Documentation & Governance

- [x] Document endpoints, models, and query logic
- [x] Update README for new frontend features
- [x] Include versioning and change logs
- [x] Align with SQL query review standards (headers, assumptions, filters)
