from bs4 import BeautifulSoup
import requests
import re


def main():
    rendering_engine()

# TODO: タグにリンクが紐づいている場合、タグ内のaタグのテキストを見る必要がある


def rendering_engine():
    # スクレイピングライブラリを仕様して指定したURLのHTMLを取得する
    load_url = 'https://tech-blog.voicy.jp/'
    # htmlファイルの読み込み(htmlは改行されている前提)
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    # htmlをstrに変換
    html_str = str(soup)

    # htmlのサンプル
    # html_str = '<title>タイトル</title>\n<h1>moji</h1>'

    # 書き込み用ファイルを用意
    f = open('./md/myfile.md', 'w', encoding='UTF-8')

    # タグを見つける
    tag_list = re.findall(r'<.*>.*</.*>', html_str)

    # レンダリングして今回はマークダウンにする
    for tag_include_text in tag_list:
        # タグを取得
        tag_prefix_match = re.search(r'<[a-z_0-9]*>', tag_include_text)
        if not tag_prefix_match:
            continue
        tag_prefix = tag_prefix_match.group()
        tag_suffix_match = re.search(r'</[a-z_0-9]*>', tag_include_text)
        tag_suffix = tag_suffix_match.group()

        # タグを削除して文字列だけ取り出す
        except_prefix_text = tag_include_text.replace(tag_prefix, '')
        text = except_prefix_text.replace(tag_suffix, '')
        # マークダウンに変換
        if tag_prefix == '<title>':
            f.write(F'# {text}\n')
        elif tag_prefix == '<h1>':
            f.write(F'## {text}\n')


if __name__ == "__main__":
    main()
