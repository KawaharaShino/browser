package main

import (
	"fmt"
	"os"
	"regexp"
)


// TODO: 入れこのタグに対応する

func main() {
    //TODO: スクレイピングライブラリを仕様して指定したURLのHTMLを取得する

	// HTML文字列を定義
	loadUrl := "<title>タイトル</title>\n<h1>moji</h1>\n"

	// 書き込み用ファイルを用意
	f, err := os.Create("./md/myfile.md")
	if err != nil {
		fmt.Println(err)
		fmt.Println("fail to create file")
	}

	// 正規表現を定義
	tag := regexp.MustCompile("<.*>.*</.*>")
	prefix := regexp.MustCompile("<[a-z_0-9]*>")
	suffix := regexp.MustCompile("</[a-z_0-9]*>")

	// タグとテキストを抽出
	strList := tag.FindAllString(loadUrl, 100)
	for _, str := range strList {
		// タグを抽出
		strPrefix := prefix.FindStringSubmatch(str)

        // タグを削除してテキストコンテンツだけ取り出す
		exceptPrefix := prefix.ReplaceAllString(str, "")
		text := suffix.ReplaceAllString(exceptPrefix, "")
		data := []byte("")

        // タグで場合分けし、マークダウンに変換
		if strPrefix[0] == "<title>" {
			data = append(data, "# "+text+"\n"...)
		} else if strPrefix[0] == "<h1>" {
			data = append(data, "## "+text+"\n"...)
		}
		_, err := f.Write(data)
		if err != nil {
			fmt.Println(err)
			fmt.Println("fail to write file")
		}
	}
    f.Close()
}
