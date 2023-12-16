import re
from openai import OpenAI
import constant as constant

# html 태그 제거
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, ' ', raw_html)
  cleantext = ' '.join(cleantext.split())

  return cleantext

# 해시태그 생성
def create_tag(text):
    client = OpenAI(
        api_key=constant.OPENAI_API_KEY
    )

    prompt = f'''
    삼중 따옴표로 구분된 텍스트의 해시태그를 10개 이하로 생성해라.
    단, 생성된 해시태그만 출력한다.
    """{text}"""
    '''

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )
    
    tags = response.choices[0].message.content.lstrip("#").split(" #")

    return tags