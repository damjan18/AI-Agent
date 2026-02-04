import asyncio
from tools.file_tool import FileTool
from tools.web_search import WebSearchTool

print("=== FILE TOOL ===")
file_tool = FileTool()

result = file_tool.write_file("test.txt", "Helloooo")
print(result)

content = file_tool.read_file("test.txt")
print(f"Content: {content}")

files = file_tool.list_files()
print(files)

print("\n=== WEB SEARCH===")
async def test_search():
    search_tool = WebSearchTool()
    result = await search_tool.search("Python programming language")
    print(result)
    
asyncio.run(test_search())