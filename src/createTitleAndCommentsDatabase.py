#encoding:utf-8
# Author : Yoshiyuki Kurose

"""
- クラスの名前はCreateProjectsDatabase

    - 目的:
        - マッチ箱に投稿された課題と、それに対するコメントをデータベースにまとめる。
        - ここでは、辞書の要素へまとめる
"""

import requests
import bs4
import re
from time import sleep

# my modules
import URLs


class CreateProjectsDatabase:

    def __init__(self, useProxy: bool = False):
        self.useProxy = useProxy
        self.proxies = {
            'http': 'http://wwwproxy.kanazawa-it.ac.jp:8080',
            'https': 'http://wwwproxy.kanazawa-it.ac.jp:8080'
        }

    # 一応完成(未テスト)
    def getProjectsIDAndTitle(self):
        """
        projectIDをkey,projectTitleをvalueとした辞書を返す
        """
        if self.useProxy:
            res_projects = requests.get(
                URLs.AllprojectURL, proxies=self.proxies)
        else:
            res_projects = requests.get(URLs.AllprojectURL)
        # sleep(1)
        # print check if an error has occurred
        print(res_projects.raise_for_status())
        soup = bs4.BeautifulSoup(res_projects.text, "html.parser")
        # 得られたタグのclass属性が"content_title"となっている要素の中で"a"タグを持つものを取得
        elems = soup.select(".content_title a")
        # IDs = [re.sub(r"\D", "", t.get('href')) for t in elems]  # elemsの中身のタグのhref属性の中身を取得
        IDs = [re.findall(r"\d+", t.get('href'))[-1]
               for t in elems]  # elemsの中身のタグのhref属性の中身を取得
        # projectTitleのリストを作成
        titles = [e.getText() for e in elems]
        # projectIDをキーtitleをバリューとした辞書を作成
        IDsAndTitles = {k: v for k, v in zip(IDs, titles)}

        return IDsAndTitles

    def getCommentsListFromID(self, ID: str):
        """
        与えられたIDから、それに紐づいたコメントのリストを作成
        """
        TitleURL = "/".join([URLs.BaseURL, "projects", ID])
        # keyをprojectID,valueをコメントの入ったリストとする辞書を作成
        if self.useProxy:
            res_project = requests.get(TitleURL, proxies=self.proxies)
        else:
            res_project = requests.get(TitleURL)

        # sleep(1)
        print(res_project)  # print check if an error has occurred
        soup = bs4.BeautifulSoup(res_project.text, "html.parser")
        elems = soup.select(".comment_text p:not(.image_all, .comment_author)")
        comments = [e.getText() for e in elems]

        return comments

    def getTitleAndComments(self):
        """ 課題のtitleと課題IDを

        Returns:
            _type_: _description_
        """
        titleIDandTitle = self.getProjectsIDAndTitle()
        return [[title, comments] for title, comments in zip(titleIDandTitle.values(), [self.getCommentsListFromID(id) for id in titleIDandTitle.keys()])]

    def update(self):
        """データベースのアップデート用

            将来的に一つのメソッドを呼び出したらデータベースがすべてupdate できるようにするために作る。

        """
        pass

# for dbg code


def dbg():
    """
    簡単な動作テスト用のコード
    """
    from pprint import pprint
    testInstance = CreateProjectsDatabase(True)
    testContent = testInstance.getTitleAndComments()
    pprint(testContent)


if __name__ == "__main__":
    # ちゃんと動くかなぁ
    dbg()
