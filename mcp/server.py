from mcp.server import Server
from mcp.types import Tool
import os

server = Server("playwright-report-mcp")

def read_test_report() -> str:
    """
    Read Playwright test report and return content
    """
    report_path = os.path.join("..", "reports", "test_report.txt")

    if not os.path.exists(report_path):
        return "Test report not found"

    with open(report_path, "r") as file:
        return file.read()

def get_failed_tests() -> list:
    """
    Extract failed test cases from report
    """
    failed = []
    report_path = os.path.join("..", "reports", "test_report.txt")

    if not os.path.exists(report_path):
        return failed

    with open(report_path, "r") as file:
        for line in file:
            if "FAILED" in line:
                failed.append(line.strip())

    return failed


# ✅ Register tools EXPLICITLY (this is the key fix)
server.add_tool(
    Tool(
        name="read_test_report",
        description="Reads Playwright test report",
        function=read_test_report,
    )
)

server.add_tool(
    Tool(
        name="get_failed_tests",
        description="Returns failed test cases from report",
        function=get_failed_tests,
    )
)

if __name__ == "__main__":
    server.run()