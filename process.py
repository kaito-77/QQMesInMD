import re

markdown = ""


def file_load():
    filename = 'dataset/TEXT.txt'
    fr = open(filename)
    dataset = fr.readlines()
    return dataset


def save_article(markdown, path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(markdown)


def dif_situations(line):
    global markdown  # 声明 markdown 为全局变量
    pattern = re.compile(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
    matches1 = re.finditer(pattern, line)
    pattern = re.compile(r"[^！!]+[！!]+")  # 匹配句尾带有感叹号的句子
    matches2 = re.finditer(pattern, line)
    pattern = re.compile(r"[^?？]+[?？]+")  # 匹配句尾带有感叹号的句子
    matches3 = re.finditer(pattern, line)
    sentence = ""
    chasing = 0     # 追踪line的光标位置
    for match in matches1:                                              # url匹配
        url = match.group()    # 获得匹配的字符串
        sentence += line[chasing:match.start()]
        sentence += '[%s](%s)\n' % (url, url)
        chasing = match.end()
    if chasing != 0 and chasing < len(line):
        sentence += line[chasing:]
        chasing = len(line)
    for match in matches2:                                              # 感叹句变红
        color = match.group()  # 获得匹配的字符串
        sentence = line[chasing:match.start()] + '<font color="#bf616a">' + color + '</font>'
        chasing = match.end()
    if chasing != 0 and chasing < len(line):
        sentence += line[chasing:]
        chasing = len(line)
    for match in matches3:                                              # 疑问句变蓝
        color = match.group()  # 获得匹配的字符串
        sentence = line[chasing:match.start()] + '<font color="#88c0d0">' + color + '</font>'
        chasing = match.end()
    if chasing < len(line):
        sentence += line[chasing:]
    sentence = sentence.replace('￼', '[图片文件]')
    markdown += '> {}\n'.format(sentence)


def processing(text):
    global markdown
    print('Processing starts!')
    pattern = r'(\d{4}/\d{1,2}/\d{1,2})'
    title = ''
    for line in text:
        match = re.search(pattern, line)
        if match:
            title = match.group(1)
            title += '{}的聊天记录'.format(line.split()[0])
            break
    markdown = '### %s\n' % title
    pattern = r'(\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{2}:\d{2})'  # 正则表达式匹配时间
    prev_name = ''  # 当前发言者
    for line in text:
        match = re.search(pattern, line)
        if match:
            extracted_text = line[:match.start() - 1]
            if extracted_text and extracted_text != prev_name:     # 合并一连串气泡的人名
                prev_name = extracted_text
                markdown += '**{}**\n\n'.format(extracted_text)
        else:
            if line == '\n':
                continue
            dif_situations(line)
    save_article(markdown, 'dataset/output.md')
    print('Processing completed!')
    return markdown


def run_process():
    text = file_load()
    return processing(text)
