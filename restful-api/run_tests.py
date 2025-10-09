#!/usr/bin/env python3
"""
Simple test runner for Flask API.

This script starts the Flask server and runs tests automatically.
"""

import subprocess
import time
import sys
from pathlib import Path


def run_tests():
    """Run Flask server and tests."""
    flask_process = None

    try:
        # Start Flask server in background
        print("🚀 Starting Flask server...")
        flask_process = subprocess.Popen(
            [sys.executable, "task_04_flask.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=Path(__file__).parent
        )

        # Wait for server to start
        print("⏳ Waiting for server to start...")
        time.sleep(3)

        # Check if server is still running
        if flask_process.poll() is not None:
            stdout, stderr = flask_process.communicate()
            print("❌ Flask server failed to start:")
            print(f"STDOUT: {stdout.decode()}")
            print(f"STDERR: {stderr.decode()}")
            return 1

        print("✅ Flask server started successfully")

        # Run tests
        print("🧪 Running tests...")
        test_result = subprocess.run(
            [sys.executable, "test_task_04_flask.py"],
            cwd=Path(__file__).parent
        )

        return test_result.returncode

    except KeyboardInterrupt:
        print("\n⚠️  Test interrupted by user")
        return 1

    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1

    finally:
        # Clean up Flask server
        if flask_process and flask_process.poll() is None:
            print("🛑 Stopping Flask server...")
            flask_process.terminate()
            try:
                flask_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                flask_process.kill()
                flask_process.wait()
            print("✅ Flask server stopped")


def main():
    """Main function."""
    print("=" * 60)
    print("🔧 Flask API Test Runner")
    print("=" * 60)

    # Check if required files exist
    required_files = ["task_04_flask.py", "test_task_04_flask.py"]
    for file in required_files:
        if not Path(file).exists():
            print(f"❌ Required file not found: {file}")
            return 1

    exit_code = run_tests()

    if exit_code == 0:
        print("\n🎉 All tests completed successfully!")
    else:
        print(f"\n💥 Tests failed with exit code: {exit_code}")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
