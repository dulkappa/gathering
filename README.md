Gathering
===
[![Build Status](https://secure.travis-ci.org/dulkappa/gathering.png)](https://travis-ci.org/dulkappa/gathering)

コレクションを管理するためのWebアプリケーション.  
初期バージョンでは単純に登録/表示/編集/削除のみができる仕様にする予定.

更新履歴
---
|Date|Content|
|:-:|:-:|
|2014.8.17|プロジェクトスタート.|

環境
---
- Python : 2.7.8
- Django : 1.6.5
- SQLite : 3.7.13
- Bootstrap : 3.2.0

ディレクトリ構造
---
```shell
gathering
├ db.sqlite3
├ manage.py
├ README.md # 本ファイル
├ cms # CRUD管理ディレクトリ
| ├ __init__.py
| ├ admin.py
| ├ forms.py
| ├ models.py
| ├ tests.py
| ├ urls.py
| ├ views.py
| └ templates
|   ├ base.html
|   └ cms
|     ├ collection_edit.html
|     ├ collection_list.html
|     ├ item_edit.html
|     └ item_list.html
├ gathering # プロジェクト管理ディレクトリ
| ├ __init__.py
| ├ settings.py  
| ├ urls.py
| └ wsgi.py
└ static # bootstrapやjqueryを格納するディレクトリ
  ├ css
  | ├ bootstrap-theme.css
  | ├ bootstrap-theme.css.map
  | ├ bootstrap-theme.min.css
  | ├ bootstrap.css
  | ├ bootstrap.css.map
  | └ bootstrap.min.css
  ├ fonts
  | ├ glyphicons-halflings-regular.eot
  | ├ glyphicons-halflings-regular.svg
  | ├ glyphicons-halflings-regular.ttf
  | └ glyphicons-halflings-regular.woff
  └ js
    ├ bootstrap.js
    ├ bootstrap.min.js
    └ jquery-1.11.1.min.js
```

とりあえずやろうとしていること
---
- SQLiteを使った処理.
- 画像の表示.
- ログインとかの管理.

その他
---
特になし
