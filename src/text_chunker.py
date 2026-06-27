def chunk_text(text, chunk_size=500, overlap=100):
    """
    Split text into overlapping chunks.

    Parameters:
        text (str): Full document text.
        chunk_size (int): Maximum characters in each chunk.
        overlap (int): Characters shared between consecutive chunks.

    Returns:
        list: List of text chunks.
    """

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks