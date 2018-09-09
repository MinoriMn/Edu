# Edu
* julius-4.4.2.1
* dictation-kit-v4.4
を導入下で生成・実行している。

## 実行コマンド
edu.jconfのあるディレクトリで
`$ julius -C edu.jconf -nostrip -gram dict/ForAnnouncement`
と入力すると実行できる。
`ForAnnouncement`は辞書ファイル群で
`edu.jconf`は設定ファイルである。

edu.jconfの
```
-v model/lang_m/bccwj.60k.htkdic
-h model/phone_m/jnas-tri-3k16-gid.binhmm
-hlist model/phone_m/logicalTri
```
で指定されているmodelフォルダとその内部ファイルは、dictation-kit-v4.4のmodelフォルダのことである。

## Edu_software

### ver.0.1alpha
#### 構想
* Edu.pyはメイン関数系の実装を行なっているのでここから確認してください
* システムの基盤とする予定のクラスを実装しました
* タイトル画面としてのTitleクラス群を仮実装しました、Edu.pyよりスレッドによる呼び出しを予定
* Julius_receiver.pyはEduソフトとjuliusの連結を行う予定。
