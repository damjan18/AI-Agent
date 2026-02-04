import os

class FileTool:
    def __init__(self, base_directory: str = "./data"):
        self.name = "file_tool"
        self.description = "Read and Write files"
        self.base_directory = base_directory
        
        if not os.path.exists(base_directory):
            os.makedirs(base_directory)
        
    def read_file(self, filename: str) -> str:
        try:
            filepath = os.path.join(self.base_directory, filename)
            with open(filepath, "r") as f:
                return f.read()
        except FileNotFoundError:
            return f"File not found: {filename}"
        except Exception as e:
            return f"Error reading file: {str(e)}"
        
    def write_file(self, filename: str, content: str) -> str:
        try:
            filepath = os.path.join(self.base_directory, filename)
            with open(filepath, "w") as f:
                f.write(content)
            return f"Successfuly wrote to {filename}"
        except Exception as e:
            return f"Error writing file: {str(e)}"
        
    def list_files(self) -> str:
        try:
            files = os.listdir(self.base_directory)
            if files:
                return "Files:\n" + "\n".join(f"- {f}" for f in files)
            else:
                return "No files found"
        except Exception as e:
            return f"Error listing files: {str(e)}"