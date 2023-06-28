# encoding:utf-8
# Author : Yoshiyuki Kurose

# 特定の要素を抽出するコード
from urllib.parse import urljoin, urlparse
import requests
import bs4


class CreateProjectsDatabase:
    def __init__(self):
        # 課題の一覧が乗っているページのURLをセット
        self.URL_projects = "https://kanazawa.ha4go.net/projects"
        # ベースとなるURL,マッチ箱のhome画面
        self.BaseURL = "https://kanazawa.ha4go.net"

    def getProjectNameAndURL(self):
        """
        課題のtitleをキー,URLをバリューとした辞書を作成
        """
        res_projects = requests.get(self.URL_projects)
        res_projects.raise_for_status()
        # URL_projectsから取得したhtmlソースを解析する
        ## soup = bs4.BeautifulSoup(res.text, "lxml") <- うまくいかない場合はこっちを使うこと
        try:
            soup = bs4.BeautifulSoup(res_projects.text, "html.parser")
        except:
            print("soup = bs4.BeautifulSoup(res.text, \"html.parser\"でエラー発生")
            print("'html.parser'だとエラーが起きるみたいなので'lxml'をhtmlパーサーに使用するね(はあと)")

        # 得られたタグのclass属性が"content_title"となっている要素の中で"a"タグを持つものを取得
        elems = soup.select(".content_title a")

        # elemsの中身のタグのhref属性の中身を取得
        projects_url_list = [self.createURLfromPath(
            t.get('href')) for t in elems]
        # elemsの要素のテキストコンテンツを取得
        projects_name_list = [t.getText() for t in elems]

        # 課題のtitleをキー,URLをバリューとした辞書を作成
        projects_url_and_name = {name: url for name, url in zip(
            projects_name_list, projects_url_list)}
        return projects_url_and_name

    def createURLfromPath(self, path: str = "none"):
        """

        Args:
            path (str, optional): Example -> "project/64". Defaults to "none".

        Returns:
            str: httpから始まるURL 
        """
        # 与えられたpathからURLのフルパスを生成
        joinedURL = '/'.join([self.BaseURL, path])
        return joinedURL

    def getCommentAgainstTitleFromURL(self, URL: str):
        """
        投稿された課題のタイトルに紐づいているであろうURLから対象のコメントをリストで返す
        """
        res_comments = requests.get(URL)
        res_comments.raise_for_status()

        soup = bs4.BeautifulSoup(res_comments.text, "html.parser")

        # セレクタを指定して、無駄なクラスを持った要素を除外
        elems = soup.select(".comment_text p:not(.image_all, .comment_author)")

        comments = [e.getText() for e in elems]

        return comments


if __name__ == "__main__":
    """
    以下はすべて簡単な動作テストのために書いたやつ。きちんとしたテストコードは後々書くつもり
    """
    testInstance = CreateProjectsDatabase()
    comments = testInstance.getCommentAgainstTitleFromURL(
        "https://kanazawa.ha4go.net/projects/64")
    print(comments)
    print(len(comments))
