import httpx

class WebSearchTool:
    def __init__(self):
        self.name = "web search"
        self.description = "Search the web information"
        
    async def search(self, query: str) -> str:
        try:
            # Using DuckDuckGo instant answer
            url = "https://api.duckduckgo.com/"
            params = {
                "q": query,
                "format": "json",
                "no_html": 1
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                data = response.json()
                
            results = []
            
            if data.get("Abstract"):
                results.append(f"Summary: {data['Abstract']}")
                
            if data.get("RelatedTopics"):
                for topic in data["RelatedTopics"][:3]:
                    if isinstance(topic, dict) and topic.get("Text"):
                        results.append(f"- {topic['Text']}")
                        
            if results:
                return "\n".join(results)
            else:
                return f"No results found for: {query}"
        
        except Exception as e:
            return f"Search error: {str(e)}"
                
            