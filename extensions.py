def readExt():
    filename = input("File name: ").lower().strip()
    ext = filename[filename.rfind("."):]
    match(ext):
        case ".gif":
            return "image/gif"
        case ".jpeg" | ".jpg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"
print(readExt())
