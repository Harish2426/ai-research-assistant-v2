import requests

from app.config import SERPER_API_KEY


class SearchTool:

    def search(self, query):

        url = "https://google.serper.dev/search"

        headers = {
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        }

        payload = {
            "q": query
        }

        try:

            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            results = []

            for item in data.get("organic", [])[:5]:

                results.append(
                    {
                        "title": item.get("title"),
                        "link": item.get("link"),
                        "snippet": item.get("snippet")
                    }
                )

            return results

        except Exception as e:

            return {
                "error": str(e)
            }


search_tool = SearchTool()