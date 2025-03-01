import re
import sys

def main():
    ''' main function '''
    print(parse(input("HTML: ")))

def parse(s):
    ''' extact youtube url '''
    s = s.strip()
    # if link not in iframe
    if not re.search(r'iframe.*youtube.+iframe', s):
        return None
    if not re.search(r'src="http', s):
        return None
    # check for spelling
    if not re.search(r'youtube\.com', s):
        return None
    # delete before https
    url = re.sub('^(.*src=")',"", s)
    # delete after link
    url = re.sub('"([^,]+)',"", url)
    # delete embed
    url = re.sub(r'(embed.)',"", url)
    # replace youtube with youtu.be
    url = re.sub(r'(youtube.com)',"youtu.be", url)
    # check if https
    if not re.search("https", url):
        url = re.sub(r'(http)',"https", url)
    # check if www
    if re.search(r'w{3}+.', url):
        url = re.sub(r'w{3}+.',"", url)
    return url
    ''' '''
if __name__ == "__main__":
    main()

