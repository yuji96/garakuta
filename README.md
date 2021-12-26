# 我楽多

プチ個人開発のたまり場。

## algorithms

### sudoku（数独）

数独を解く脳筋アルゴリズム。再帰の勉強用に使ったのだろう。単純に枝刈りしながら再帰的に総当りしている。
ただの Python だと実行が終わらないが、numba を使用することで最小ヒント問題でも 3 分以内に解けるようになった。
数独のテクニックを実装すれば何倍も早くなるらしい。

### tenpuzzle

4 つの数字から 10 を作るアルゴリズム。ナンバープレートでよくやるやつ。イテレータの勉強用に使ったのだろう。
同じロジックでイテレータとそうでない実装をしている。イテレータ、簡潔、好き。

### ox_game

マルバツゲーム。オブジェクト指向の勉強用に使ったのだろう。今、見ると褒められた設計してないな。
だからといって、今、きれいな設計が思いついているわけではないが。

## Designing-Math

svg を JavaScript で操作することで扇風機の羽をぐるぐる回したり首振りさせたりしている。
武蔵野美術大学の[古堅教授](http://furukatics.com/)が作成した
[Designing Math](http://visual-communication.design/designingMath/index.php)を参考にした。

[デモを見る](https://yuji96.github.io/garakuta/Designing-Math/index.html)

## python-quiz

- Python の基本構文
  - 最後の出力を円周率にするというコンセプトが独り歩きしている。
- numpy
  - 自作課題。一つずつ実装すれば多項式回帰が実装できるという問題。
- pandas
  - [データサイエンス 100 本ノック](https://github.com/The-Japan-DataScientist-Society/100knocks-preprocess/blob/master/docker/work/preprocess_knock_Python.ipynb)のうち、必要不可欠な問題と考えないとできない問題を抜粋した。
