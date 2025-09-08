# Text Splitter in LangChain
This directory contains implementations of various text splitting strategies used in LangChain. Text splitters are essential for breaking down large documents into smaller, manageable chunks that can be processed more effectively by language models.

## Available Text Splitters
- **CharacterTextSplitter**: Splits text based on character count, ensuring that each chunk does not exceed a specified number of characters.
- **RecursiveCharacterTextSplitter**: A more advanced version of the CharacterTextSplitter that attempts to split text at natural boundaries (like paragraphs or sentences) before falling back to character count.
- **MarkdownTextSplitter**: Specifically designed to handle Markdown formatted text, preserving the structure while splitting.
- **TokenTextSplitter**: Splits text based on token count, which is particularly useful for models that have token limits.
- **LanguageAwareTextSplitter**: Utilizes language-specific rules to split text more intelligently based on linguistic features.
- **CustomTextSplitter**: A base class that can be extended to create custom text splitting strategies.
- **SpacyTextSplitter**: Uses the SpaCy library to split text based on linguistic features such as sentences and paragraphs.