# Ujimaru Text Generate

## 主題

Reformerによるツイートの模倣・生成

## 結果

しょっぺぇ

### 3000文6万文字を使用
2000step(1.5h)程度でサチった、accuracyが41.5%より上がらなくなった

### 8000文字18万文字を使用
同様に2000step程度でサチる、accuracyが46.5%程度

100万分程度あればまともな文が出てくる可能性


## 実装、データ

[Google Drive](https://drive.google.com/file/d/1-3DzppHf9vy_7NUepw-yv6qBlHjtxNkQ/view?usp=sharing)


## 詰まったところ

- trax@1.2.4と@1.2.0の間にbreaking change有り、インストールするバージョンに注意
- テキスト生成系は大規模モデルをベースに個人用のモデルで追加学習とかしてもそんなにいい結果にはならないらしい