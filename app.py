import sys
import paperscraper


if len(sys.argv) < 2:
    print("Usage: python example.py <search_query>")
    sys.exit(1)

search_query = sys.argv[1]  

papers = paperscraper.search_papers(search_query,
                                    limit=10,
                                    pdir='downloaded-papers')

for paper in papers:
    print(paper.title)
