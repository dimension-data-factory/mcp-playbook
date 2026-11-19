import os
from mcp.server import MCPServer

mcp = MCPServer("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host=os.environ.get("HOST", "0.0.0.0"),  # 监听所有网卡，以便外部访问
        port=int(os.environ.get("PORT", "8000")),
    )


