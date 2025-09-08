from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Apple Inc. is an American multinational corporation and technology company headquartered in Cupertino, California, in Silicon Valley. 
It is best known for its consumer electronics, software, and services. Founded in 1976 as Apple Computer Company by Steve Jobs, Steve Wozniak and Ronald Wayne, 
the company was incorporated by Jobs and Wozniak as Apple Computer, Inc. the following year. It was renamed Apple Inc. in 2007 as the company had expanded its focus from computers to consumer electronics. 
Apple is the largest technology company by revenue, with US$391.04 billion in the 2024 fiscal year.

The company was founded to produce and market Wozniak's Apple I personal computer. Its second computer, the Apple II, 
became a best seller as one of the first mass-produced microcomputers. Apple introduced the Lisa in 1983 and the Macintosh in 1984, 
as some of the first computers to use a graphical user interface and a mouse. By 1985, internal company problems led to Jobs leaving to 
form NeXT, and Wozniak withdrawing to other ventures; John Sculley served as long-time CEO for over a decade. In the 1990s, Apple lost considerable market share in the personal computer industry to the lower-priced Wintel duopoly of the 
Microsoft Windows operating system on Intel-powered PC clones. In 1997, Apple was weeks away from bankruptcy. 
To resolve its failed operating system strategy, it bought NeXT, effectively bringing Jobs back to the company, who guided Apple back to profitability over the next decade with the introductions of the iMac, iPod, iPhone, 
and iPad devices to critical acclaim as well as the iTunes Store, launching the "Think different" advertising campaign, and opening the Apple Store retail chain. 
These moves elevated Apple to consistently be one of the world's most valuable brands since about 2010. Jobs resigned in 2011 for health reasons, and died two months later; he was succeeded as CEO by Tim Cook.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,
)

result = splitter.split_text(text)

print(result[0])