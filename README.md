# 我楽多

プチ個人開発のたまり場。

## algorithms

### suudoku（数独）

数独を解く脳筋アルゴリズム。再帰の勉強用に使ったのだろう。単純に枝刈りしながら再帰的に総当りしている。
ただの Python だと実行が終わらないが、numba を使用することで最小ヒント問題でも 3 分以内に解けるようになった。
数独のテクニックを実装すれば何倍も早くなるらしい。

```
python main.py
```

## Designing-Math

<div class="area">
  <a href="https://yuji96.github.io/garakuta/Designing-Math/index.html">
    <button>デモを見る</button>
  </a>
</div>

svg を JavaScript で操作することで扇風機の羽をぐるぐる回したり首振りさせたりしている。
武蔵野美術大学の[古堅教授](http://furukatics.com/)が作成した
[Designing Math](http://visual-communication.design/designingMath/index.php)を参考にした。

<style>
  .area {
    background: #ecf0f3;
    display: flex;
    justify-content: center;
  }

  button {
    width: 150px;
    height: 50px;
    margin: 30px;
    font-family: 'Open Sans', Arial, sans-serif;
    background: #ecf0f3;
    border: none;
    cursor: pointer;
    border-radius: 50px;
    font-size: 1.2rem;
    font-weight: 900;
    color: #333333;
    text-shadow: -2px -2px 5px #fff, 2px 2px 5px #d1d9e6;
    box-shadow: -18px -18px 30px #fff, 18px 18px 30px #d1d9e6, inset 0 0 0 transparent, inset  0 0 0 transparent;
    transition: all 0.3s ease-out;
  }

  button:active {
    box-shadow: 0 0 0 transparent, 0 0 0 transparent, inset -18px -18px 30px #fff, inset 18px 18px 30px #d1d9e6;
  }

  button:focus {
    outline: none;
  }
</style>
