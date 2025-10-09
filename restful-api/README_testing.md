# Flask API Testing Guide

## Files Overview

- `task_04_flask.py` - Main Flask API server
- `test_task_04_flask.py` - Comprehensive automated test suite
- `run_tests.py` - Test runner that starts server and runs tests
- `manual_test.sh` - Manual testing with curl commands

## Quick Start

### 1. Automated Testing (Recommended)

```bash
# Install requests if not installed
pip install requests

# Run all tests automatically
python3 run_tests.py
```

This will:
- Start the Flask server automatically
- Run comprehensive tests
- Stop the server
- Show test results

### 2. Manual Testing

Start the Flask server:
```bash
python3 task_04_flask.py
```

In another terminal, run tests:
```bash
# Using the automated test suite
python3 test_task_04_flask.py

# OR using curl commands
bash manual_test.sh

# OR individual curl tests
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/status
curl http://127.0.0.1:5000/data
curl http://127.0.0.1:5000/user/jane
curl -X POST -H "Content-Type: application/json" \
     -d '{"username":"bob","name":"Bob","age":30,"city":"NY"}' \
     http://127.0.0.1:5000/add_user
```

## API Endpoints

| Method | Endpoint | Description | Expected Response |
|--------|----------|-------------|-------------------|
| GET | `/` | Welcome message | HTML: Welcome message |
| GET | `/status` | Health check | Text: "OK" |
| GET | `/data` | List all users | JSON: Array of user objects |
| GET | `/user/<username>` | Get specific user | JSON: User object or 404 error |
| POST | `/add_user` | Add new user | JSON: Success message + user data |

## Test Cases Covered

✅ **Positive Tests:**
- Home page responds with welcome message
- Status endpoint returns OK
- Data endpoint returns user list
- Get existing user returns user data
- Add valid user succeeds

✅ **Negative Tests:**
- Get non-existent user returns 404
- Add user without username returns 400
- Add user without JSON data returns 400

✅ **Edge Cases:**
- Server connectivity check
- JSON parsing validation
- Required field validation

## Sample Test Output

```
🚀 Starting Flask API Tests
Base URL: http://127.0.0.1:5000
✅ Flask server is running
==================================================
[PASS] ✅ Home endpoint: Passed
[PASS] ✅ Status endpoint: Passed
[PASS] ✅ Data endpoint: Passed
[PASS] ✅ Get existing user: Passed
[PASS] ✅ Get non-existent user: Passed
[PASS] ✅ Add valid user: Passed
[PASS] ✅ Add user without username: Passed
[PASS] ✅ Add user without JSON: Passed
[PASS] ✅ Get previously added user: Passed
==================================================
📊 Test Summary:
   ✅ Passed: 9
   ❌ Failed: 0
   📈 Total:  9
🎉 All tests passed!
```

## Dependencies

- `flask` - Web framework
- `requests` - HTTP client for tests (only needed for testing)

Install dependencies:
```bash
pip install flask requests
```

## Troubleshooting

**"Connection refused" error:**
- Make sure Flask server is running: `python3 task_04_flask.py`
- Check if port 5000 is available
- Wait a few seconds after starting server before running tests

**"Module not found" error:**
- Install missing dependencies: `pip install flask requests`
- Ensure you're in the correct directory

**Tests failing:**
- Check Flask server logs for errors
- Verify server is accessible: `curl http://127.0.0.1:5000/status`
- Run individual tests to isolate issues
